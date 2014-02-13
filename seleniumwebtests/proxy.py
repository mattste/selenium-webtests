# -*- coding: utf-8 -*-

import os
import subprocess
import requests
import json
import seleniumwebtests as swt

class Proxy():

    def __init__(self):

        # check if the provided start file exists
        self.server_start_file = swt.config.PROXY_START_SCRIPT
        if not os.path.isfile(self.server_start_file):
            raise Exception("Browsermob-proxy bin file ({0}) not found".format(self.server_start_file))

        # Start server
        stdout = open(os.devnull, 'w')
        command = [self.server_start_file, "--port={0}".format(swt.config.PROXY_PORT)]
        self.process = subprocess.Popen(command, stdout=stdout, stderr=subprocess.STDOUT)

    def stop(self):
        """
        Stop server
        """
        self.process.kill()

    def startClient(self, url):
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.post("{0}/proxy".format(url), urlencode(''))
        jcontent = json.loads(response.content)
        self.port = jcontent['port']
        url_parts = url.split(":")
        self.proxy = url_parts[1][2:] + ":" + str(self.port)
