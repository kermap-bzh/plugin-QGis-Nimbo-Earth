# -*- coding: utf-8 -*-
"""
Unitary tests for services.py (NimboEarth QGIS Plugin)

These tests cover :
- get_access_token
- get_kermap_token
- get_user_informations
- get_user_subscription_type_from_kermap_token
- get_tile_maps / _add_tile_map
- get_month_name
- get_years
- _get_authorized_features
- get_href_compositions_from_subscription_type
- get_compositions_mapping
"""

import os
import sys
import unittest
import importlib.util
from collections import namedtuple
from unittest.mock import MagicMock, patch

# ---------------------------------------------------------------------------
# 1. Load externals dependencies (whl) with plugin mechanism
# ---------------------------------------------------------------------------
_plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_services_dir = os.path.join(_plugin_dir, "services")

if _services_dir not in sys.path:
    sys.path.insert(0, _services_dir)
if _plugin_dir not in sys.path:
    sys.path.insert(0, _plugin_dir)

from imports import ensure_import  # services/imports.py

ensure_import("xmltodict")
ensure_import("requests")

# ---------------------------------------------------------------------------
# 2. Stub QGIS (not available out of QGIS environment)
# ---------------------------------------------------------------------------
_qgis = MagicMock()
for _mod in (
    "qgis",
    "qgis.PyQt",
    "qgis.PyQt.QtCore",
    "qgis.PyQt.QtGui",
    "qgis.PyQt.QtWidgets",
    "qgis.core",
):
    sys.modules.setdefault(_mod, _qgis)


# ---------------------------------------------------------------------------
# 3. Import plugin modules with importlib
# ---------------------------------------------------------------------------
def _load(module_name, rel_path):
    """
    Load a module from a relative path

    Parameters
    ----------
    module_name : str
        Name of the module to load
    rel_path : str
        Relative path to the module
    """
    path = os.path.join(_plugin_dir, rel_path)

    full_name = f"plugin_QGis_Nimbo_Earth.{module_name}"

    spec = importlib.util.spec_from_file_location(full_name, path)
    mod = importlib.util.module_from_spec(spec)

    sys.modules[full_name] = mod
    spec.loader.exec_module(mod)

    return mod


constants_mod = _load("constants", "constants.py")
checks_mod = _load("services.checks", "services/checks.py")
models_mod = _load("models.models", "models/models.py")
services_mod = _load("services.services", "services/services.py")

Checks = checks_mod.Checks
XYZLayerModel = models_mod.XYZLayerModel
TileMapsModel = models_mod.TileMapsModel
Services = services_mod.Services

# ---------------------------------------------------------------------------
# Data for tests
# ---------------------------------------------------------------------------

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<TileMapService>
  <TileMaps>
    <TileMap title="RGB 2023-06" srs="EPSG:3857" profile="none"
             href="https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2023_06_1@kermap/"/>
    <TileMap title="NIR 2022-12" srs="EPSG:3857" profile="none"
             href="https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2022_12_2@kermap/"/>
    <TileMap title="RGB 2023-06" srs="EPSG:3857" profile="none"
             href="https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2023_06_1@kermap/"/>
  </TileMaps>
</TileMapService>"""

SAMPLE_FEATURES_ALL = [
    {
        "service_included": [
            {"request": "nimbo_2023_06_1@kermap", "service": "NIMBO_RGB"},
            {"request": "nimbo_2022_12_2@kermap", "service": "NIMBO_NIR"},
        ]
    }
]

SAMPLE_FEATURES_FREE = [
    {
        "service_included": [
            {"request": "nimbo_2023_06_1@kermap", "service": "NIMBO_RGB"},
        ]
    }
]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestIsValidEmail(unittest.TestCase):
    """
    Tests about Checks.isValidEmail

    Attributes
    ----------
    checks : Checks
        Checks instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.checks = Checks()

    def test_valid_email(self):
        """
        Test with a valid email
        """
        self.assertTrue(self.checks.isValidEmail("user@example.com"))

    def test_email_with_subdomain(self):
        """
        Test with a valid email with subdomain
        """
        self.assertTrue(self.checks.isValidEmail("user@mail.example.co.uk"))

    def test_email_without_at(self):
        """
        Test with a valid email without @
        """
        self.assertFalse(self.checks.isValidEmail("userexample.com"))

    def test_email_without_domain(self):
        """
        Test with a valid email without domain
        """
        self.assertFalse(self.checks.isValidEmail("user@"))

    def test_email_without_tld(self):
        """
        Test with a valid email without tld
        """
        self.assertFalse(self.checks.isValidEmail("user@example"))

    def test_empty_email(self):
        """
        Test with an empty email
        """
        self.assertFalse(self.checks.isValidEmail(""))


