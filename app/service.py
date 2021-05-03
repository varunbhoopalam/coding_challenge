from models import Aggregator
from exceptions import ProfileNotFoundError

def get_profile_statistics(github_profile, bitbucket_profile):
    github_repos = github_api.get(github_profile)
    bitbucket_repos = bitbucket_api.get(bitbucket_profile)
    if github_profile is None or bitbucket_profile is None:
        raise ProfileNotFoundError(github_repos, bitbucket_repos)
    aggregator = Aggregator()
    repos = github_repos + bitbucket_repos
    for repo in repos:
        aggregator.add(repo)
    return aggregator.asdict()
