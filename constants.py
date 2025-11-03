"""
Module containing constants
"""
from aenum import Enum


# base service URLs

ABOUT_URL = 'https://nimbo.earth'

SERVICE_URL = 'https://prod-data.nimbo.earth/mapcache/tms/1.0.0?kermap_token='

USER_URL = 'https://prod-admin.nimbo.earth'

# base for layer name for import
LAYER_NAME = 'Nimbo_Earth-'

# user feature reference constants
GEOCREDITS_REF = 'geocredits'

# enum for image composition
class ImageComposition(Enum):
    """Available compositions for combobox selection"""
    _init_ = "value string"

    NATURAL = 1, "RGB"
    INFRARED = 2, "NIR"
    VEGETATION = 3, "NDVI"
    RADAR = 4, "RADAR"
    HD = 5, "HD"

    def describe(self):
        return self.name.capitalize()

    def __str__(self):
        return self.string
