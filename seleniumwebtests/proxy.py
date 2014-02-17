# -*- coding: utf-8 -*-

import browsermobproxy

class Proxy(browsermobproxy.Client):

    def new_har(self, name, options=None):
        options = options
        if not options:
            options = {"captureHeaders": True, "captureContent": True}
        super(Proxy, self).new_har(name, options)

    def find_in_har(self, url, props={}):
        har = self.har
        for entry in har["log"]["entries"]:
            if url in entry["request"]["url"]:
                for key in props:
                    parent = entry
                    keys = key.split(".")
                    for k in keys:
                        try:
                            parent = parent[k]
                        except:
                            raise Exception("key \"" + key + "\" was not found in HAR file")


                    if isinstance(parent, list):
                        found = False
                        for item in parent:
                            uniprops = { k.decode('utf8'): v.decode('utf8') for k, v in props[key].items() }
                            uniitems = { k.decode('utf8'): v.decode('utf8') for k, v in item.items() }
                            if uniprops == uniitems:
                                found = True

                        if not found:
                            return False

                    if isinstance(parent, (int, str)):
                        if parent != props[key]:
                            return False
                return True
        return False
