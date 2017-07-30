import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_squid_file(host):
    squid = host.file("/etc/squid/squid.conf")
    assert squid.contains("0.0.0.0/3306")
    assert squid.user == "root"
    assert squid.group == "squid"
    assert squid.mode == 0o640


def test_system_type(SystemInfo):
    '''Check OS type'''
    type = SystemInfo.type
    assert type == 'linux'


def test_squid_is_installed(host):
    squid = host.package("squid")
    assert squid.is_installed


def test_squid_running_and_enabled(host):
    squid = host.service("squid")
    assert squid.is_running
    assert squid.is_enabled