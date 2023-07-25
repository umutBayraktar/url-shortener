import hashlib

from django.test import TestCase
from shortener.utils import get_md5_hash
from shortener.exceptions import EmptyHashValueException, InvalidHashValueException

class UtilsTestCase(TestCase):

    def setUp(self) -> None:
        self.valid_str = "Hello, World!"
        self.valid_hash = hashlib.md5(self.valid_str.encode('utf-8')).hexdigest()

    def test_get_md5_hash_with_valid_str(self):
        hash_value = get_md5_hash(self.valid_str)
        self.assertEqual(hash_value, self.valid_hash[:10])
        self.assertEqual(len(hash_value), 10)

    def test_get_md5_hash_with_hash_size(self):
        hash_size = 5
        hash_value = get_md5_hash(self.valid_str, hash_size=hash_size)
        self.assertEqual(hash_value, self.valid_hash[:hash_size])
        self.assertEqual(len(hash_value), hash_size)

    def test_get_md5_hash_with_empty_str(self):
        # Test with an empty string
        empty_str = ""
        with self.assertRaises(EmptyHashValueException):
            get_md5_hash(empty_str)

    def test_get_md5_hash_with_invalid_value(self):
        # Test with an empty string
        empty_str = {"key":"value"}
        with self.assertRaises(InvalidHashValueException):
            get_md5_hash(empty_str)

    def test_get_md5_hash_with_nonascii_value(self):
        # Test with a non-ASCII string
        non_ascii_str = "Îñţérñåţîöñåļîžåţîờñ"
        expected_non_ascii_hash = "adfcfee9df"
        self.assertEqual(get_md5_hash(non_ascii_str), expected_non_ascii_hash)
