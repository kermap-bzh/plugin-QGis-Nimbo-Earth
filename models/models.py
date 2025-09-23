from qgis.PyQt.QtCore import QAbstractItemModel, QAbstractListModel, Qt


class XYZLayerModel(QAbstractItemModel):
    """A class for creating a layer from the xml file"""
    def __init__(self, title='', srs='', profile='', href='', year='', month='', composition='') -> None:
        self.title = title
        self.srs = srs
        self.profile = profile
        self.href = href
        self.year = year
        self.month = month
        self.composition = composition

        def __str__(self):
            return self.href


class TileMapsModel(QAbstractListModel):
    """a class listing all the XYZLayers"""
    def __init__(self, *args, layers=None, **kwargs):
        super(TileMapsModel, self).__init__(*args, **kwargs)
        self.layers = layers or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            month, year, composition = self.layers[index.row()]
            return year, month, composition

    def rowCount(self, index) -> int:
        return len(self.layers)


class NimboUser(QAbstractItemModel):
    """a class to get a nimbo user"""
    def __init__(self, email='', password='', api_key='', subscription_type=None):
        self.email = email
        self.password = password
        self.api_key = api_key
        # 'FREE' or 'PRO' (from user-feature-me endpoint)
        self.subscription_type = subscription_type
