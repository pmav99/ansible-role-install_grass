import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_grass_is_installed(host):
    grass = host.package("grass")
    assert grass.is_installed
    assert grass.version.startswith("7.")
