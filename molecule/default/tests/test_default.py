import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_telegraf_is_installed(host):
    assert host.package('telegraf').is_installed


def test_telegraf_is_running(host):
    assert host.service('telegraf').is_enabled
    assert host.service('telegraf').is_running


def test_telegraf_conf_exists(host):
    assert host.file('/etc/telegraf/telegraf.conf').exists
