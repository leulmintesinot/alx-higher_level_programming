#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

request = urllib.request.Request(url)

with urllib.request.urlopen(request) as response:
    request_id = response.headers.get('X-Request-Id')
    print(f'{request_id}')
