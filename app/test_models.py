import unittest

from models import Repo, Aggregator

class RepoTests(unittest.TestCase):

    def test_init(self):
        is_original = True
        watcher_count = 10
        language = "Python"
        topics = ["Flask"]
        repo = Repo(is_original, watcher_count, language, topics)
        self.assertEqual(repo.is_original, is_original)
        self.assertEqual(repo.watcher_count, watcher_count)
        self.assertEqual(repo.language, language)
        self.assertEqual(repo.topics, topics)

class AggregatorTests(unittest.TestCase):

    def test_add_original(self):
        aggregator = Aggregator()
        aggregator.add(Repo(True, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.original_count, 1)
        self.assertEqual(aggregator.forked_count, 0)

    def test_add_forked(self):
        aggregator = Aggregator()
        aggregator.add(Repo(False, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.original_count, 0)
        self.assertEqual(aggregator.forked_count, 1)

    def test_add_languages(self):
        aggregator = Aggregator()
        aggregator.add(Repo(False, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.languages, {"Python":1})
        aggregator.add(Repo(False, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.languages, {"Python":2})
        aggregator.add(Repo(False, 10, "Java", ["Flask"]))
        self.assertEqual(aggregator.languages, {"Python":2, "Java":1})

    def test_add_topics(self):
        aggregator = Aggregator()
        aggregator.add(Repo(False, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.topics, {"Flask":1})
        aggregator.add(Repo(False, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.topics, {"Flask":2})
        aggregator.add(Repo(False, 10, "Python", ["Flask", "Numpy"]))
        self.assertEqual(aggregator.topics, {"Flask":3, "Numpy":1})

    def test_asdict(self):
        aggregator = Aggregator()
        expected = {
            "public_repo_count": 0,
            "public_repo_breakdown": {
                "original_repo_count": 0,
                "forked_repo_count": 0
            },
            "watcher_count": 0,
            "languages": [],
            "topics": []
        }
        self.assertEqual(aggregator.asdict(), expected)
        expected2 = {
            "public_repo_count": 1,
            "public_repo_breakdown": {
                "original_repo_count": 1,
                "forked_repo_count": 0
            },
            "watcher_count": 10,
            "languages": [{"name": "Python", "count":1}],
            "topics": [{"name": "Flask", "count": 1}]
        }
        aggregator.add(Repo(True, 10, "Python", ["Flask"]))
        self.assertEqual(aggregator.asdict(), expected2)

if __name__ == '__main__':
    unittest.main()
