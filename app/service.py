from models import Aggregator
from exceptions import ProfileNotFoundError, ServiceNotAvailable
import github_api

def get_profile_statistics(github_profile, bitbucket_profile):
    try:
        github_repos = github_api.get(github_profile)
    except HTTPException as e:
        if e.response.status_code is 404:
            github_profile_not_found = True
        else:
            github_not_available = True
    try:
        bitbucket_repos = bitbucket_api.get(bitbucket_profile)
    except HTTPException as e:
        if e.response.status_code is 404:
            bitbucket_profile_not_found = True
        else:
            bitbucket_not_available = True
    if github_profile_not_found is True or bitbucket_profile_not_found is True:
        raise ProfileNotFoundError(github_profile_not_found, bitbucket_profile_not_found)
    if github_not_available is True or bitbucket_not_available is True:
        raise ServiceNotAvailable(github_not_available, bitbucket_not_available)
    aggregator = Aggregator()
    repos = github_repos + bitbucket_repos
    for repo in repos:
        aggregator.add(repo)
    return aggregator.asdict()
