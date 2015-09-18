# !/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import json
import sys


class NetworkTotal(object):
    def __init__(self):
        self.url = 'https://networktotal.com/search.php?q='

    def query(self, md5sum):
        url = '{}{}&json=1'.format(self.url, md5sum)
        req = urllib2.Request(url)
        rsp = urllib2.urlopen(req)
        js = json.load(rsp)
        for key in js:
            print key
            if type(js[key]) is list:
                for value in js[key]:
                    print '\t{}'.format(value)
            else:
                print '\t{}'.format(js[key])


def main():
    md5sum = sys.argv[1]
    print 'Query {} on NetworkTotal.com'.format(md5sum)
    nt = NetworkTotal()
    nt.query(md5sum)


main()