class TestIsValidLayer(unittest.TestCase):
    """
    Tests about Checks.isValidLayer

    Attributes
    ----------
    checks : Checks
        Checks instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.checks = Checks()

    def test_valid_href(self):
        """
        Test with a valid href
        """
        href = "https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2023_06_1@kermap/"
        self.assertTrue(self.checks.isValidLayer(href, ["nimbo_2023_06_1@kermap"]))

    def test_invalid_href(self):
        """
        Test with an invalid href
        """
        href = "https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2023_06_99@kermap/"
        self.assertFalse(self.checks.isValidLayer(href, ["nimbo_2023_06_1@kermap"]))

    def test_empty_list(self):
        """
        Test with an empty list of patterns
        """
        href = "https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2023_06_1@kermap/"
        self.assertFalse(self.checks.isValidLayer(href, []))

    def test_several_patterns(self):
        """
        Test with several patterns
        """
        href = "https://prod.nimbo.earth/mapcache/tms/1.0.0/nimbo_2022_12_2@kermap/"
        patterns = ["nimbo_2023_06_1@kermap", "nimbo_2022_12_2@kermap"]
        self.assertTrue(self.checks.isValidLayer(href, patterns))


class TestGetAccessToken(unittest.TestCase):
    """
    Tests about Services.get_access_token

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    @patch("requests.post")
    def test_valid_access_token(self, mock_post):
        """
        Test with a valid access token

        Parameters
        ----------
        mock_post : MagicMock
            Mocked post
        """
        mock_post.return_value = MagicMock(
            status_code=200, json=lambda: {"access": "tok123"}
        )
        result = self.svc.get_access_token("user@test.com", "pass")
        self.assertEqual(result, "tok123")

    @patch("requests.post")
    def test_invalid_exception(self, mock_post):
        """
        Test with an invalid access token

        Parameters
        ----------
        mock_post : MagicMock
            Mocked post
        """
        mock_post.return_value = MagicMock(status_code=401)
        with self.assertRaises(Exception):
            self.svc.get_access_token("user@test.com", "wrong")

    def test_invalid_email_exception(self):
        """
        Test with an invalid email
        """
        with self.assertRaises(Exception):
            self.svc.get_access_token("pas-un-email", "pass")

    def test_email_without_domain_exception(self):
        """
        Test with an email without domain
        """
        with self.assertRaises(Exception):
            self.svc.get_access_token("user@", "pass")

    @patch("requests.post", side_effect=Exception("réseau KO"))
    def test_network_exception(self, _):
        """
        Test with a network exception

        Parameters
        ----------
        _ : MagicMock
            Mocked post
        """
        with self.assertRaises(Exception):
            self.svc.get_access_token("user@test.com", "pass")


class TestGetKermapToken(unittest.TestCase):
    """
    Tests about Services.get_kermap_token

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    @patch("requests.get")
    def test_kermap_token(self, mock_get):
        """
        Test with a valid kermap token

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: {"key": "kmap-abc"}
        )
        result = self.svc.get_kermap_token("access-token")
        self.assertEqual(result, "kmap-abc")

    @patch("requests.get")
    def test_403_exception(self, mock_get):
        """
        Test with a 403 exception (unauthorized access token)

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = MagicMock(status_code=403)
        with self.assertRaises(Exception):
            self.svc.get_kermap_token("access-token")

    @patch("requests.get", side_effect=ConnectionError("timeout"))
    def test_network_exception(self, _):
        """
        Test with a network exception

        Parameters
        ----------
        _ : MagicMock
            Mocked get
        """
        with self.assertRaises(Exception):
            self.svc.get_kermap_token("access-token")


class TestGetUserInformations(unittest.TestCase):
    """
    Tests about Services.get_user_informations

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()
        self.svc._authorized_features_cache["ALL"] = ["cached"]

    @patch("requests.get")
    def test_empty_response(self, mock_get):
        """
        Test with an empty response

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        fake_resp = MagicMock(status_code=200)
        mock_get.return_value = fake_resp
        result = self.svc.get_user_informations("kermap-token")
        self.assertEqual(result, fake_resp)
        self.assertEqual(self.svc._authorized_features_cache, {})

    @patch("requests.get")
    def test_not_200_exception(self, mock_get):
        """
        Test with a non 200 response

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = MagicMock(status_code=500)
        with self.assertRaises(Exception):
            self.svc.get_user_informations("kermap-token")
        self.assertIn("ALL", self.svc._authorized_features_cache)

    @patch("requests.get", side_effect=Exception("erreur réseau"))
    def test_network_exception(self, _):
        """
        Test with a network exception

        Parameters
        ----------
        _ : MagicMock
            Mocked get
        """
        with self.assertRaises(Exception):
            self.svc.get_user_informations("kermap-token")


