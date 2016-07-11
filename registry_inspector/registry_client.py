from __future__ import print_function
import requests
import sys


class RegistryClient(object):
    def __init__(self, registry):
        self.registry = registry

    def _call_registry(self, method, path):
        return requests.request(method, self.registry + path, verify=False)

    def get_catalog(self):
        return self._call_registry('GET', '/v2/_catalog/').json()

    def get_tags(self, name):
        return self._call_registry('GET', '/v2/%s/tags/list' % (name,)).json()

    def get_manifest(self, name, tag):
        return self._call_registry(
            'GET', '/v2/%s/manifests/%s' %
            (name, tag,)).json()

    def get_digest_length(self, name, digest):
        r = self._call_registry('HEAD', '/v2/%s/blobs/%s' % (name, digest,))
        return r.headers['Content-Length']

    def log(self, *args):
        print(*args, file=sys.stderr)