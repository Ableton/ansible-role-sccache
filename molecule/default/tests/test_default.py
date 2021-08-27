import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_sccache_installed(host):
    sccache_bin = host.file("/usr/local/bin/sccache")

    assert sccache_bin.is_file
    assert sccache_bin.mode == 0o0755