class TestGetUserSubscriptionType(unittest.TestCase):
    """
    Tests about Services.get_user_subscription_type

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    def _mock_response(self, user_features):
        """
        Mock response

        Parameters
        ----------
        user_features : list
            List of user features

        Returns
        -------
        MagicMock
        """
        resp = MagicMock(status_code=200)
        resp.json.return_value = {"user_features": user_features}
        return resp

    @patch("requests.get")
    def test_feature_account_geocredits(self, mock_get):
        """
        Test with a feature account geocredits

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = self._mock_response(
            [
                {"feature": "Other Feature", "feature_account": "PAID"},
                {"feature": "Nimbo GeoCredits", "feature_account": "PREMIUM"},
            ]
        )
        result = self.svc.get_user_subscription_type_from_kermap_token("tok")
        self.assertEqual(result, "PREMIUM")

    @patch("requests.get")
    def test_exception_empty_geocredits(self, mock_get):
        """
        Test with an empty geocredits

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = self._mock_response(
            [
                {"feature": "Autre", "feature_account": "PAID"},
            ]
        )
        with self.assertRaises(Exception):
            self.svc.get_user_subscription_type_from_kermap_token("tok")

    @patch("requests.get")
    def test_exception_empty_list(self, mock_get):
        """
        Test with an empty list

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = self._mock_response([])
        with self.assertRaises(Exception):
            self.svc.get_user_subscription_type_from_kermap_token("tok")

    @patch("requests.get")
    def test_not_200_exception(self, mock_get):
        """
        Test with a non 200 response

        Parameters
        ----------
        mock_get : MagicMock
            Mocked get
        """
        mock_get.return_value = MagicMock(status_code=401)
        with self.assertRaises(Exception):
            self.svc.get_user_subscription_type_from_kermap_token("tok")

    @patch("requests.get", side_effect=Exception("réseau KO"))
    def test_network_exception(self, _):
        """
        Test with a network exception

        Parameters
        ----------
        _ : MagicMock
            Mocked get
        """
        with self.assertRaises(Exception):
            self.svc.get_user_subscription_type_from_kermap_token("tok")


class TestGetTileMaps(unittest.TestCase):
    """
    Tests about Services.get_tile_maps and Services._add_tile_map

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()
        self.svc._authorized_features_cache["ALL"] = SAMPLE_FEATURES_ALL

    def test_parse_xml_tile_maps(self):
        """
        Test with a valid xml
        """
        result = self.svc.get_tile_maps(SAMPLE_XML)
        self.assertEqual(len(result.layers), 2)

    def test_hrefs_duplication(self):
        """
        Test with a valid xml with hrefs duplication
        """
        result = self.svc.get_tile_maps(SAMPLE_XML)
        hrefs = [l.href for l in result.layers]
        self.assertEqual(len(hrefs), len(set(hrefs)))

    def test_sort(self):
        """
        Test with a valid xml and sort
        """
        result = self.svc.get_tile_maps(SAMPLE_XML)
        pairs = [(l.year, l.month) for l in result.layers]
        self.assertEqual(pairs, sorted(pairs))

    def test_year_month_composition(self):
        """
        Test a layer with a valid xml
        """
        result = self.svc.get_tile_maps(SAMPLE_XML)
        layer = next(l for l in result.layers if l.composition == "1")
        self.assertEqual(layer.year, "2023")
        self.assertEqual(layer.month, "06")

    def test_clear_layers(self):
        """
        Test if layers are cleared with a valid xml
        """
        self.svc.get_tile_maps(SAMPLE_XML)
        result = self.svc.get_tile_maps(SAMPLE_XML)
        self.assertEqual(len(result.layers), 2)


class TestAddTileMap(unittest.TestCase):
    """
    Tests about Services._add_tile_map

    Attributes
    ----------
    svc : Services
        Services instance
    rec : LayerRecord
        Layer record
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()
        LayerRecord = namedtuple("LayerRecord", "title srs profile href")
        self.rec = LayerRecord(
            title="RGB",
            srs="EPSG:3857",
            profile="none",
            href="https://example.com/tms/1.0.0/nimbo_2023_06_1@kermap/",
        )

    def test_normal_layer(self):
        """
        Test with a normal layer
        """
        self.svc._add_tile_map(self.rec, "2023_06_1")
        layer = self.svc.tile_maps.layers[-1]
        self.assertEqual(layer.year, "2023")
        self.assertEqual(layer.month, "06")
        self.assertEqual(layer.composition, "1")

    def test_layer_without_date(self):
        """
        Test with a layer without date
        """
        self.svc._add_tile_map(self.rec, "special_1")
        layer = self.svc.tile_maps.layers[-1]
        self.assertIsNone(layer.year)
        self.assertIsNone(layer.month)
        self.assertEqual(layer.composition, "1")


