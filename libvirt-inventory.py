#!/bin/env python

import argparse
import json
import yaml

try:
    import libvirt
except ImportError as ex:
    print("Importing python libvirt bindings failed with: {}".format(ex))
    exit(1)


class Context:
    libvirtURIs = None

    def __init__(self, config=None):
        if config is None:
            config = "./libvirt-inventory.yaml"

        with open(config) as c:
            data = yaml.safe_load(c)
            self.libvirtURIs = data['libvirtURIs']


class LibVirtConnection:
    _connections = None

    def __init__(self, ctx=None):
        self._connections = [libvirt.openReadOnly(host) for host in ctx.libvirtURIs]  # noqa: E501

    def domainNames(self, ):
        domains = []
        for c in self._connections:
            allDomains = c.listAllDomains(0)
            [domains.append(d.name()) for d in allDomains]
        return domains


def process_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", help="return all managed host groups",
                       action="store_true")
    group.add_argument("--host", help="print variables of host")

    return parser


def make_inventory(hosts):
    return {
        "libvirt": {
            "hosts": [
                hosts
            ]
        }
    }


if __name__ == "__main__":
    parser = process_arguments()
    parser.parse_args()

    ctx = Context()
    virt = LibVirtConnection(ctx)
    hosts = virt.domainNames()

    print(json.dumps(make_inventory(hosts)))
