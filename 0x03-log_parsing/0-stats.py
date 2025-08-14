#!/usr/bin/python3
""" log parsing """
import sys
import re
import signal
from datetime import datetime


i = 0
size = 0
all_status = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

# just for learning
# matches numbers 1-255 (unused for this version)
# byte_pattern = '(?:[1-9]|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])'
# pattern = (
#    r'^({0}\.){{3}}{0} - \[(.*?)\] '
#    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
# ).format(byte_pattern)

pattern = (
    r'^\S+?\s*-\s*\[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) \d+$'
)


def show_stats():
    """ show logs """
    print(f'File size: {size}')
    for k, v in all_status.items():
        if v != 0:
            print(f'{k}: {v}')


def handler(signum, frame):
    """ handle signal """
    show_stats()
    sys.exit(0)


signal.signal(2, handler)


for line in sys.stdin:
    try:
        file_size = line.split()[-1]
        size += int(file_size)
    except Exception:
        size += 0
    m = re.match(pattern, line)
    i += 1
    if m:
        date = m.group(1)
        status = m.group(2)
        try:
            valid_date = datetime.strptime(
                date, "%Y-%m-%d %H:%M:%S.%f")
        except Exception:
            valid_date = None

        if status in all_status and valid_date:
            all_status[status] += 1

    if i % 10 == 0:
        show_stats()

show_stats()  # this is like EOF
