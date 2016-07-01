from registry_inspector.registry_client import RegistryClient


def test_get_catalog():
    registry = 'http://localhost:5000'
    client = RegistryClient(registry)
    assert ('repositories' in client.get_catalog())


def test_get_tags():
    registry = 'http://localhost:5000'
    client = RegistryClient(registry)
    name = 'ubuntu'
    assert ('tags' in client.get_tags(name))


def test_get_manifests():
    registry = 'http://localhost:5000'
    client = RegistryClient(registry)
    name = 'ubuntu'
    tag = 'latest'
    assert ('fsLayers' in client.get_manifests(name, tag))
