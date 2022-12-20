from smat import API, Site


def test_get_content_with_string():
    client = API()
    content = client.get_content(term="bitcoin", site="4chan", limit=1)
    assert content is not {}


def test_get_content_with_enum():
    client = API()
    content = client.get_content(term="bitcoin", site=Site.FOURCHAN, limit=1)
    assert content is not {}


def test_get_content_with_invalid_site():
    client = API()
    content = client.get_content(term="bitcoin", site="invalid", limit=1)
    assert not content


def test_get_time_series_with_string():
    client = API()
    content = client.get_time_series(term="bitcoin", site="4chan")
    assert content is not {}


def test_get_time_series_with_enum():
    client = API()
    content = client.get_time_series(term="bitcoin", site=Site.FOURCHAN)
    assert content is not {}


def test_get_time_series_with_invalid_site():
    client = API()
    content = client.get_time_series(term="bitcoin", site="invalid")
    assert not content


def test_get_activity_with_string():
    client = API()
    content = client.get_activity(term="bitcoin", site="4chan")
    assert content is not {}


def test_get_activity_with_enum():
    client = API()
    content = client.get_activity(term="bitcoin", site=Site.FOURCHAN)
    assert content is not {}


def test_get_activity_with_invalid_site():
    client = API()
    content = client.get_activity(term="bitcoin", site="invalid")
    assert not content
