from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    
    def test_add_numbers(self):
        
        """Test where two numbers are added together"""
        self.assertEqual(add(3,11), 14)

    def test_subtract_numbers(self):
        """Test subtracted numbers"""
        self.assertEqual(subtract(3,11), -8)