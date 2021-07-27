Ansible role ableton.sccache
============================

This role installs [sccache][sccache] on the given Ansible host and configures it for a
given user.

Requirements
------------

Ansible >= 2.10 is required. This role supports package-based installation on the
following OS types:

- Debian Linux (via the `apt` module)
- macOS (via the `homebrew` module)
- Windows (via the `win_chocolatey` module)

For all other platforms, a source-based installation will be performed. On such systems
where package-based installation is *not* available, the software can be installed from a
binary download. In such cases, please refer to the [sccache releases][sccache-releases]
to see supported platforms.

Role Variables
--------------

The following variables influence how `sccache` is installed on the host:

- `sccache_config_options`: Dictionary of dictionaries describing key/value options to
  write to the `sccache` configuration file.
- `sccache_download_url`: Where to download prebuilt `sccache` binaries from.
- `sccache_install_from_binary`: When `true`, install `sccache` from a prebuilt binary
  instead of installing from a package manager.
- `sccache_user`: User to configure sccache for.
- `sccache_version`: Version and SHA256 checksums of sccache to install. Only applies when
  installing from a binary package.

See the [`defaults/main.yml`](defaults/main.yml) file for full documentation on required
and optional role variables.

Example Playbook
----------------

```yaml
---
- name: Install sccache on hosts
  hosts: "all"
  vars:
    sccache_config_options:
      cache:
        redis.url: "redis://your-redis-server-here"
    sccache_version:
      version: "0.2.15"
      shas:
        Darwin: 908e939ea3513b52af03878753a58e7c09898991905b1ae3c137bb8f10fa1be2

  pre_tasks:
    - name: Force sccache to be installed from a binary on macOS
      set_fact:
        sccache_install_from_binary: true
      when: ansible_os_family == "Darwin"

  roles:
    - ableton.sccache
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@mst-ableton](https://github.com/mst-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[sccache]: https://github.com/mozilla/sccache
[sccache-releases]: https://github.com/mozilla/sccache/releases
