#!/usr/bin/python
# Filename: parsingutils.py


def _no_conversion(data):
    return data


def _money_conversion(data):
    return float(data) / 100


def _rstrip_conversion(data):
    return data.rstrip()


NO, INT, MONEY, RTRIM = [_no_conversion, int, _money_conversion, _rstrip_conversion]


class DataSegment:

    def __init__(self, startIndex=0, endIndex=0, postProcessing=NO):
        self._slice = slice(startIndex, endIndex)
        self._funct = postProcessing

    def parse(self, data):
        return self._funct(data[self._slice])
