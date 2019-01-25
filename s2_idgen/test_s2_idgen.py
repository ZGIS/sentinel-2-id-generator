import unittest

from s2_idgen import s2_idgen

class TestGenerator(unittest.TestCase):
    
    def setUp(self):
        self.s2_id = s2_idgen.Generator(granule_id = 'T33UVP', acquisition_time = '20170105T013442')
    
    def test_getid(self):
        self.assertEqual(self.s2_id.getID(), 't33uvp-2017-005-01-6')


class TestGenerator2(unittest.TestCase):
        
    def test_checkgranuleid(self):
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = None, acquisition_time = '20170105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = '33UVVP', acquisition_time = '20170105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UVVP', acquisition_time = '20170105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'TXXXXX', acquisition_time = '20170105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UV1', acquisition_time = '20170105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 6, acquisition_time = '20170105T013442')

    def test_checktimestamp(self):
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UVP', acquisition_time = None)        
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UVP', acquisition_time = '20140105T013442')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UVP', acquisition_time = 'somedummystuffhere')
        self.assertRaises(Exception,s2_idgen.Generator,granule_id = 'T33UVP', acquisition_time = 1244)

if __name__ == '__main__':
    unittest.main()