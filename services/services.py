import re

import xmltodict
import requests

from collections import namedtuple
from requests.structures import CaseInsensitiveDict


from ..models.models import XYZLayerModel, TileMapsModel
from .checks import Checks
from ..constants import MONTH_NAMES, SERVICE_FEATURE_URL, SERVICE_TOKEN_URL, TIMEOUT, USER_URL
from qgis.core import Qgis, QgsMessageLog


class Services:
    """
    Services class to manage services calls

    Attributes
    ----------
    tile_maps : TileMapsModel
        TileMapsModel instance
    checks : Checks
        Checks instance
    _authorized_features_cache : dict
        Dictionary to cache authorized features
    """

    def __init__(self):
        """
        Initialize class
        """
        self.tile_maps = TileMapsModel()
        self.checks = Checks()
        self._authorized_features_cache = {}

    def get_access_token(self, email, password):
        """
        Get access token from email and password

        Parameters
        ----------
        email : str
            User email
        password : str
            User password

        Returns
        -------
        str
            Access token
        """
        # Check if email is valid
        if self.checks.isValidEmail(email):
            # Create post request
            login_info = {
                'username' : email,
                'password' : password
            }

            response = requests.post(USER_URL + '/jwt-token/', json = login_info, timeout=TIMEOUT)
        else:
            raise Exception(f"Failed to fetch access token: email is not valid")

        # If response status code is 200, get the access token
        if response.status_code == 200:
            return response.json()['access']
        # If it fails, raise an exception
        else:
            raise Exception(f"Failed to fetch access token: {response.status_code}")
    

    def get_kermap_token(self, access_token):
        """
        Get kermap token from access token

        Parameters
        ----------
        access_token : str
            Access token

        Returns
        -------
        str
            Kermap token
        """
        # Prepare headers
        headers = CaseInsensitiveDict()
        headers = {'Authorization' : 'Bearer ' + access_token}

        # Make request to get token
        response = requests.get(USER_URL + '/my-token/', headers = headers, timeout=TIMEOUT)

        # If the response status is 200, return the kermap token
        if response.status_code == 200:
            return response.json()['key']
        # If it fails, raise an exception
        else:
            raise Exception(f"Failed to fetch kermap token: {response.status_code}")


    def get_user_informations(self, kermap_token):
        """
        Get user informations from kermap token

        Parameters
        ----------
        kermap_token : str
            Kermap token

        Returns
        -------
        dict
            User informations
        """
        # Get the request URL with the API key
        request_url = SERVICE_TOKEN_URL + kermap_token

        # Prepare headers
        headers = {'User-Agent': "QGIS Nimbo plugin"}

        # Make the request to get user features
        response = requests.get(request_url, headers = headers, timeout=TIMEOUT)

        # If the response status is 200, get the user features
        if response.status_code == 200:
            self._authorized_features_cache.clear()
            return response
        # If it fails, raise an exception
        else:
            raise Exception(f"Failed to fetch user features: {response.status_code}")
    

    def get_user_subscription_type_from_kermap_token(self, kermap_token):
        """
        Get user subscription type from kermap token (API Key),
        call the backend endpoint /user-me-from-kermap-token 
        and extract user_features to know the subscription type

        Parameters
        ----------
        kermap_token : str
            Kermap token

        Returns
        -------
        str
            User subscription type
        """
        # Get the request URL
        url = f"{USER_URL}/user-me-from-kermap-token/?kermap_token={kermap_token}"

        # Make the request to get user features
        response = requests.get(url, timeout=TIMEOUT)

        # If the response status is 200, get the user features
        if response.status_code == 200:
            data = response.json()
            features = data.get('user_features', [])
            # Find 'Nimbo GeoCredits' feature and return its feature_account
            for feat in features:
                if feat.get('feature') == 'Nimbo GeoCredits':
                    return feat.get('feature_account', 'FREE')
            raise Exception(f"Nimbo GeoCredits feature not found in user features")
        # If it fails, raise an exception
        else:
            raise Exception(f"Failed to fetch user subscription type: {response.status_code}")


    def get_tile_maps(self, xml_file):
        """
        Get tile maps from xml file and subscription type

        Parameters
        ----------
        xml_file : str
            Xml file

        Returns
        -------
        list
            List of tile maps
        """
        # Create a set to store hrefs to avoid duplicates
        hrefs = set()

        # Clear the tile_maps_list
        self.tile_maps.layers.clear()
        # Turn the xml to dict
        tms_dict = xmltodict.parse(xml_file)

        # Get a list of dictionnaries containing the urls for nimbo services
        tms_list = tms_dict['TileMapService']['TileMaps']['TileMap']

        # Create the tile maps list of XYZLayer
        layer_record = namedtuple('LayerRecord', 'title srs profile href')

        # Get the list of authorized tile maps
        href_accepted = self.get_href_compositions_from_subscription_type('ALL')

        # Create the tile maps list
        for layer in tms_list:
            href = layer.get('@href')
            # Check if the href is already in the set
            if href in hrefs:
                QgsMessageLog.logMessage(f"Duplicate href {href} found in tile maps", level=Qgis.MessageLevel.Warning)
                continue
            hrefs.add(href)

            # Check if the href layer is valid compared with the authorized hrefs
            if self.checks.isValidLayer(href, href_accepted):
                # Create the record from the layer dict
                rec = layer_record(
                    title=layer.get('@title'),
                    srs=layer.get('@srs'),
                    profile=layer.get('@profile'),
                    href=href
                )
                
                # Get the raw id
                raw_id = href.split('/tms/1.0.0/')[-1].split('@')[0]
                
                # Remove the prefix from the raw id to keep only the tile map id
                # r'^[a-zA-Z_]*?(\d)' for the part before the first number and r'\1' for the beginning of the number
                raw_id = re.sub(r'^[a-zA-Z_]*?(\d)', r'\1', raw_id)
                
                # Add the tile map
                self._add_tile_map(rec, raw_id)

        # Sort the tile maps list
        self.tile_maps.layers.sort(key=lambda x: (
            int(x.year) if str(x.year).isdigit() else 0,
            int(x.month) if str(x.month).isdigit() else 0
        ))

        return self.tile_maps
    

    def _add_tile_map(self, rec, raw_id):
        """
        Add tile map to tile maps list with the raw id and the layer record

        Parameters
        ----------
        rec : LayerRecord
            Layer record
        raw_id : str
            Raw id
        """
        # Split the raw id
        data = raw_id.split('_')

        # Check if the layer is normal and add it
        if len(data) >= 3 and data[-3].isdigit() and data[-2].isdigit() and data[-1].isdigit():
            layer = XYZLayerModel(
                title=rec.title,
                srs=rec.srs,
                profile=rec.profile,
                href=rec.href,
                year=data[-3],
                month=data[-2],
                composition=data[-1]
            )
            self.tile_maps.layers.append(layer)
        else:
            layer = XYZLayerModel(
                title=rec.title,
                srs=rec.srs,
                profile=rec.profile,
                href=rec.href,
                year=None,
                month=None,
                composition=data[-1]
            )
            self.tile_maps.layers.append(layer)


    def get_month_name(self, month):
        """
        Get month name from month number

        Parameters
        ----------
        month : str
            Month number

        Returns
        -------
        str
            Month name
        """
        return MONTH_NAMES.get(int(month), '')


    def get_years(self):
        """
        Get years

        Returns
        -------
        list
            List of years
        """
        years = set()
        # Get the years from the layers
        for layer in self.tile_maps.layers:
            if layer.year is None:
                continue
            years.add(int(layer.year))
        return list(years)


    def _get_authorized_features(self, subscription_type):
        """
        Get authorized features from subscription type

        Parameters
        ----------
        subscription_type : str
            Subscription type

        Returns
        -------
        list
            List of authorized features
        """
        # If subscription type is None, raise an exception
        if subscription_type is None:
            raise Exception(f"Failed to fetch authorized features: subscription type is None")
        
        # Get all features
        elif subscription_type == 'ALL':
            request_url = f"{SERVICE_FEATURE_URL}"
        # Get features from subscription type
        else:
            request_url = f"{SERVICE_FEATURE_URL}/?feature_account={subscription_type.upper()}"

        response = requests.get(request_url, timeout=TIMEOUT)
        # If the response status is 200, return the authorized features
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch authorized features: {response.status_code}")


    def get_href_compositions_from_subscription_type(self, subscription_type):
        """
        Get compositions from subscription type

        Parameters
        ----------
        subscription_type : str
            Subscription type

        Returns
        -------
        list
            List of compositions
        """
        # Get authorized features
        if subscription_type in self._authorized_features_cache:
            data = self._authorized_features_cache[subscription_type]
        else:
            self._authorized_features_cache[subscription_type] = self._get_authorized_features(subscription_type)
            data = self._authorized_features_cache[subscription_type]

        # If data is None, raise an exception
        if data is None:
            raise Exception(f"Failed to fetch authorized features: data is None")
        
        # Get the list of compositions
        compositions_list = []
        # If subscription type is ALL, get the list of compositions from all features
        if subscription_type == 'ALL':
            for feature in data:
                for composition in feature.get('service_included'):
                    if composition.get('request') not in compositions_list:
                        compositions_list.append(composition.get('request'))
            return compositions_list
        # If subscription type is not ALL, get the list of compositions from the subscription type
        else:
            for composition in data[0].get('service_included'):
                compositions_list.append(composition.get('request'))
            return compositions_list

    def get_compositions_mapping(self, subscription_type):
        """
        Get compositions name from subscription type

        Parameters
        ----------
        subscription_type : str
            Subscription type

        Returns
        -------
        list
            List of compositions name
        """
        # Get authorized features
        if 'ALL' in self._authorized_features_cache:
            data = self._authorized_features_cache['ALL']
        else:
            self._authorized_features_cache['ALL'] = self._get_authorized_features('ALL')
            data = self._authorized_features_cache['ALL']

        # If data is None, raise an exception
        if data is None:
            raise Exception(f"Failed to fetch authorized features: data is invalid")

        # Build name mapping for ALL
        api_mapping = {}
        for feature in data:
            for service in feature.get('service_included', []):
                request = service.get('request', '')
                # Get the composition number with _<number>@
                match = re.search(r'_(\d+)@', request)
                if match:
                    # Get the composition number
                    comp_int = int(match.group(1))
                    # Get the full composition name like "RGB" or "NIR_RED"
                    name = service.get('service', '').split('_', 1)[-1].replace('_', ' ')
                    if comp_int not in api_mapping and 'WATERMARK' not in name.upper():
                        api_mapping[comp_int] = name

        # Get hrefs the user has access to
        href_allowed = self.get_href_compositions_from_subscription_type(subscription_type)

        # If href_allowed is None, raise an exception
        if href_allowed is None:
            raise Exception(f"Failed to fetch authorized features: href_allowed is invalid")

        # Build name mapping for the user subscription
        comp_mapping = {}
        for layer in self.tile_maps.layers:
            comp_int = int(layer.composition)
            if comp_int not in comp_mapping:
                if self.checks.isValidLayer(layer.href, href_allowed):
                    if comp_int in api_mapping:
                        comp_mapping[comp_int] = api_mapping[comp_int]

        return comp_mapping