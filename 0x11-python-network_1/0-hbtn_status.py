#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response_type = type(response)
    print(f'Body response:')
    print(f'\t- type: {response_type}')
    response_content = response.read()
    print(f'\t- content: {response_content}')

    response_utf8_content = response_content.decode('utf-8')
    print(f'\t- utf8 content: {response_utf8_content}')
