#!/bin/env python

import json

inventory = {
    'simplegroupA': {
        'hosts': [
            'simplehostA',
            'simplehostB',
            'simplehostC',
        ]
    }
}

print(json.dumps(inventory))
