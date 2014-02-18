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

    def find_in_har(self, url, criterions={}):
        """
        This will get the captured HAR and try to find a result matching given options.
        Returns True if a match has been found. False otherwise.

        :param url: URL or substring of URL of the request we are searching for
        :param criterions: A dictionary of criterions the result has to match. \
                Keys in the dictionary represent key names in the HAR its value we want \
                to test. Using dots in the key name it is possible to access data stores \
                depper in the HAR. Example: \
                criterions={ \
                    "response.status": 200, \
                    "response.headers": { \
                        "name": "Connection", "value": "closed"} \
                    } \
        See examples/har.json to see the structure of HAR result.
        """
        har = self.har
        for entry in har["log"]["entries"]:
            if url in entry["request"]["url"]:
                for key in criterions:
                    # get the node in the JSON in which we will be searching
                    parent = entry
                    keys = key.split(".")
                    for k in keys:
                        try:
                            parent = parent[k]
                        except:
                            raise Exception("key \"" + key + "\" was not found in HAR file")

                    # if the parent is a list, search through all items
                    if isinstance(parent, list):
                        found = False
                        for item in parent:
                            unicriterions = { k.decode('utf8'): v.decode('utf8') for k, v in criterions[key].items() }
                            uniitems = { k.decode('utf8'): v.decode('utf8') for k, v in item.items() }
                            if unicriterions == uniitems:
                                found = True

                        if not found:
                            return False

                    # if is integer or string, simply check if its match the desired value
                    if isinstance(parent, (int, str)):
                        if parent != criterions[key]:
                            return False
                return True
        return False