class TestGetMonthName(unittest.TestCase):
    """
    Tests about Services.get_month_name

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    def test_valid_months(self):
        """
        Test with valid months
        """
        cases = {1: "January", 6: "June", 12: "December"}
        for num, name in cases.items():
            with self.subTest(month=num):
                self.assertEqual(self.svc.get_month_name(num), name)

    def test_string_month(self):
        """
        Test with a string month
        """
        self.assertEqual(self.svc.get_month_name("3"), "March")

    def test_invalid_months(self):
        """
        Test with an invalid month
        """
        self.assertEqual(self.svc.get_month_name(99), "")


class TestGetYears(unittest.TestCase):
    """
    Tests about Services.get_years

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()
        self.svc.tile_maps.layers = [
            XYZLayerModel(year="2021", month="01", composition="1"),
            XYZLayerModel(year="2022", month="06", composition="1"),
            XYZLayerModel(year=None, month=None, composition="2"),
        ]

    def test_years_without_none(self):
        """
        Test with valid years without None
        """
        years = self.svc.get_years()
        self.assertIn(2021, years)
        self.assertIn(2022, years)
        self.assertNotIn(None, years)

    def test_without_duplication(self):
        """
        Test without duplication
        """
        self.svc.tile_maps.layers.append(
            XYZLayerModel(year="2021", month="12", composition="1")
        )
        years = self.svc.get_years()
        self.assertEqual(len(years), len(set(years)))


