class Repo:

    def __init__(self, is_original, watcher_count, language, topics):
        self.is_original = is_original
        self.watcher_count = watcher_count
        self.language = language
        self.topics = topics


class Aggregator:

    def __init__(self):
        self.count = 0
        self.original_count = 0
        self.forked_count = 0
        self.watcher_count = 0
        self.languages = {}
        self.topics = {}

    def add(self, repo):
        self.count += 1
        if repo.is_original is not None:
            if repo.is_original:
                self.original_count += 1
            else:
                self.forked_count += 1
        self.watcher_count += repo.watcher_count
        self.languages[repo.language] = self.languages.get(repo.language, 0) + 1
        for topic in repo.topics:
            self.topics[topic] = self.topics.get(topic, 0) + 1

    def asdict(self):
        return {
            "public_repo_count": self.original_count + self.forked_count,
            "public_repo_breakdown": {
                "original_repo_count": self.original_count,
                "forked_repo_count": self.forked_count
            },
            "watcher_count": self.watcher_count,
            "languages": to_json_formatted_dict_list(self.languages),
            "topics": to_json_formatted_dict_list(self.topics)
        }


def to_json_formatted_dict_list(dict):
    return [{"name": key, "count": value} for (key, value) in dict.items()]
