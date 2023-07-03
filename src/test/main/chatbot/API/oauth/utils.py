from collections import namedtuple
from urllib.parse import urlencode, urlunparse


def build_url(scheme, netloc, url, params=None, query=None, fragment=None):
    if query is None:
        query = {}
    if params is None:
        params = {}
    Components = namedtuple(
        typename='Components',
        field_names=['scheme', 'netloc', 'url', 'params', 'query', 'fragment']
    )

    return urlunparse(
        Components(
            scheme=scheme,
            netloc=netloc,
            url=url,
            params=params,
            query=urlencode(query),
            fragment=fragment
        )
    )
