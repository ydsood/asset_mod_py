import unittest
import asset_mod

class TestSuite(unittest.TestCase):
    
    def test_assetmod_updateGuids(self):
        self.assertEqual( asset_mod.updateGuids('371492ec-7009-43c8-b800-7ba7fe0a2d7e'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'Converts lowercase to uppercase')
        self.assertEqual( asset_mod.updateGuids('371492EC-7009-43C8-B800-7BA7FE0A2D7E'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'does not change upper case')
        self.assertEqual( asset_mod.updateGuids('Test this string'), 'Test this string', 'Does not modify non-guids' )
    
    def test_assetmod_updateTimestampDataType(self):
        self.assertEqual( asset_mod.updateTimestampDataType('TrxHdrEffectiveDateHigh datetime'), 'TrxHdrEffectiveDateHigh date', 'Replaces datetime with date')
        self.assertEqual( asset_mod.updateTimestampDataType('TrxHdrEffectiveDateHigh DATETIME'), 'TrxHdrEffectiveDateHigh date', 'Case insensitive')
        self.assertEqual( asset_mod.updateTimestampDataType('TrxHdrEffectiveDateHigh'), 'TrxHdrEffectiveDateHigh', 'No-Op if not found')
    
    def test_assetmod_updateTimestampData(self):
        self.assertEqual( asset_mod.updateTimestampData('Converts AM time 1/1/1900 7:00:00 AM'), 'Converts AM time 1900-1-1 7:00:00', 'Converts AM time')
        self.assertEqual( asset_mod.updateTimestampData('Converts AM time 1/1/1900 12:00:00 AM'), 'Converts AM time 1900-1-1 00:00:00', 'Converts AM time')
        self.assertEqual( asset_mod.updateTimestampData('Converts AM time 1/1/1900 12:35:35 AM'), 'Converts AM time 1900-1-1 00:35:35', 'Converts AM time')
        self.assertEqual( asset_mod.updateTimestampData('Converts PM time 9/25/2017 7:20:50 PM'), 'Converts PM time 2017-9-25 19:20:50', 'Converts PM time ')
        self.assertEqual( asset_mod.updateTimestampData('Converts PM time 9/25/2017 12:20:50 PM'), 'Converts PM time 2017-9-25 12:20:50', 'Converts PM time ')



if __name__ == "__main__":
    unittest.main()