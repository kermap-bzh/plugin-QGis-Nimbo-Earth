# -*- coding: utf-8 -*-
#
# NimboEarth documentation build configuration file, created by
# sphinx-quickstart on Sun Feb 12 17:11:03 2012.

import sys
import os

# -- General configuration -----------------------------------------------------

# Core Sphinx extensions
extensions = ["sphinx.ext.todo", "sphinx.ext.imgmath", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project (Aligned with metadata.txt)
project = "Nimbo's Earth Basemaps"
copyright = "2026, Kermap"
author = "Kermap"

# Version management aligned with the v2 plugin branch specifications
version = "2.0"
release = "2.0"

# List of patterns, relative to source directory, to ignore when looking for source files
exclude_patterns = ["build", "Thumbs.db", ".DS_Store"]

pygments_style = "sphinx"

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "default"

html_static_path = ["_static"]

# Output file base name for HTML help builder
htmlhelp_basename = "NimboEarthDoc"

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    (
        "index",
        "NimboEarth.tex",
        "Nimbo's Earth Basemaps Documentation",
        "Kermap",
        "manual",
    ),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ("index", "nimboearth", "Nimbo's Earth Basemaps Documentation", ["Kermap"], 1)
]
