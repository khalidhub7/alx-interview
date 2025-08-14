#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
import signal
from datetime import datetime


all_status = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
size = 0
i = 0

# matches numbers 1–255
byte_pattern = '(?:[1-9]|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])'
pattern = (
    r'^({0}\.){{3}}{0} - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)\n$'
).format(byte_pattern)


# define a signal


def handler(signum, frame):
    """ handle signal """
    print(f'File size: {size}')
    for k, v in all_status.items():
        if v != 0:
            print(f'{k}: {v}')


signal.signal(2, handler)


for line in sys.stdin:
    i += 1
    m = re.match(pattern, line)
    if m:
        date = m.group(2)
        status = m.group(3)
        if status in all_status:
            all_status[status] += 1
        size += int(m.group(4))

        try:
            valid_date = datetime.strptime(
                date, "%Y-%m-%d %H:%M:%S.%f")
        except Exception:
            valid_date = None

        if i % 10 == 0 and valid_date and status in all_status:
            print(f'File size: {size}')
            for k, v in all_status.items():
                if v != 0:
                    print(f'{k}: {v}')
