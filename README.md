[![CircleCI](https://img.shields.io/circleci/project/github/jasonwalsh/ansible-role-telegraf/master.svg?style=flat-square)](https://circleci.com/gh/jasonwalsh/ansible-role-telegraf/tree/master) [![Ansible Quality Score](https://img.shields.io/ansible/quality/40537.svg?style=flat-square)](https://galaxy.ansible.com/jasonwalsh/telegraf) [![Ansible Role](https://img.shields.io/ansible/role/d/40537.svg?style=flat-square)](https://galaxy.ansible.com/jasonwalsh/telegraf)

> Ansible role for installing [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)

## Contents

- [Introduction](#introduction)
- [Install](#install)
- [Usage](#usage)
  - [Custom Telegraf Configuration](#custom-telegraf-configuration)
- [Platforms](#platforms)
- [Testing](#testing)
- [License](#license)

## Introduction

This repository contains an [Ansible](https://www.ansible.com/) role for installing and configuring [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/), an open source server agent to help collect metrics from stacks, sensors, and systems.

While similar roles exist, the purpose of this role is to be compatible with various platforms and architectures. Telegraf is cross-compiled and tested for different [platforms](https://github.com/influxdata/telegraf/releases/latest).

Refer to the [Platforms](#platforms) section of the README to view a table of platforms and architectures supported by this role.

## Install

This role is installable via [Ansible Galaxy](https://galaxy.ansible.com/) or git:

    $ ansible-galaxy install jasonwalsh.telegraf

    $ git clone git@github.com:jasonwalsh/ansible-role-telegraf.git roles/telegraf

## Usage

After installing the role, include it in an Ansible [playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#using-roles):

```yaml
---

- hosts: all
  roles:
    - jasonwalsh.telegraf
```

### Custom Telegraf Configuration

By default, this role uses the Telegraf configuration defined in the official [repository](https://github.com/influxdata/telegraf/blob/master/etc/telegraf.conf) and exists in the [`files`](files) subdirectory.

To use a custom configuration file, create a `telegraf_conf` variable with the absolute or relative path to the configuration file.

```yaml
---

# roles/x/vars/main.yml

telegraf_conf: ~/telegraf.conf
```

## Platforms

| Distribution | Architectures |
|:------------:|:-------------:|
| CentOS 7 | `x86_64` |
| Ubuntu 14.04 | `x86_64` |
| Ubuntu 16.04 | `x86_64` |

## Testing

This repository uses [Ansible Molecule](https://molecule.readthedocs.io/en/stable/) for testing the role. To install Molecule via [pip](https://packaging.python.org/key_projects/#pip), invoke the following command:

    $ pip install molecule

After installing Molecule, invoke the following command to run the entire test suite:

    $ molecule test

## License

MIT License
