#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re

class HARExplorer(object):


    def __init__(self, har):
        self._har = har["log"]["entries"]


    def test_match(self, url, criterions=None):
        return len(self.get_matches(url, criterions)) != 0


    def get_matches(self, url, criterions=None):
        url_matches = self._filter_entries_by_url(url)
        if criterions:
            matches = []
            for entry in url_matches:
                for key in criterions:
                    if not self._test_entry_to_criterion_match(entry, key, criterions[key]):
                        break
                else:
                    continue
                break
        else:
            return url_matches
        return matches


    def _filter_entries_by_url(self, url):
        pattern = re.compile(url)
        matches = []
        for entry in self._har:
            if pattern.search(entry["request"]["url"]):
                matches.append(entry)
        return matches


    def _test_entry_to_criterion_match(self, entry, criterion_key, criterion_value):
        parent = self._get_parent_node(entry, criterion_key)
        if isinstance(parent, list):
            return True
        if isinstance(parent, str)
            return parent == criterion_value:


    def _get_parent_node(self, entry, criterion):
        # get the node in the JSON in which we will be searching
        parent = entry
        keys = key.split(".")
        for k in keys:
            try:
                parent = parent[k]
            except:
                raise Exception("key \"" + key + "\" was not found in HAR file")
        return parent




f = open("../examples/har.json")
har = json.loads(f.read())

test = HARExplorer(har)
print test.test_match("zbozi.(dev|cdddz|test)")


def find_in_har(url, criterions={}):

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
                        break

                # if it is integer or string, simply check if it is match the desired value
                if isinstance(parent, (int, str)):
                    if parent != criterions[key]:
                        break
            else:
                return True
    return False
