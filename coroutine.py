#!/usr/bin/env python


def line_splitter(delimeter=None):
    print "Ready to Split"
    result = None
    while True:
        line = (yield result)
        result = line.split(delimeter)
