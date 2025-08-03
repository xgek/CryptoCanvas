# test_cryptocanvas.py
"""
Tests for CryptoCanvas module.
"""

import unittest
from cryptocanvas import CryptoCanvas

class TestCryptoCanvas(unittest.TestCase):
    """Test cases for CryptoCanvas class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoCanvas()
        self.assertIsInstance(instance, CryptoCanvas)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoCanvas()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
