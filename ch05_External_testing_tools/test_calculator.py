#######################Task 01 ####################################

import unittest
from calculator import Calculator

class myCalulator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
   
    def test_myCalculator(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4,result)
        
    def test_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add,'two','three')

if __name__ == '__main__':
    unittest.main()