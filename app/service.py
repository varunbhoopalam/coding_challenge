from app.models import Aggregator
from app.exceptions import ProfileNotFoundError, ServiceNotAvailable
import app.github_api
import app.bitbucket_api
from requests.exceptions import HTTPError


def get_profile_statistics(github_profile, bitbucket_profile):
    github_repos = []
    bitbucket_repos = []
    github_profile_not_found = False
    bitbucket_profile_not_found = False
    github_not_available = False
    bitbucket_not_available = False

    try:
        github_repos = app.github_api.get(github_profile)
    except HTTPError as e:
        if e.response.status_code == 404:
            github_profile_not_found = True
        else:
            github_not_available = True
    try:
        bitbucket_repos = app.bitbucket_api.get(bitbucket_profile)
    except HTTPError as e:
        if e.response.status_code == 404:
            bitbucket_profile_not_found = True
        else:
            bitbucket_not_available = True
    if github_profile_not_found or bitbucket_profile_not_found:
        raise ProfileNotFoundError("not found", {
            "code": 404,
            "github_profile": {
                "name": github_profile,
                "found": not github_profile_not_found
            },
            "bitbucket_profile": {
                "name": bitbucket_profile,
                "found": not bitbucket_profile_not_found
            }
        })
    if github_not_available or bitbucket_not_available:
        raise ServiceNotAvailable("service unavailable", {
            "code": 500,
            "github_not_available": github_not_available,
            "bitbucket_not_available": bitbucket_not_available
        })
    aggregator = Aggregator()
    repos = github_repos + bitbucket_repos
    for repo in repos:
        aggregator.add(repo)
    return aggregator.asdict()
