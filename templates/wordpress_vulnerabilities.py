# {{ ansible_managed }}

import subprocess
import sys, os
import httplib
import ssl
import json
from checks import AgentCheck

class WordpressCheck(AgentCheck):
    def check(self, instance):
        ssl._create_default_https_context = ssl._create_unverified_context

        path = instance['path'];

        os.chdir(path)
        wp_version = subprocess.check_output(["wp", "core", 'version']).strip().replace(".", "")

        conn = httplib.HTTPSConnection("wpvulndb.com")
        headers = {
            "User-agent": "Datadog Wordpress Vulnerabilities check"
        }
        conn.request("GET","/api/v2/wordpresses/" + wp_version, None, headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        json_data = json.loads(data)

        vulnerability_count = len(json_data.values()[0]['vulnerabilities'])

        self.gauge('wordpress.core.vulnerabilities', vulnerability_count)
