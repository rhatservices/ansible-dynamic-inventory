#!/bin/env python

import argparse
import json


class Host:
    name = ""


def process_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", help="return all managed host groups",
                       action="store_true")
    group.add_argument("--host", help="print variables of host")

    return parser


def generate_host(i):
    host = Host()
    host.name = "host{:d}".format(i)
    host.vars = {
        "var{:d}".format(i): True
    }

    return host


def make_inventory(hosts):
    return {
        "all": {
            "hosts": [
                "host1",
                "host2",
                "host3"
            ]
        }
    }


if __name__ == "__main__":
    parser = process_arguments()
    parser.parse_args()

    hosts = [generate_host(i) for i in range(1, 5)]

    print(json.dumps(make_inventory(hosts)))
