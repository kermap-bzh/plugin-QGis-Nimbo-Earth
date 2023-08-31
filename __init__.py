# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NimboEarth
                                 A QGIS plugin
 This plugins allows you to access all Nimbo earth tile map services.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-10-18
        copyright            : (C) 2023 by Kermap
        email                : contact@nimbo.earth
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


    
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NimboEarth class from file NimboEarth.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .services.imports import ensure_import
    ensure_import('xmltodict')
    ensure_import('requests')
    ensure_import('aenum')
    
    #
    from .nimbo_earth import NimboEarth
    return NimboEarth(iface)
