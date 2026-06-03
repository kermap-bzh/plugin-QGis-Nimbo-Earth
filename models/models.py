"""
Module containing models
"""

class XYZLayerModel:
    """A class for creating a layer from the xml file"""
    def __init__(self, title='', srs='', profile='', href='', year='', month='', composition='') -> None:
        self.title = title
        self.srs = srs
        self.profile = profile
        self.href = href
        self.year = year
        self.month = month
        self.composition = composition


class TileMapsModel:
    """A class for creating a list of layers from the xml file"""
    def __init__(self, layers=[]):
        self.layers = layers


class NimboUser:
    """A class for creating a Nimbo user"""
    def __init__(self, email='', password='', access_token='', api_key='', subscription_type=None):
        self.email = email
        self.password = password
        self.access = access_token
        self.api_key = api_key
        self.subscription_type = subscription_type
