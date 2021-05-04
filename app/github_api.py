from app.models import Repo
import app.fetch
import re
from flask import current_app


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
    return [build_repo(json) for json in repos_json if not json.get("private")]

def get_repos(url):
    """
    Call github url accounting for pagination and return all repos as dict representation in a list
    :param url: string
    :return: dict[]
    """
    response = app.fetch.get(url, BASE_HEADERS)
    current_app.logger.info(f"Called github url: {url}")
    response.raise_for_status()
    next_link = response.headers.get("Link")
    if not next_link:
        return response.json()
    else:
        try:
            next_url = re.search('<(.+?)(>; rel="next")', next_link).group(1)
            return response.json() + get_repos(next_url)
        except AttributeError as e:
            return response.json()


def build_repo(json):
    """
    Build repo class from returned json
    :param json: dict - json from github
    :return: Repo
    """
    is_original = not json.get("fork")
    watchers_count = json.get("watchers_count")
    language = json.get("language")
    topics = json.get("topics", [])
    return Repo(is_original, watchers_count, language, topics)
