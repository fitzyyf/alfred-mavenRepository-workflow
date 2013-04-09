#!/usr/bin/python
#_*_ coding:UTF-8 _*_
# 
# Copyright 2012-2013 by yfyang. All Rights Reserved.

import json
import urllib
import urllib2

import alfred


theQuery = u'{query}'
# theQuery = 'Spring'
theQuery = urllib.quote_plus(theQuery)
url = 'http://search.maven.org/solrsearch/select?q=%s&rows=20&wt=json' % theQuery

request = urllib2.Request(url)
req_open = urllib2.build_opener()
conn = req_open.open(request)
req_data = conn.read()

data = json.loads(req_data)

results = []

response = data['response']

for doc in response['docs']:
	arg = doc['id']
	group = doc['g']
	artifact = doc['a']
	version = doc['latestVersion']

	zb = "%s:%s:%s" % (group, artifact, version)

	item = alfred.Item({'uid': 1, 'arg': zb}, zb, arg,('cmp.gif', {'type': 'gif'}))
	results.append(item)

xml = alfred.xml(results)
alfred.write(xml)