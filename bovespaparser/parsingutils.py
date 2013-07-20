#!/usr/bin/python


import datetime


def __no_conversion(data):
    return data


def __money_conversion(data):
    return float(data) / 100


def __rstrip_conversion(data):
    return data.rstrip()


def __date_conversion(data):
    return datetime.datetime(int(data[0:4]), int(data[4:6]), int(data[6:8]))


NO, INT, MONEY, RTRIM, DATE = ([__no_conversion,
                                int,
                                __money_conversion,
                                __rstrip_conversion,
                                __date_conversion])


class DataSegment:

    def __init__(self, startIndex=0, endIndex=0, postProcessing=NO):
        self.__slice = slice(startIndex, endIndex)
        self.__funct = postProcessing

    def parse(self, data):
        return self.__funct(data[self.__slice])
