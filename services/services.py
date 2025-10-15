import xmltodict
import requests

from collections import namedtuple
from requests.structures import CaseInsensitiveDict
from operator import attrgetter


from ..models.models import XYZLayerModel, TileMapsModel
from .checks import Checks
from ..constants import USER_URL, ImageComposition


class Services:
    checks = Checks()
    tile_maps = TileMapsModel()

    def get_user_subscription_type_from_kermap_token(self, kermap_token):
        """
        Given a Kermap Token (API key), call the backend endpoint /user-me-from-kermap-token,
        extract user_features, and return 'PRO' or 'FREE' for the geocredits feature.
        """
        from ..constants import USER_URL
        url = f"{USER_URL}/user-me-from-kermap-token/?kermap_token={kermap_token}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                features = data.get('user_features', [])
                # Find 'Nimbo GeoCredits' feature and return its feature_account
                for feat in features:
                    if feat.get('feature') == 'Nimbo GeoCredits':
                        return feat.get('feature_account', 'FREE')
                return 'FREE'
            else:
                print(f"Failed to fetch user features: {response.status_code}")
                return 'FREE'
        except Exception as e:
            print(f"Exception fetching user features from kermap_token: {e}")
            return 'FREE'

    def get_user_subscription_type(self, access_token):
        """Fetches user features and returns 'FREE' or 'PRO' for the geocredits feature."""
        from ..constants import USER_URL, GEOCREDITS_REF
        headers = {'Authorization': 'Bearer ' + access_token}
        url = USER_URL + '/user-feature-me/'
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                features = response.json()
                return self.get_geocredits_feature_type_from_features(features)
            return 'FREE'  # fallback to FREE if not found or error
        except Exception as e:
            print(f"Error fetching user features: {e}")
            return 'FREE'
            
    def get_api_key(self, email, password):
        # making request to get the access token
        access_token = self.get_access_token(
            email, password)
        if access_token is not None:
            # making request to get the api key
            return self.get_kermap_token(access_token)

    def get_access_token(self, email, password):
        # creating post request
        login_info = {
            'username': email,
            'password': password
        }
        # user login
        if self.checks.isValidEmail(email):
            res = requests.post(USER_URL+'/jwt-token/', json=login_info)

            # get access token from response
            if res.status_code == 200:
                access_token = res.json()['access']
            else:
                access_token = None

        else:
            access_token = None

        return access_token

    def get_kermap_token(self, access_token):
        # preparing headers
        headers = CaseInsensitiveDict()
        headers = {'Authorization': 'Bearer ' + access_token}

        # making request to get token
        res = requests.get(USER_URL+'/my-token/', headers=headers)

        # get kermap token from access token
        kermap_token = res.json()['key']
        return kermap_token


    def get_tile_maps(self, xml_file, subscription_type=None):
        # clearing the tile_maps_list
        self.tile_maps.layers.clear()
        
        # turning the xml to dict
        tms_dict = xmltodict.parse(xml_file)

        # getting a list of dictionnaries containing the urls for nimbo services
        tms_list = tms_dict['TileMapService']['TileMaps']['TileMap']

        # creating the tile maps list of XYZLayer
        layer_record = namedtuple('LayerRecord', 'title srs profile href')
        for layer in tms_list:
            # suppression the @ character from the key
            new_layer = {k.replace(u'@', ''): v for k, v in layer.items()}
            # creating the record from the layer dict
            rec = layer_record(**new_layer)
            
            # filtering for FREE/PRO
            if subscription_type == 'FREE':
                # getting the year, month and composition of the layer
                # print(rec.href.split('/'))
                data = rec.href.split('/')[6].split('@')[0].split('_')
                # Only allow watermark services for FREE
                # Only process if tileset is in expected format: watermark_YEAR_MONTH_COMPO
                # print("DEBUG: Processing data: data={data}")
                if len(data) == 4 and data[0].lower() == 'watermark':
                    year, month, compo = data[1], data[2], data[3]
                    # Do NOT zero-pad month for FREE users
                    month = str(int(month)) if month.isdigit() else month
                    # print('month ==>',month)
                    # print("DEBUG: Adding layer: year={year}, month={month}, composition={compo}")
                    self.tile_maps.layers.append(XYZLayerModel(
                        rec.title, rec.srs, rec.profile, rec.href, year=year, month=month, composition=compo))
                    self.tile_maps.layers.sort(key=lambda x: (int(x.year), int(x.month)))
            elif subscription_type == 'PRO':
                # print("dans le else a la génération")
                # getting the year, month and composition of the layer
                data = rec.href.split('/')[6].split('@')[0].split('_')
                # PRO or default: all layers except water/rasterdem/copernicus/SR
                if ('water' not in data) and ('rasterdem' not in data) and ('copernicus' not in data) and ('SR' not in data):
                    # For PRO, do not zero-pad month, always use int
                    month = str(int(data[1])) if data[1].isdigit() else data[1]
                    self.tile_maps.layers.append(XYZLayerModel(
                        rec.title, rec.srs, rec.profile, rec.href, year=data[0], month=month, composition=data[2]))
                    self.tile_maps.layers.sort(key=lambda x: (int(x.year), int(x.month)))
            elif subscription_type == 'PRO HD':
                # print("dans le else a la génération")
                # getting the year, month and composition of the layer
                data = rec.href.split('/')[6].split('@')[0].split('_')
                # PRO or default: all layers except water/rasterdem/copernicus/SR
                if ('water' not in data) and ('rasterdem' not in data) and ('copernicus' not in data):
                    # For PRO, do not zero-pad month, always use int
                    if ('SR' in data):
                        data.remove('SR')
                    month = str(int(data[1])) if data[1].isdigit() else data[1]
                    self.tile_maps.layers.append(XYZLayerModel(
                        rec.title, rec.srs, rec.profile, rec.href, year=data[0], month=month, composition=data[2]))
                    self.tile_maps.layers.sort(key=lambda x: (int(x.year), int(x.month)))
        return self.tile_maps

    def get_month_name(self, month):
        if month == "01" or month == "1":
            return "January"
        elif month == "02" or month == "2":
            return"February"
        elif month == "03" or month == "3":
            return "March"
        elif month == "04" or month == "4":
            return "April"
        elif month == "05" or month == "5":
            return "May"
        elif month == "06" or month == "6":
            return "June"
        elif month == "07" or month == "7":
            return "July"
        elif month == "08" or month == "8":
            return "August"
        elif month == "09" or month == "9":
            return "September"
        elif month == "10":
            return "October"
        elif month == "11":
            return "November"
        elif month == "12":
            return "December"

    def get_composition_name(self, composition):
        if composition == "1":
            return ImageComposition.NATURAL.__str__()
        elif composition == "2":
            return ImageComposition.INFRARED.__str__()
        elif composition == "3":
            return ImageComposition.VEGETATION.__str__()
        elif composition == "4":
            return ImageComposition.RADAR.__str__()
        elif composition == "5":
            return ImageComposition.SUPER_RES.__str__()

    def get_min_year(self, tile_maps):
        years = self.get_years(tile_maps)
        return min(years)

    def get_max_year(self, tile_maps):
        years = self.get_years(tile_maps)
        return max(years)

    def get_years(self, tile_maps):
        years = set()
        for layer in tile_maps.layers:
            years.add(int(layer.year))
        return list(years)

    def get_composition_from_layers(self, tile_maps):
        compositions = set()
        for layer in tile_maps.layers:
            compositions.add(int(layer.composition))
        return list(compositions)

    def get_month_for_this_year(self, year, tile_maps):
        months = set()
        for layer in tile_maps.layers:
            if layer.year == year:
                months.add(int(layer.month))
        return list(months)

    def filtering_layers(self, data):
        # print(f"DEBUG: filtering_layers called, data={data}")  # Debug log
        for layer in self.tile_maps.layers:
            # print(f"DEBUG: Comparing layer: month_name={self.get_month_name(layer.month)}, year={layer.year}, composition_name={self.get_composition_name(layer.composition)}")
            # print(f"DEBUG: Against data: month={data[0]}, year={data[1]}, composition={data[2]}")
            # print(f"DEBUG: layer={layer}")  # Debug log
            # checking which layer possess this year, month and composition
            if  self.get_month_name(layer.month) == data[0]\
                and layer.year == data[1] \
                    and self.get_composition_name(layer.composition) == data[2]:
                return layer



