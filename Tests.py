import unittest
import asset_mod

class TestSuite(unittest.TestCase):
    
    def test_UpdateArtifacts_updateGuids(self):
        self.assertEqual( asset_mod.updateGuids('371492ec-7009-43c8-b800-7ba7fe0a2d7e'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'Converts lowercase to uppercase')
        self.assertEqual( asset_mod.updateGuids('371492EC-7009-43C8-B800-7BA7FE0A2D7E'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'does not change upper case')
        self.assertEqual( asset_mod.updateGuids('Test this string'), 'Test this string', 'Does not modify non-guids' )

if __name__ == "__main__":
    unittest.main()