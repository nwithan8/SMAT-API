from typing import Union
from urllib.parse import urlencode

import requests

import smat.api_logging as logs


def make_session():
    return requests.Session()


def make_url(base: str, endpoint: str, suffix: str = "") -> str:
    if base.endswith("/"):
        base = base[:-1]
    if endpoint.startswith("/"):
        endpoint = endpoint[1:]
    return f"{base}/{endpoint}{suffix}"


def encode_params(params: dict = None) -> str:
    if params:
        return urlencode(params)
    return ""


def get(url: str,
        params: dict = None,
        headers: dict = None,
        timeout: int = 2,
        log: bool = False,
        session: requests.Session = None,
        **kwargs) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        if session:
            res = session.get(url=url, headers=headers, timeout=timeout)
        else:
            res = requests.get(url=url, headers=headers, timeout=timeout)
        if log:
            logs.log(message=f"GET {url}", level='info')
            logs.log(message=f"Response: {res}", level=("error" if not res else 'info'))
        return res
    except requests.exceptions.Timeout:
        return None

def request(method,
            url: str,
            params: dict = None,
            headers: dict = None,
            data: dict = None,
            files: dict = None,
            timeout: int = 2,
            log: bool = False,
            session: requests.Session = None) -> requests.Response:
    return globals()[method](**locals())


def request_json(method,
                 url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 files: dict = None,
                 timeout: int = 2,
                 log: bool = False,
                 session: requests.Session = None) -> dict:
    try:
        res = globals()[method](**locals())
        if res:
            return res.json()
        return {}
    except:
        raise Exception(f"{method} is an invalid method")
