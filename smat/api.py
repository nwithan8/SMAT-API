from typing import Union

import objectrest

import smat.utils as utils
from smat.sites import Site


class API:
    _default_since = utils.string_to_datetime("2020-12-12T03:31:12.253311")
    _default_to = utils.string_to_datetime("2021-02-12T03:31:12.253311")

    def __init__(self, verbose: bool = False):
        self._requestor = objectrest.RequestHandler(
            base_url="https://api.smat-app.com/", log_requests=verbose
        )

    def get_content(
        self,
        term: str,
        site: Union[Site, str],
        limit: int = 10,
        since: utils.datetime = _default_since,
        until: utils.datetime = _default_to,
        esquery: bool = False,
    ) -> Union[dict, object]:
        if isinstance(site, Site):
            site = site.value
        params = {
            "term": term,
            "site": site,
            "limit": limit,
            "since": utils.datetime_to_string(since),
            "until": utils.datetime_to_string(until),
            "esquery": esquery,
        }
        utils.validate_dict(items=params)

        return self._requestor.get_json(url="content", params=params)

    def get_time_series(
        self,
        term: str,
        site: Union[Site, str],
        interval: str = "day",
        since: utils.datetime = _default_since,
        until: utils.datetime = _default_to,
        change_point: bool = False,
    ) -> Union[dict, object]:
        if isinstance(site, Site):
            site = site.value
        params = {
            "term": term,
            "site": site,
            "interval": interval,
            "since": utils.datetime_to_string(since),
            "until": utils.datetime_to_string(until),
            "changepoint": change_point,
        }
        utils.validate_dict(items=params)

        return self._requestor.get_json(url="timeseries", params=params)

    def get_activity(
        self,
        term: str,
        site: Union[Site, str],
        aggregate_by: str = None,
        since: utils.datetime = _default_since,
        until: utils.datetime = _default_to,
    ) -> Union[dict, object]:
        if isinstance(site, Site):
            site = site.value
        params = {
            "term": term,
            "site": site,
            "agg_by": aggregate_by,
            "since": utils.datetime_to_string(since),
            "until": utils.datetime_to_string(until),
        }
        utils.validate_dict(items=params)

        return self._requestor.get_json(url="activity", params=params)
