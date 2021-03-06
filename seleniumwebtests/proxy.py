# -*- coding: utf-8 -*-

import browsermobproxy

class Proxy(browsermobproxy.Client):
    """
    Extends browsermobproxy.Client class
    """

    def new_har(self, name, options=None):
        """
        This sets a new HAR to be recorded

        :param name: A reference for the HAR. Defaults to None
        :param options: A dictionary that will be passed to BrowserMob Proxy \
                with specific keywords. Keywords are: \
                captureHeaders - Boolean, capture headers. Defaults to True \
                captureContent - Boolean, capture content bodies. Defaults to True \
                captureBinaryContent - Boolean, capture binary content. Defaults to False
        """
        options = options
        if not options:
            options = {"captureHeaders": True, "captureContent": True}
        super(Proxy, self).new_har(name, options)

    def test_match(self, url, criterions=[], har=None):
        """
        Returns True if a request with given url and matching given criterions has been captured.

        :param url: URL substring the request URL has to contain
        :param criterions: List of criterions dicionaries the request has to match. Each dictionary has two items:
            "key" - dot separated path to the value in the HAR JSON we want to test. , i.e. "response.status", "request.headers" etc.
                See the examples/har.json to see how one single request is stored in the HAR format.
            "value" - desired value. Can be string, integer or dict.
        :param har: HAR JSON to search through. If not provided the proxy is asked to provide the actual one.
        """
        return len(self.get_matches(url, criterions, har)) != 0

    def get_matches(self, url, criterions=[], har=None):
        """
        Returns list of matching requests.

        :param url: URL substring the request URL has to contain
        :param criterions: List of criterions dicionaries the request has to match. Each dictionary has two items:
            "key" - dot separated path to the value in the HAR JSON we want to test. , i.e. "response.status", "request.headers" etc.
                See the examples/har.json to see how one single request is stored in the HAR format.
            "value" - desired value. Can be string, integer or dict.
        :param har: HAR JSON to search through. If not provided the proxy is asked to provide the actual one.
        """
        url_matches = self._filter_entries_by_url(url, har)
        if len(criterions):
            matches = []
            criterions_length = len(criterions)-1
            for entry in url_matches:
                for i, criterion in enumerate(criterions):
                    try:
                        if not self._test_entry_to_criterion_match(entry, criterion):
                            break
                    except:
                        return []
                else:
                    if i == criterions_length:
                        # all criterions match -> passed
                        matches.append(entry)
                    continue
        else:
            return url_matches
        return matches

    def _filter_entries_by_url(self, url, har):
        """
        Filters all captured requests by passed URL substring

        :param url: URL substring the request URL has to contain
        """
        if not har:
            har = self.har
        
        matches = []
        for entry in har["log"]["entries"]:
            if url in entry["request"]["url"]:
                matches.append(entry)
        return matches

    def _test_entry_to_criterion_match(self, entry, criterion):
        """
        Tests single entry in HAR file whether it match given single criterion

        :param entry: Request entry from HAR JSON
        :param criterion:
        """
        parent = self._get_parent_node(entry, criterion["key"])
        parent_type = type(parent)
        if parent_type == list:
            unicriterions = { k.decode('utf8', "replace"): v.decode('utf8', "replace") for k, v in criterion["value"].items() }
            for item in parent:
                if set(unicriterions.items()) <= set({ k: v for k, v in item.items() }.items()):
                    return True
            return False
        if parent_type == str or int:
            return str(parent) == str(criterion["value"])

    def _get_parent_node(self, entry, key):
        """
        Finds item in single request entry matching given criterion key
        """
        parent = entry
        keys = key.split(".")
        for k in keys:
            try:
                parent = parent[k]
            except:
                raise Exception("key \"" + key + "\" was not found in HAR file")
        return parent
