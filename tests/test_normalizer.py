import unittest
import normalizer

class NormalizerTests(unittest.TestCase):
    def test_transliteration(self):
        filename = "Привет"
        expectedname = "Privet"

        normalized_name = normalizer.normalize(filename)

        self.assertEqual(expectedname, normalized_name)

    def test_name_whis_dots(self):

        name_whis_dots = "sdasd.qwe.."
        expected_name = "sdasd_qwe__"

        normalized_name = normalizer.normalize(name_whis_dots)

        self.assertEqual(expected_name, normalized_name)

    def test_empty_name(self):
        name = ""
        expected_name = ""

        normalized_name = normalizer.normalize(name)

        self.assertEqual(expected_name, normalized_name)

    def test_name_whis_unknown_simbol(self):
        name = "$%#@!&?()"
        expected_name = "_________"

        normalized_name = normalizer.normalize(name)

        self.assertEqual(expected_name, normalized_name)