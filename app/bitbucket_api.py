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
    return [build_repo(json) for json in repos_json if not json.get("is_private")]


def get_repos(url):
    """
    Call bitbucket url accounting for pagination and return all repos as dict representation in a list
    :param url: string
    :return: dict[]
    """
    response = app.fetch.get(url, {})
    current_app.logger.info(f"Called bitbucket url: {url}")
    response.raise_for_status()
    response_json = response.json()
    next_url = response_json.get("next")
    if not next_url:
        return response_json.get("values")
    else:
        return response_json.get("values") + get_repos(next_url)


def build_repo(json):
    """
    Build repo class from returned json
    :param json: dict - json from bitbucket
    :return: Repo
    """
    watchers_url = json.get("links", {}).get("watchers", {}).get("href", {})
    watchers_count = get_watchers_count(watchers_url)
    language = json.get("language")
    return Repo(None, watchers_count, language, [])


def get_watchers_count(watchers_url):
    """
    Given a watchers_url, this will extract the total number of watchers
    :param watchers_url: string
    :return: int
    """
    if not watchers_url:
        return 0
    response = app.fetch.get(watchers_url, {})
    current_app.logger.info(f"Called bitbucket watchers url: {watchers_url}")
    if not response.ok:
        return 0
    return response.json().get("size", 0)
