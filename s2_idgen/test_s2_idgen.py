import unittest

import s2_idgen

class TestGenerator(unittest.TestCase):
    
    def setUp(self):
        self.s2_id = s2_idgen.Generator(granule_id = 'T33UVP', acquisition_time = '20170105T013442')
    
    def test_getid(self):
        self.assertEqual(self.s2_id.getID(), 't33uvp-2017-005-01-6')
        
if __name__ == '__main__':
    unittest.main()