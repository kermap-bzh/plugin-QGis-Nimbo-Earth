.. NimboEarth documentation master file, created by
   sphinx-quickstart on Sun Feb 12 17:11:03 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NimboEarth's documentation!
============================================

Contents:
Concepts
Running Nimbo Earth

.. toctree::
   :maxdepth: 2

.. index::Concepts
Concepts
==================
Nimbo Earth provide you access to Nimbo tile map services. 
From it you can add natural, infrared, vegetation (NDVI) or radar raster layers.

# Open the plugin from within QGis
# Login or use your api key
# Select a map to add
# Add it to your project

Running Nimbo Earth
===========================
You can open the plugin from the icon in toolbar or from the Web menu
When you open plugin a dockwidget appears on the right side of QGis.
The first window you will see has text fields.
Either you connect using your nimbo account email and password
or you can directly paste your api key.

Once your login or api key validation succeed, you will access to the second panel.
In this panel you will choose a layer to import.
You have two choices :
- you can select composition, year and month from the comboboxes
- you can directly select the layer from the list (you can only select one layer at a time)

Remember that adding a layer will consume geocredits from your nimbo account
you can consult your geocredits balance from your dashboard on https://maps.nimbo.earth/myNimbo/dashboard
(if you are logged in).

Indices and tables
==================

* :ref:`search`

