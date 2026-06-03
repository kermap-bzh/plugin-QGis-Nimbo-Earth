#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import unittest

def run_nimbo_tests():
    # Définition du répertoire racine du plugin
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # On s'assure que le dossier parent du plugin est dans le path pour les imports relatifs
    plugin_parent = os.path.dirname(current_dir)
    if plugin_parent not in sys.path:
        sys.path.insert(0, plugin_parent)

    print("🚀 Démarrage des tests dynamiques Nimbo Earth...")
    print("-" * 50)

    loader = unittest.TestLoader()
    # On cherche les tests dans le dossier /tests
    suite = loader.discover(os.path.join(current_dir, 'tests'), pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Sortie propre pour les scripts d'automatisation (CI/CD)
    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == '__main__':
    run_nimbo_tests()