import unittest
from skillz.web_scraping.web_scraping_skills import get_webpage, duckduckgo_keyword_search


class TestWebScrapingSkills(unittest.TestCase):

    def test_get_page_format(self):
        _input = "https://notes.willmo.dev/"
        result = get_webpage(_input)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

    def test_duckduckgo_keyword_search(self):
        _input = "python"
        result = duckduckgo_keyword_search('python coding')
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0, "Expected non-empty result")
        self.assertEqual(len(result), 5, "Expected 5 results")
        self.assertNotEqual(result[0]['title'], "", "Expected non-empty result")
        self.assertNotEqual(result[0]['href'], "", "Expected non-empty result")
        self.assertNotEqual(result[0]['body'], "", "Expected non-empty result")


if __name__ == '__main__':
    unittest.main()
