# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/guillaume/Documents/Depot/plugin-QGis-Nimbo-Earth/nimbo_earth_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NimboEarthDockWidgetBase(object):
    def setupUi(self, NimboEarthDockWidgetBase):
        NimboEarthDockWidgetBase.setObjectName("NimboEarthDockWidgetBase")
        NimboEarthDockWidgetBase.resize(500, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NimboEarthDockWidgetBase.sizePolicy().hasHeightForWidth())
        NimboEarthDockWidgetBase.setSizePolicy(sizePolicy)
        NimboEarthDockWidgetBase.setMinimumSize(QtCore.QSize(500, 850))
        NimboEarthDockWidgetBase.setMaximumSize(QtCore.QSize(500, 850))
        NimboEarthDockWidgetBase.setStyleSheet("")
        NimboEarthDockWidgetBase.setWindowTitle("")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setMaximumSize(QtCore.QSize(500, 831))
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_kn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_kn.setObjectName("horizontalLayout_kn")
        spacerItem = QtWidgets.QSpacerItem(30, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_kn.addItem(spacerItem)
        self.nimbo_icon_label = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nimbo_icon_label.sizePolicy().hasHeightForWidth())
        self.nimbo_icon_label.setSizePolicy(sizePolicy)
        self.nimbo_icon_label.setMinimumSize(QtCore.QSize(20, 20))
        self.nimbo_icon_label.setMaximumSize(QtCore.QSize(45, 45))
        self.nimbo_icon_label.setText("")
        self.nimbo_icon_label.setPixmap(QtGui.QPixmap("/home/guillaume/Documents/Depot/plugin-QGis-Nimbo-Earth/assets/nimboIcon.png"))
        self.nimbo_icon_label.setScaledContents(True)
        self.nimbo_icon_label.setObjectName("nimbo_icon_label")
        self.horizontalLayout_kn.addWidget(self.nimbo_icon_label)
        self.nimbo_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.nimbo_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nimbo_label.setTextFormat(QtCore.Qt.RichText)
        self.nimbo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nimbo_label.setOpenExternalLinks(True)
        self.nimbo_label.setObjectName("nimbo_label")
        self.horizontalLayout_kn.addWidget(self.nimbo_label)
        spacerItem1 = QtWidgets.QSpacerItem(30, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_kn.addItem(spacerItem1)
        self.kermap_icon_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.kermap_icon_label.setMinimumSize(QtCore.QSize(20, 20))
        self.kermap_icon_label.setMaximumSize(QtCore.QSize(40, 40))
        self.kermap_icon_label.setText("")
        self.kermap_icon_label.setPixmap(QtGui.QPixmap("/home/guillaume/Documents/Depot/plugin-QGis-Nimbo-Earth/kermapLogo.png"))
        self.kermap_icon_label.setScaledContents(True)
        self.kermap_icon_label.setObjectName("kermap_icon_label")
        self.horizontalLayout_kn.addWidget(self.kermap_icon_label)
        self.kermap_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.kermap_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kermap_label.setTextFormat(QtCore.Qt.RichText)
        self.kermap_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kermap_label.setOpenExternalLinks(True)
        self.kermap_label.setObjectName("kermap_label")
        self.horizontalLayout_kn.addWidget(self.kermap_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_kn.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_kn, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.geocredit_label = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geocredit_label.sizePolicy().hasHeightForWidth())
        self.geocredit_label.setSizePolicy(sizePolicy)
        self.geocredit_label.setText("")
        self.geocredit_label.setTextFormat(QtCore.Qt.AutoText)
        self.geocredit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.geocredit_label.setObjectName("geocredit_label")
        self.horizontalLayout_5.addWidget(self.geocredit_label)
        self.gc_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.gc_label.setObjectName("gc_label")
        self.horizontalLayout_5.addWidget(self.gc_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 728))
        self.tabWidget.setObjectName("tabWidget")
        self.key_tab = QtWidgets.QWidget()
        self.key_tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.key_tab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.key_tab.setObjectName("key_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.key_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 30, -1, 20)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.key_tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 411, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.key_label = QtWidgets.QLabel(self.layoutWidget)
        self.key_label.setObjectName("key_label")
        self.horizontalLayout_6.addWidget(self.key_label)
        self.free_pButton = QtWidgets.QPushButton(self.layoutWidget)
        self.free_pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.free_pButton.setObjectName("free_pButton")
        self.horizontalLayout_6.addWidget(self.free_pButton)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.key_tab)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 160))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.key_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.key_label_2.setGeometry(QtCore.QRect(10, 40, 431, 51))
        self.key_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_2.setObjectName("key_label_2")
        self.subscribe_pButton = QtWidgets.QPushButton(self.groupBox_5)
        self.subscribe_pButton.setGeometry(QtCore.QRect(20, 110, 200, 25))
        self.subscribe_pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subscribe_pButton.setObjectName("subscribe_pButton")
        self.pricing_pButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pricing_pButton.setGeometry(QtCore.QRect(240, 110, 200, 25))
        self.pricing_pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pricing_pButton.setObjectName("pricing_pButton")
        self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.key_tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 320))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 330))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.email_label = QtWidgets.QLabel(self.groupBox)
        self.email_label.setGeometry(QtCore.QRect(19, 55, 101, 20))
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(self.groupBox)
        self.password_label.setGeometry(QtCore.QRect(19, 90, 101, 20))
        self.password_label.setObjectName("password_label")
        self.email_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.email_lineEdit.setGeometry(QtCore.QRect(120, 50, 301, 25))
        self.email_lineEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(120, 90, 271, 25))
        self.password_lineEdit.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_pButton = QtWidgets.QPushButton(self.groupBox)
        self.login_pButton.setGeometry(QtCore.QRect(120, 130, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_pButton.sizePolicy().hasHeightForWidth())
        self.login_pButton.setSizePolicy(sizePolicy)
        self.login_pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_pButton.setObjectName("login_pButton")
        self.eye_pButton = QtWidgets.QPushButton(self.groupBox)
        self.eye_pButton.setGeometry(QtCore.QRect(400, 90, 26, 24))
        self.eye_pButton.setText("")
        self.eye_pButton.setObjectName("eye_pButton")
        self.key_input_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.key_input_lineEdit.setGeometry(QtCore.QRect(120, 230, 301, 25))
        self.key_input_lineEdit.setObjectName("key_input_lineEdit")
        self.key_pButton = QtWidgets.QPushButton(self.groupBox)
        self.key_pButton.setGeometry(QtCore.QRect(120, 270, 200, 25))
        self.key_pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.key_pButton.setObjectName("key_pButton")
        self.key_label_3 = QtWidgets.QLabel(self.groupBox)
        self.key_label_3.setGeometry(QtCore.QRect(19, 230, 101, 20))
        self.key_label_3.setObjectName("key_label_3")
        self.key_label_4 = QtWidgets.QLabel(self.groupBox)
        self.key_label_4.setGeometry(QtCore.QRect(120, 170, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.key_label_4.setFont(font)
        self.key_label_4.setScaledContents(False)
        self.key_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_4.setObjectName("key_label_4")
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.key_tab, "")
        self.tms_tab = QtWidgets.QWidget()
        self.tms_tab.setObjectName("tms_tab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tms_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 451, 661))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.tms_tab_vLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.tms_tab_vLayout.setContentsMargins(0, 0, 0, 0)
        self.tms_tab_vLayout.setObjectName("tms_tab_vLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 409, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.composition_label = QtWidgets.QLabel(self.layoutWidget1)
        self.composition_label.setEnabled(True)
        self.composition_label.setTextFormat(QtCore.Qt.AutoText)
        self.composition_label.setScaledContents(False)
        self.composition_label.setWordWrap(True)
        self.composition_label.setObjectName("composition_label")
        self.horizontalLayout_2.addWidget(self.composition_label)
        self.composition_selector_comBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.composition_selector_comBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.composition_selector_comBox.setPlaceholderText("")
        self.composition_selector_comBox.setObjectName("composition_selector_comBox")
        self.horizontalLayout_2.addWidget(self.composition_selector_comBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 90, 409, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.year_selector_label = QtWidgets.QLabel(self.layoutWidget2)
        self.year_selector_label.setWordWrap(True)
        self.year_selector_label.setObjectName("year_selector_label")
        self.horizontalLayout_4.addWidget(self.year_selector_label)
        self.year_comBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.year_comBox.setObjectName("year_comBox")
        self.horizontalLayout_4.addWidget(self.year_comBox)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 150, 409, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.month_selector_label = QtWidgets.QLabel(self.layoutWidget3)
        self.month_selector_label.setWordWrap(True)
        self.month_selector_label.setObjectName("month_selector_label")
        self.horizontalLayout_3.addWidget(self.month_selector_label)
        self.month_comBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.month_comBox.setObjectName("month_comBox")
        self.horizontalLayout_3.addWidget(self.month_comBox)
        self.add_map_cbox_pButton = QtWidgets.QPushButton(self.groupBox_2)
        self.add_map_cbox_pButton.setGeometry(QtCore.QRect(110, 200, 200, 25))
        self.add_map_cbox_pButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.add_map_cbox_pButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.add_map_cbox_pButton.setObjectName("add_map_cbox_pButton")
        self.tms_tab_vLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.layer_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.layer_listWidget.setGeometry(QtCore.QRect(20, 30, 400, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.layer_listWidget.setFont(font)
        self.layer_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layer_listWidget.setObjectName("layer_listWidget")
        self.add_map_list_pButton = QtWidgets.QPushButton(self.groupBox_4)
        self.add_map_list_pButton.setGeometry(QtCore.QRect(110, 160, 200, 25))
        self.add_map_list_pButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.add_map_list_pButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.add_map_list_pButton.setObjectName("add_map_list_pButton")
        self.tms_tab_vLayout.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 170))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 170))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.pricing_link = QtWidgets.QPushButton(self.groupBox_6)
        self.pricing_link.setGeometry(QtCore.QRect(110, 130, 200, 25))
        self.pricing_link.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pricing_link.setSizeIncrement(QtCore.QSize(0, 0))
        self.pricing_link.setObjectName("pricing_link")
        self.key_label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.key_label_6.setGeometry(QtCore.QRect(10, 30, 431, 91))
        self.key_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_6.setObjectName("key_label_6")
        self.tms_tab_vLayout.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tms_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        NimboEarthDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(NimboEarthDockWidgetBase)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(NimboEarthDockWidgetBase)

    def retranslateUi(self, NimboEarthDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        self.nimbo_label.setText(_translate("NimboEarthDockWidgetBase", "<html><head/><body><p><a href=\"https://nimbo.earth/\"><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">About Nimbo</span></a></p></body></html>"))
        self.kermap_label.setText(_translate("NimboEarthDockWidgetBase", "<html><head/><body><p><a href=\"https://kermap.com/en/our-story/\"><span style=\" font-weight:600; color:#ffffff;\">About Kermap</span></a></p></body></html>"))
        self.title_label.setText(_translate("NimboEarthDockWidgetBase", "Welcome to Nimbo Earth Basemaps TMS"))
        self.gc_label.setText(_translate("NimboEarthDockWidgetBase", "remaining Geocredits"))
        self.groupBox_3.setTitle(_translate("NimboEarthDockWidgetBase", "Try our cloud-free basemap service"))
        self.key_label.setText(_translate("NimboEarthDockWidgetBase", "Try now with"))
        self.free_pButton.setText(_translate("NimboEarthDockWidgetBase", "June 2023 | Natural"))
        self.groupBox_5.setTitle(_translate("NimboEarthDockWidgetBase", "Create you account for free access to all Nimbo Services"))
        self.key_label_2.setText(_translate("NimboEarthDockWidgetBase", "<html><head/><body><p><span>Create your Nimbo account to load any <br>monthly basemap into QGIS, from Oct. 2019 to present. <br>4 color layers available.</span></p></body></html>"))
        self.subscribe_pButton.setText(_translate("NimboEarthDockWidgetBase", "Sign up to Nimbo"))
        self.pricing_pButton.setText(_translate("NimboEarthDockWidgetBase", "See offers"))
        self.groupBox.setTitle(_translate("NimboEarthDockWidgetBase", "Already have a Nimbo account?"))
        self.email_label.setText(_translate("NimboEarthDockWidgetBase", "E-mail"))
        self.password_label.setText(_translate("NimboEarthDockWidgetBase", "Password"))
        self.login_pButton.setText(_translate("NimboEarthDockWidgetBase", "Login"))
        self.key_pButton.setText(_translate("NimboEarthDockWidgetBase", "Validate your key"))
        self.key_label_3.setText(_translate("NimboEarthDockWidgetBase", "API key"))
        self.key_label_4.setText(_translate("NimboEarthDockWidgetBase", "Or"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.key_tab), _translate("NimboEarthDockWidgetBase", "API key validation"))
        self.groupBox_2.setTitle(_translate("NimboEarthDockWidgetBase", "Select your parameters"))
        self.composition_label.setText(_translate("NimboEarthDockWidgetBase", "Select composition"))
        self.year_selector_label.setText(_translate("NimboEarthDockWidgetBase", "Choose a year"))
        self.month_selector_label.setText(_translate("NimboEarthDockWidgetBase", "Choose a month"))
        self.add_map_cbox_pButton.setText(_translate("NimboEarthDockWidgetBase", "Add layer"))
        self.groupBox_4.setTitle(_translate("NimboEarthDockWidgetBase", "Or choose from the list"))
        self.add_map_list_pButton.setText(_translate("NimboEarthDockWidgetBase", "Add layer"))
        self.groupBox_6.setTitle(_translate("NimboEarthDockWidgetBase", "Professional plans"))
        self.pricing_link.setText(_translate("NimboEarthDockWidgetBase", "Discover offers"))
        self.key_label_6.setText(_translate("NimboEarthDockWidgetBase", "<html><head/><body><p>Learn more about Nimbo geocredit plans and advanced <br>geospatial applications: basemap integration, multispectral <br> basemap download or real-time monitoring.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tms_tab), _translate("NimboEarthDockWidgetBase", "Layer selector"))
