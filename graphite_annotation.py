#!/usr/bin/python

""" send events to graphite's event store """

# Requirements:
# pip install urllib3[secure]
# python2

# We verify certificates, this depends on the urllib3[secure] libraries.

# Graphite Events documentation = http://graphite.readthedocs.io/en/latest/events.html

# usage:
# python graphite_annotation.py --what "Title" --tag "tag" --data "D" --url https://example.com

###########

import argparse
import json
import urllib3

PARSER = argparse.ArgumentParser(description='Send annotations to graphite')
PARSER.add_argument('--what', dest='what', required=True,
                    help='What - Title')
PARSER.add_argument('--tag', dest='tag', required=True,
                    help='tag - only one')
PARSER.add_argument('--data', dest='data', default="",
                    help='more detailed and longer description')
PARSER.add_argument('--url', dest='url', required=True,
                    help='url, for example https://graphite.example.com')
PARSER.add_argument('--uri', dest='uri', default="/events/",
                    help='uri, for example /events/ which is the default')

ARGS = PARSER.parse_args()

def send_event(args):
    """ make a dict with the data provided as args and turn it into JSON """

    url = args.url
    uri = args.uri
    urluri = str(url) + str(uri)

    datadict = {}
    datadict['what'] = args.what
    datadict['tags'] = args.tag
    datadict['data'] = args.data

    # convert the dict into JSON
    jsondata = json.dumps(datadict).encode('utf8')

    # https://stackoverflow.com/questions/31778800/how-can-i-make-a-post-request-on-python-with-urllib3
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    http.request(
        "POST",
        urluri,
        body=jsondata,
        headers={'Content-Type': 'application/json'})

######

send_event(ARGS)
