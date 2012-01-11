#! /usr/bin/env python

import sys
import os

LOGIN_IDBOOSTER = '75054'
PROXY_IP = '10.1.40.3'
PROXY_PORT = '3128'

HTTP_PROXY = 'http_proxy'
HTTPS_PROXY = 'https_proxy'
HTTP_PROTOCOL = 'http'


def putenv(name, value):
	os.putenv(name, value)
	print 'Put in local env ' + name + ' with value : ' + value


if len(sys.argv) != 2:
	print 'Invalid arguments'
	sys.exit(0)

password = sys.argv[1]

if not password:
	print 'Password is required as first argument'
	sys.exit(0)

proxy = HTTP_PROTOCOL + '://' + LOGIN_IDBOOSTER + ':' + password + '@' + PROXY_IP + ':' + PROXY_PORT
putenv(HTTP_PROXY, proxy)
putenv(HTTPS_PROXY, proxy)

print 'Done.'