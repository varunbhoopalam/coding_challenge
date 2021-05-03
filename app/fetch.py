import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def get(url):
    """
    Simply http request wrapper with retry logic implemented

    :param url: String to get from
    :return: requests response object
    """
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session.get(url)
