from app.models import Repo
import app.fetch

from flask import current_app

BASE_URL = "https://api.bitbucket.org"


def get(bitbucket_profile):
    """
    Returns a list of Repo objects for a bitbucket profile
    :param bitbucket_profile: string
    :return: Repo[]
    """

    url = f"{BASE_URL}/2.0/repositories/{bitbucket_profile}"
    repos_json = get_repos(url)
    return [build_repo(json) for json in repos_json if json.get("is_private") is False]


def get_repos(url):
    response = app.fetch.get(url, {})
    current_app.logger.info(f"Calling url: {url}")
    response.raise_for_status()
    response_json = response.json()
    next_url = response_json.get("next")
    if not next_url:
        return response_json.get("values")
    else:
        return response_json.get("values") + get_repos(next_url)


def build_repo(json):
    watchers_url = json.get("links", {}).get("watchers", {}).get("href", {})
    watchers_count = get_watchers_count(watchers_url)
    language = json.get("language")
    return Repo(None, watchers_count, language, [])


def get_watchers_count(watchers_url):
    if not watchers_url:
        return 0
    response = app.fetch.get(watchers_url, {})
    if not response.ok:
        return 0
    return response.json().get("size", 0)
