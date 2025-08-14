#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write(
        "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
        .format(
            random.randint(1, 255), random.randint(1, 255),
            random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024))
    )
    sys.stdout.flush()


# example
'<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'
'37.128.34.206 - [2025-08-13 11:22:14.093182] "GET /projects/260 HTTP/1.1" 301 846'
