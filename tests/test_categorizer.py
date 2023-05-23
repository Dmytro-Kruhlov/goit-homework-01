import unittest
import categorizer


class CategorizerTests(unittest.TestCase):
    def test_video_category(self):
        filename = "qwe.avi"
        expected_category = "video"

        actual_category = categorizer.categorize(filename)

        self.assertEqual(
            actual_category,
            expected_category
        )

    def test_image_category(self):
        filename = "asd.jpeg"
        expected_category = "images"

        actual_category = categorizer.categorize(filename)

        self.assertEqual(
            actual_category,
            expected_category
        )


    def test_audio_category(self):
        filename = "qwe.ogg"
        expected_category = "audio"

        actual_category = categorizer.categorize(filename)

        self.assertEqual(actual_category, expected_category)


    def test_documents_category(self):
        filename = "qwer.xlsx"    
        expected_category = "documents"

        actual_category = categorizer.categorize(filename)

        self.assertEqual(actual_category, expected_category)


    def test_archive_category(self):
        filename = "asdf.gz"
        expected_category = "archives"

        actual_category = categorizer.categorize(filename)

        self.assertEqual(actual_category, expected_category)


    def test_categorize_files(self):
        data = [
            "123.ppa", "5.tar", "1.jpeg", "qwe.avi", "asdf.mp3", "zxc.pptx", "sdf.qwe", "213.zxc"
        ]
        expected_categories = {
                "to_move": {
                "images": ["1.jpeg"],
                "archives": ["5.tar"],
                "audio": ["asdf.mp3"],
                "documents": ["zxc.pptx"],
                "video": ["qwe.avi"]
            },
            "all_extensions": {"jpeg", "tar", "avi", "mp3", "pptx"},
            "unknown_extensions": {"ppa", "qwe", "zxc"}
        }

        actual_categories = categorizer.categorize_files(data)

        self.assertDictEqual(
            expected_categories,
            actual_categories
        )