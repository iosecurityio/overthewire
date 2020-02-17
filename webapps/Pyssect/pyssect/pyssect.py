#!/usr/bin/python

# Parses URLS for parameters and values
# Can brute force directories and files

from urllib.parse import urlsplit
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, sys

# target = 'https://notices.rei.com/pub/cc?_ri_=X0Gzc2X%3DYQpglLjHJlYQGlzgrUuDoFwYhOXw7IOJtMkXzet485LP184ezfyh2hio6awBjyN1wWVXtpKX%3DSRSURUSS&_ei_=EuFBWJqUWaLLkAGD46ZqJrUbr5-YyY_DjIDdYqp_nNjkND0ck3O66ynK-LSVPorUrAeMFI2rGCZttWMaKBZQSvV558sdFVYMDViP9dcPMmib5YufWANGVXqcCxEPeLQj4SNfONGEo9LhP7OffEAyVbpvBdVv2Ydrnq-rmSTelxDncLSWBPa-bFxNaDTvBwMg72-TOfEQmwc1M3R0ZInXkZ4VEdDYGpVSeoJWyjEhV4waNiF1EnSMILRw5gu8B4mjP2zF82HTQgzHHsGEVjE6kxgrdvruhsyur-ZFAazYeE9E-advv0MnFZKkxboyAbtWliG91T7j.&_di_=ipunve4fji97i05k16klrmh5pbi629smgv8nbh403qj39ijif7kg'

if len(*args) != 2:
    sys.exit('No Target URL')

class Target:
    'Base class for Target to enumerate'
    #Get Target as input
    url = sys.argv[1]

    def __init__(self, protocol=urlsplit(url[0]), domain=urlsplit(url[1]), path=urlsplit(url[2]), query=urlsplit(url[3]), cookies=None):
        self.protocol = protocol 
        self.domain = domain
        self.path = path
        self.query = query
        self.cookies=cookies


targetURL = Target()
'''
TODO

# Look for a directory function
# urllib.parse.urljoin(base, url)
# url = fileinput

# Look for a file function
# # Brute Force
# # Exists?
'''