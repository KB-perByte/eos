#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

##############################################
#                 WARNING                    #
##############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
##############################################

"""
The module file for eos_l2_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: eos_l2_interfaces
short_description: L2 interfaces resource module
description:
  This module provides declarative management of Layer-2 interface on Arista
  EOS devices.
version_added: 1.0.0
author: Nathaniel Case (@Qalthos)
notes:
  - Tested against Arista EOS 4.24.6F
  - This module works with connection C(network_cli).
    See U(https://docs.ansible.com/ansible/latest/network/user_guide/platform_eos.html)
options:
  config:
    description: A dictionary of Layer-2 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Full name of interface, e.g. Ethernet1.
        type: str
        required: true
      access:
        description:
          - Switchport mode access command to configure the interface as a layer 2 access.
        type: dict
        suboptions:
          vlan:
            description:
              - Configure given VLAN in access port. It's used as the access VLAN ID.
            type: int
      trunk:
        description:
          - Switchport mode trunk command to configure the interface as a Layer 2 trunk.
        type: dict
        suboptions:
          native_vlan:
            description:
              - Native VLAN to be configured in trunk port. It is used as the trunk
                native VLAN ID.
            type: int
          trunk_allowed_vlans:
            description:
              - List of allowed VLANs in a given trunk port. These are the only VLANs
                that will be configured on the trunk.
            type: list
            elements: str
      mode:
        description:
          - Mode in which interface needs to be configured.
          - Access mode is not shown in interface facts, so idempotency will not be
            maintained for switchport mode access and every time the output will come
            as changed=True.
        type: str
        choices:
          - access
          - trunk
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section ^interface).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - parsed
      - rendered
      - gathered
    default: merged
    description:
      - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Merge provided configuration with device configuration.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
        mode: trunk
        trunk:
          native_vlan: 10
      - name: Ethernet2
        mode: access
        access:
          vlan: 30
    state: merged

# Task Output
# -----------
#
# before:
# - name: Ethernet1
# - name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - switchport mode trunk
# - switchport trunk native vlan 10
# - interface Ethernet2
# - switchport mode access
# - switchport access vlan 30
# after:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using replaced

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet1
      mode: trunk
      trunk:
        native_vlan: 20
        trunk_allowed_vlans: 5-10, 15
    state: replaced

# Task Output
# -----------
#
# before:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - switchport trunk native vlan 20
# - switchport trunk allowed vlan 10,15,5,6,7,8,9
# after:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 20
#     trunk_allowed_vlans:
#     - 5-10
#     - '15'
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 20
#    switchport trunk allowed vlan 5-10,15
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using overridden

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 20
#    switchport trunk allowed vlan 5-10,15
#    switchport mode trunk
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Override device configuration of all L2 interfaces on device with provided
    configuration.
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet2
      mode: access
      access:
        vlan: 30
    state: overridden

# Task Output
# -----------
#
# before:
# - mode: trunk
#   name: Ethernet1
#   trunk:
#     native_vlan: 20
#     trunk_allowed_vlans:
#     - 5-10
#     - '15'
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet1
# - no switchport mode
# - no switchport trunk allowed vlan
# - no switchport trunk native vlan
# - interface Ethernet2
# - switchport mode access
# after:
# - name: Ethernet1
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# Using deleted

# Before state:
# -------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
#    switchport access vlan 30
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

- name: Delete EOS L2 interfaces as in given arguments.
  arista.eos.eos_l2_interfaces:
    config:
      - name: Ethernet1
      - name: Ethernet2
    state: deleted

# Task Output
# -----------
#
# before:
# - name: Ethernet1
# - access:
#     vlan: 30
#   name: Ethernet2
# - name: Management1
# commands:
# - interface Ethernet2
# - no switchport access vlan
# after:
# - name: Ethernet1
# - name: Ethernet2
# - name: Management1

# After state:
# ------------
#
# test#show running-config | section interface
# interface Ethernet1
# !
# interface Ethernet2
#    description Configured by Ansible
#    shutdown
# !
# interface Management1
#    ip address dhcp
#    dhcp client accept default-route

# using rendered

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_l2_interfaces:
    config:
    - name: Ethernet1
      mode: trunk
      trunk:
        native_vlan: 10
    - name: Ethernet2
      mode: access
      access:
        vlan: 30
    state: rendered

# Module Execution Result:
# ------------------------
#
# rendered:
# - interface Ethernet1
# - switchport mode trunk
# - switchport trunk native vlan 10
# - interface Ethernet2
# - switchport mode access
# - switchport access vlan 30

# Using parsed

# File: parsed.cfg
# ----------------
#
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !

- name: Parse the commands for provided configuration
  arista.eos.l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# parsed:
#  - name: Ethernet1
#    mode: trunk
#    trunk:
#      native_vlan: 10
#  - name: Ethernet2
#    mode: access
#    access:
#      vlan: 30

# Using gathered

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#    switchport trunk native vlan 10
#    switchport mode trunk
# !
# interface Ethernet2
#    switchport access vlan 30
# !

- name: Gather interfaces facts from the device
  arista.eos.l2_interfaces:
    state: gathered

# Module Execution Result:
# ------------------------
#
# gathered:
# - name: Ethernet1
#   mode: trunk
#   trunk:
#     native_vlan: 10
# - name: Ethernet2
#   mode: access
#   access:
#     vlan: 30
"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - interface Ethernet1
    - switchport mode trunk
    - switchport access vlan 20
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - interface Ethernet1
    - switchport mode trunk
    - switchport access vlan 20
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.l2_interfaces.l2_interfaces import (
    L2_interfacesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.l2_interfaces.l2_interfaces import (
    L2_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=L2_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = L2_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
