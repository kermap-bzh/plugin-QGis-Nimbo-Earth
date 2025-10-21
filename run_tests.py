#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exécuter les tests du plugin Nimbo Earth
Usage: python3 run_tests.py
"""
import sys
import os
import unittest

def discover_and_run_tests():
    """Découvre et exécute les tests avec unittest"""
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(plugin_dir, 'tests')
    
    # Ajouter le répertoire du plugin au PYTHONPATH
    if plugin_dir not in sys.path:
        sys.path.insert(0, plugin_dir)
    
    # Ajouter le répertoire parent pour permettre les imports relatifs
    parent_dir = os.path.dirname(plugin_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    print("🧪 Exécution des tests unitaires du plugin Nimbo Earth...")
    print("=" * 60)
    print(f"📁 Répertoire des tests: {tests_dir}")
    print(f"🐍 Python: {sys.version}")
    print("=" * 60)
    
    # Découverte automatique des tests
    loader = unittest.TestLoader()
    start_dir = tests_dir
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Exécution des tests
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)
    
    # Résumé
    print("\n" + "=" * 60)
    print(f"✅ Tests réussis: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Tests échoués: {len(result.failures)}")
    print(f"💥 Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n🔍 Échecs détaillés:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\n💥 Erreurs détaillées:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.split('Error:')[-1].strip()}")
    
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(discover_and_run_tests())
