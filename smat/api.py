from typing import Union

import smat.api_requests as api_requests
import smat.utils as utils
from smat.models import *


def return_class(site: str, request_type: str):
    if request_type == 'content':
        if site == 'reddit':
            return RedditContent
        elif site == 'twitter':
            return TwitterContent
        elif site == '4chan':
            return FourChanContent
        elif site == '8kun':
            return EightKunContent
        elif site == 'gab':
            return GabContent
        elif site == 'parler':
            return ParlerContent
        elif site == 'thedonald':
            return TheDonaldContent
        elif site == 'telegram':
            return TelegramContent
        elif site == 'poal':
            return PoalContent
        else:
            raise Exception(f"{site} is not a valid site option for {request_type}")
    elif request_type == 'activity':
        if site == 'reddit':
            return RedditActivity
        elif site == 'twitter':
            return TwitterActivity
        elif site == '4chan':
            return FourChanActivity
        elif site == '8kun':
            return EightKunActivity
        elif site == 'gab':
            return GabActivity
        elif site == 'parler':
            return ParlerActivity
        elif site == 'thedonald':
            return TheDonaldActivity
        elif site == 'poal':
            return PoalActivity
        else:
            raise Exception(f"{site} is not a valid site option for {request_type}")
    elif request_type == 'timeseries':
        if site == 'reddit':
            return RedditTimeSeries
        elif site == 'twitter':
            return TwitterTimeSeries
        elif site == '4chan':
            return FourChanTimeSeries
        elif site == '8kun':
            return EightKunTimeSeries
        elif site == 'gab':
            return GabTimeSeries
        elif site == 'parler':
            return ParlerTimeSeries
        elif site == 'thedonald':
            return TheDonaldTimeSeries
        elif site == 'telegram':
            return TelegramTimeSeries
        elif site == 'poal':
            return PoalTimeSeries
        else:
            raise Exception(f"{site} is not a valid site option for {request_type}")
    else:
        raise Exception("Invalid request_type")


def parse_response(json: dict = None):
    if not json:
        return {}
    if 'detail' in json.keys():
        api_requests.logs.error(message="API returned an error about a bad request.")
        return {}
    return json


class API:
    base = "https://api.smat-app.com/"
    session = api_requests.make_session()
    _default_since = utils.string_to_datetime("2020-12-12T03:31:12.253311")
    _default_to = utils.string_to_datetime("2021-02-12T03:31:12.253311")

    def __init__(self, raw_json: bool = True, verbose: bool = False):
        self._raw = raw_json
        self._verbose = verbose

    def get_content(self, term: str, limit: int = 10, site: str = "reddit", since: utils.datetime = _default_since,
                    until: utils.datetime = _default_to, esquery: bool = False, raw_json: bool = False) -> Union[
        dict, object]:
        if not raw_json:
            raw_json = self._raw
        params = {
            'term': term,
            'site': site,
            'limit': limit,
            'since': utils.datetime_to_string(since),
            'until': utils.datetime_to_string(until),
            'esquery': esquery
        }
        utils.validate_dict(items=params)
        endpoint = api_requests.make_url(base=self.base, endpoint='content')
        json = api_requests.request_json(method='get', url=endpoint, params=params, session=self.session,
                                         log=self._verbose)
        json = parse_response(json)
        if raw_json:
            return json
        else:
            if not json:
                return None
            object_to_make = return_class(site=site, request_type="content")
            return object_to_make(**json)

    def get_time_series(self, term: str, interval: str = 'day', site: str = "reddit",
                        since: utils.datetime = _default_since, until: utils.datetime = _default_to,
                        change_point: bool = False, raw_json: bool = False) -> Union[dict, object]:
        if not raw_json:
            raw_json = self._raw
        params = {
            'term': term,
            'site': site,
            'interval': interval,
            'since': utils.datetime_to_string(since),
            'until': utils.datetime_to_string(until),
            'changepoint': change_point
        }
        utils.validate_dict(items=params)
        endpoint = api_requests.make_url(base=self.base, endpoint='content')
        json = api_requests.request_json(method='get', url=endpoint, params=params, session=self.session,
                                         log=self._verbose)
        json = parse_response(json)
        if raw_json:
            return json
        else:
            object_to_make = return_class(site=site, request_type="timeseries")
            return object_to_make(**json)

    def get_activity(self, term: str, site: str = "reddit", aggregate_by: str = None,
                     since: utils.datetime = _default_since, until: utils.datetime = _default_to,
                     raw_json: bool = False) -> Union[dict, object]:
        if not raw_json:
            raw_json = self._raw
        params = {
            'term': term,
            'site': site,
            'agg_by': aggregate_by,
            'since': utils.datetime_to_string(since),
            'until': utils.datetime_to_string(until)
        }
        utils.validate_dict(items=params)
        endpoint = api_requests.make_url(base=self.base, endpoint='activity')
        json = api_requests.request_json(method='get', url=endpoint, params=params, session=self.session, log=self._verbose)
        json = parse_response(json)
        if raw_json:
            return json
        else:
            object_to_make = return_class(site=site, request_type="activity")
            return object_to_make(**json)
