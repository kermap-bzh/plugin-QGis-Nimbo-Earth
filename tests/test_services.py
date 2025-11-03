# -*- coding: utf-8 -*-
"""
Tests pour la logique métier des services
"""
import unittest
import sys
import os

# Ajouter le répertoire parent au path pour permettre l'import
plugin_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, plugin_dir)

# Ajouter le répertoire parent du plugin pour les imports relatifs
parent_dir = os.path.dirname(plugin_dir)
sys.path.insert(0, parent_dir)

# Initialiser les dépendances externes avant d'importer les services
from services.imports import ensure_import
ensure_import('xmltodict')
ensure_import('requests')
ensure_import('aenum')

# Import en tant que module du plugin
plugin_name = os.path.basename(plugin_dir)
services_module = __import__(f"{plugin_name}.services.services", fromlist=['Services'])
Services = services_module.Services


class TestServicesGetTiles(unittest.TestCase):
    """Tests pour la logique des services"""
    
    def test_get_tile_maps_PRO(self):
        """Test que les utilisateurs PRO ont accès à tous les services"""
        xml_file_path = os.path.join(os.path.dirname(__file__), "data", "data-pro.xml")
        
        # Lire le contenu du fichier XML
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        tile_maps = Services().get_tile_maps(xml_content, 'PRO')
        # Vérifier que le nombre de services est correct et qu'il ne contient pas la mention watermark dans le href
        self.assertEqual(len(tile_maps.layers), 13)
        for layer in tile_maps.layers:
            self.assertNotIn('watermark', layer.href)
            
            
    def test_get_tile_maps_PRO_HD(self):
        """Test que les utilisateurs PRO HD ont accès à tous les services et la HD"""
        xml_file_path = os.path.join(os.path.dirname(__file__), "data", "data-pro.xml")
        
        # Lire le contenu du fichier XML
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        tile_maps = Services().get_tile_maps(xml_content, 'PRO HD')
        # Vérifier que le nombre de services est correct et qu'il contient la mention watermark dans le href
        self.assertEqual(len(tile_maps.layers), 13)
        for layer in tile_maps.layers:
            self.assertNotIn('watermark', layer.href)
        
        
    def test_get_tile_maps_FREE(self):
        """Test que les utilisateurs FREE n'ont accès qu'aux services watermark"""
        xml_file_path = os.path.join(os.path.dirname(__file__), "data", "data-free.xml")
        
        # Lire le contenu du fichier XML
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        tile_maps = Services().get_tile_maps(xml_content, 'FREE')
        # Vérifier que le nombre de services est correct et qu'il contient la mention watermark dans le href
        self.assertEqual(len(tile_maps.layers), 12)
        for layer in tile_maps.layers:
            self.assertIn('watermark', layer.href)
        
        
if __name__ == '__main__':
    unittest.main()
