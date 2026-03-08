import unittest

from RuxmingText import Validate16Char, sample, test as package_test
from RuxmingText.Convert_Char_v1a import (
    Obtain16Char,
    hexStr_to_str,
    str_to_hexStr,
)


class ConvertCharTests(unittest.TestCase):
    def test_hex_string_round_trip_for_multibyte_character(self):
        hex_value = str_to_hexStr("开")
        self.assertEqual(hex_value, "e5bc80")
        self.assertEqual(hexStr_to_str(hex_value), "开")

    def test_obtain16char_extracts_encoded_bytes(self):
        text = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1=82abcdef"
        self.assertEqual(Obtain16Char(text, "="), "E68891E698AFE8AFB7E6B182")

    def test_validate16char_ignores_trailing_incomplete_sequence(self):
        text = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1"
        valid_hex = Validate16Char(text, "=")
        self.assertEqual(valid_hex, "E68891E698AFE8AFB7")
        self.assertEqual(hexStr_to_str(valid_hex), "我是请")

    def test_validate16char_returns_empty_for_no_matches(self):
        self.assertEqual(Validate16Char("plain ascii", "="), "")

    def test_sample_data_and_public_package_exports(self):
        self.assertEqual(sample(0), "i am request,\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82")
        self.assertEqual(sample(6), "开")
        self.assertIn("Nunst", package_test())
        self.assertEqual(Validate16Char("=E6=88", "="), "")


if __name__ == "__main__":
    unittest.main()
