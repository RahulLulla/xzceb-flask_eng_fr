import sys
import os
import unittest

directory = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(directory)
parent = os.path.dirname(parent)
sys.path.append(parent)

from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslations(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_null_english_to_french(self):
        self.assertEqual(englishToFrench(None),'')

    def test_null_french_to_english(self):
        self.assertEqual(frenchToEnglish(None),'')

if __name__ == '__main__':
    unittest.main()