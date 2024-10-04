import unittest
class TestATM(unittest.TestCase):
    
    def test_valid_pin(self):
        self.assertEqual(validate_pin('1234'), 'Access Granted')
    
    def test_invalid_pin(self):
        self.assertEqual(validate_pin('0000'), 'Access Denied')
def validate_pin(pin):
    valid_pin = '1234'
    if pin == valid_pin:
        return 'Access Granted'
    else:
        return 'Access Denied'
if __name__ == '__main__':
    unittest.main()
