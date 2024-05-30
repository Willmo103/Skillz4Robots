# test_reddit_skills.py
import unittest
from skillz.reddit.reddit_skills import (
    search_for_a_subreddit,
    scrape_subreddit,
    search_subreddit_by_keyword,
)


class TestRedditSkills(unittest.TestCase):

    def test_search_for_a_subreddit(self):
        result = search_for_a_subreddit("python")
        self.assertIsNotNone(result, "Expected search_for_a_subreddit to return a non-None result")
        self.assertGreater(len(result), 0, "Expected non-empty result from search_for_a_subreddit")
        self.assertEqual(result[0]["display_name"], "Python", "Expected display name to be 'Python'")
        self.assertNotEqual(result[0]["title"], "", "Expected non-empty title")
        self.assertGreater(result[0]["subscribers"], 0, "Expected subscribers to be greater than 0")

    def test_scrape_subreddit(self):
        result = scrape_subreddit("python")
        self.assertIsNotNone(result, "Expected scrape_subreddit to return a non-None result")
        self.assertGreater(len(result), 0, "Expected non-empty result from scrape_subreddit")
        self.assertNotEqual(result[0]["title"], "", "Expected non-empty title")
        self.assertGreater(result[0]["score"], 0, "Expected score to be greater than 0")

    def test_search_subreddit_by_keyword(self):
        result = search_subreddit_by_keyword("python", "reddit")
        self.assertIsNotNone(result, "Expected search_subreddit_by_keyword to return a non-None result")
        self.assertGreater(len(result), 0, "Expected non-empty result from search_subreddit_by_keyword")
        self.assertNotEqual(result[0]["title"], "", "Expected non-empty title")
        self.assertGreater(result[0]["score"], 0, "Expected score to be greater than 0")


if __name__ == '__main__':
    unittest.main()
