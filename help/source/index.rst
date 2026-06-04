.. NimboEarth documentation master file, created by
   sphinx-quickstart on Sun Feb 12 17:11:03 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Nimbo Earth Basemaps TMS Documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Concepts
========

Nimbo Earth Basemaps is an innovative Earth observation service providing cloud-free, homogenous mosaics of the world's entire landmass as captured by satellite imagery. Mosaics are updated every single month and served in WMS/WMTS formats.

The plugin provides users with 4 distinct data layers every month:

* **Natural colors (RGB)** at 10m resolution.
* **Infrared (NIR)** at 10m resolution.
* **NDVI (vegetation health index)** at 10m resolution.
* **HD Natural colors (RGB)** at 2.5m resolution (AI enhanced through in-house algorithms).

Data Availability Timeline
--------------------------

**For all 10m resolution layers (RGB, NIR, NDVI):**

* **From October 2019 to present**: Europe, Northern Africa, and Middle East.
* **From March 2022 to present**: All of the above + the USA.
* **From February 2023 to present**: Full Global coverage.

**For the HD Natural colors (RGB) at 2.5m:**

* **From May 2025 to present**: Full Global coverage.

Running Nimbo Earth
===================

You can launch the plugin either by clicking its icon in the QGIS toolbar or via the **Web** menu. 
Once opened, the **Welcome to Nimbo Earth Basemaps TMS** dock widget will appear on the right side of the QGIS interface.

1. API Key Validation Tab
-------------------------

When you first open the plugin, you will interact with the **API key validation** tab. This interface is split into three main sections:

* **Try our cloud-free basemap service**: Allows you to instantly test the service by loading a free sample layer (**June 2023 | RGB**) without requiring an account.
* **Create your account**: If you don't have an account yet, use the **Sign up to Nimbo** or **See offers** buttons to register and access the monthly tiers.
* **Already have a Nimbo account?**: Authenticate directly using one of two methods:

  - Enter your **E-mail** and **Password** then click **Login** to securely fetch your token.
  - Paste your personal **API key** extracted from your online dashboard, then click **Validate your key**.

2. Layer Selector Tab
---------------------

Once authenticated, the **Layer selector** tab becomes active and accessible.

* **Geocredits Tracking**: The top bar displays your remaining balance of **Geocredits**. 
* **Parameters Filtering**: You can easily filter the extensive catalog of monthly basemaps using three dropdown comboboxes:

  - **Compositions**: Filter by image type (All, RGB, NDVI, Infrared, etc.).
  - **Months**: Filter by a specific month.
  - **Years**: Filter by a specific year.

* **Adding Layers**: Select a layer from the reverse-chronological list view and click the **Add layer** button to load it into your current QGIS project workspace.

.. important::
   Please note that each layer you enable (i.e., check/select) will consume credits from your balance. 
   You can monitor your detailed data consumption from your personal online dashboard.

Professional Plans
------------------

For advanced users requiring custom integrations, multispectral basemap downloads, or real-time environmental monitoring, use the **Discover offers** button under the **Professional plans** section to learn more about advanced geospatial options.

Support & Links
===============

* Need assistance? Click the **Support** link in the top-right corner of the window to access our support form.
* Learn more about our ecosystem using the **About Nimbo** and **About Kermap** links located at the bottom of the plugin window.

Indices and Tables
==================

* :ref:`search`