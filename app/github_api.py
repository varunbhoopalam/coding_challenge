from models import Repo
import fetch
import re

BASE_URL = "https://api.github.com"
BASE_HEADERS = {
    "Accept": "application/vnd.github.mercy-preview+json"
}


def get(github_profile):
    """
    Returns a list of Repo objects for a github profile
    :param github_profile: string
    :return: Repo[]
    """

    url = f"{BASE_URL}/orgs/{github_profile}/repos"
    repos_json = get_repos(url)
    return [parse_repo(json) for json in repos_json if json.get("private") is False]

def get_repos(url):
    response = fetch.get(url, BASE_HEADERS)
    response.raise_for_status()  # Need to handle exceptions in service
    next_link = response.headers.get("Link")
    if not next_link:
        return response.json()
    else:
        try:
            next_url = re.search('<(.+?)(>; rel="next")', next_link).group(1)
            return response.json() + get_repos(next_url)
        except AttributeError as e:
            return response.json()


def parse_repo(json):
    is_original = not json.get("fork")
    watchers_count = json.get("watchers_count")
    language = json.get("language")
    topics = json.get("topics", [])
    return Repo(is_original, watchers_count, language, topics)