class TestGetAuthorizedFeatures(unittest.TestCase):
    """
    Tests about Services._get_authorized_features

    Attributes
    ----------
    svc : Services
        Services instance
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    def test_subscription_type_none(self):
        """
        Test with a None subscription type
        """
        with self.assertRaises(Exception):
            self.svc._get_authorized_features(None)

    @patch("requests.get")
    def test_valid_features(self, mock_get):
        """
        Test with valid features

        Parameters
        ----------
        mock_get : MagicMock
            Mocked requests.get
        """
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: SAMPLE_FEATURES_ALL
        )
        result = self.svc._get_authorized_features("ALL")
        self.assertEqual(result, SAMPLE_FEATURES_ALL)

    @patch("requests.get")
    def test_invalid_features(self, mock_get):
        """
        Test with an invalid features

        Parameters
        ----------
        mock_get : MagicMock
            Mocked requests.get
        """
        mock_get.return_value = MagicMock(status_code=500)
        with self.assertRaises(Exception):
            self.svc._get_authorized_features("ALL")

    @patch("requests.get", side_effect=Exception("timeout"))
    def test_timeout_exception(self, _):
        """
        Test with a timeout exception

        Parameters
        ----------
        _ : MagicMock
            Mocked requests.get
        """
        with self.assertRaises(Exception):
            self.svc._get_authorized_features("ALL")

    @patch("requests.get")
    def test_subscription_type_free(self, mock_get):
        """
        Test with a free subscription type

        Parameters
        ----------
        mock_get : MagicMock
            Mocked requests.get
        """
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: SAMPLE_FEATURES_FREE
        )
        self.svc._get_authorized_features("FREE")
        call_url = mock_get.call_args[0][0]
        self.assertIn("feature_account=FREE", call_url)

    @patch("requests.get")
    def test_subscription_type_all(self, mock_get):
        """
        Test with an all subscription type

        Parameters
        ----------
        mock_get : MagicMock
            Mocked requests.get
        """
        mock_get.return_value = MagicMock(
            status_code=200, json=lambda: SAMPLE_FEATURES_ALL
        )
        self.svc._get_authorized_features("ALL")
        call_url = mock_get.call_args[0][0]
        self.assertNotIn("feature_account", call_url)


class TestGetCompositionsFromSubscriptionType(unittest.TestCase):
    """
    Tests about Services.get_href_compositions_from_subscription_type

    Attributes
    ----------
    svc : Services
        Services
    """

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()

    def test_all_compositions(self):
        """
        Test with an all subscription type
        """
        self.svc._authorized_features_cache["ALL"] = SAMPLE_FEATURES_ALL
        result = self.svc.get_href_compositions_from_subscription_type("ALL")
        self.assertIn("nimbo_2023_06_1@kermap", result)
        self.assertIn("nimbo_2022_12_2@kermap", result)

    def test_all_without_duplication(self):
        """
        Test without duplication
        """
        features_avec_doublons = [
            {
                "service_included": [
                    {"request": "nimbo_2023_06_1@kermap"},
                    {"request": "nimbo_2023_06_1@kermap"},
                ]
            }
        ]
        self.svc._authorized_features_cache["ALL"] = features_avec_doublons
        result = self.svc.get_href_compositions_from_subscription_type("ALL")
        self.assertEqual(len(result), len(set(result)))

    def test_subscription_type_free_compositions(self):
        """
        Test with a free subscription type
        """
        self.svc._authorized_features_cache["FREE"] = SAMPLE_FEATURES_FREE
        result = self.svc.get_href_compositions_from_subscription_type("FREE")
        self.assertEqual(result, ["nimbo_2023_06_1@kermap"])

    def test_data_none(self):
        """
        Test with a None data
        """
        self.svc._authorized_features_cache["ALL"] = None
        with self.assertRaises(Exception):
            self.svc.get_href_compositions_from_subscription_type("ALL")

    def test_use_cache(self):
        """
        Test with use cache
        """
        self.svc._authorized_features_cache["ALL"] = SAMPLE_FEATURES_ALL
        with patch.object(self.svc, "_get_authorized_features") as mock_feat:
            self.svc.get_href_compositions_from_subscription_type("ALL")
            mock_feat.assert_not_called()


class TestGetCompositionsMapping(unittest.TestCase):
    """
    Tests about Services.get_compositions_mapping

    Attributes
    ----------
    svc : Services
        Services
    FEATURES_ALL_WITH_NAMES : list
        List of features
    """

    FEATURES_ALL_WITH_NAMES = [
        {
            "service_included": [
                {"request": "nimbo_2023_06_1@kermap", "service": "NIMBO_RGB"},
                {"request": "nimbo_2022_12_2@kermap", "service": "NIMBO_NIR RED"},
                {"request": "nimbo_2023_06_3@kermap", "service": "NIMBO_RGB_WATERMARK"},
            ]
        }
    ]

    def setUp(self):
        """
        Initialize class
        """
        self.svc = Services()
        self.svc._authorized_features_cache["ALL"] = self.FEATURES_ALL_WITH_NAMES
        self.svc._authorized_features_cache["FREE"] = SAMPLE_FEATURES_FREE
        self.svc.tile_maps.layers = [
            XYZLayerModel(href="nimbo_2023_06_1@kermap", composition="1"),
            XYZLayerModel(href="nimbo_2022_12_2@kermap", composition="2"),
            XYZLayerModel(href="nimbo_2023_06_3@kermap", composition="3"),
        ]

    def test_mapping_without_watermark(self):
        """
        Test without watermark
        """
        result = self.svc.get_compositions_mapping("FREE")
        for name in result.values():
            self.assertNotIn("WATERMARK", name.upper())

    def test_mapping_subscription_type(self):
        """
        Test with a subscription type
        """
        result = self.svc.get_compositions_mapping("FREE")
        self.assertIn(1, result)
        self.assertNotIn(2, result)

    def test_feature_none(self):
        """
        Test with a None feature
        """
        self.svc._authorized_features_cache["ALL"] = None
        with self.assertRaises(Exception):
            self.svc.get_compositions_mapping("FREE")

    def test_hrefs_allowed_none(self):
        """
        Test with a None hrefs list
        """
        self.svc._authorized_features_cache["ALL"] = self.FEATURES_ALL_WITH_NAMES
        self.svc._authorized_features_cache["FREE"] = None
        with self.assertRaises(Exception):
            self.svc.get_compositions_mapping("FREE")

    def test_mapping_without_duplication(self):
        """
        Test without duplication
        """
        self.svc.tile_maps.layers.append(
            XYZLayerModel(href="nimbo_2023_06_1@kermap", composition="1")
        )
        result = self.svc.get_compositions_mapping("FREE")
        self.assertEqual(len(result), len(set(result.keys())))


if __name__ == "__main__":
    unittest.main(verbosity=2)
