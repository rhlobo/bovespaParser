#!/usr/bin/python


import unittest
import os
from functools import partial
import datetime
from .. import bovespaparser as parser


DATAHEADER = "00COTAHIST.2012BOVESPA 20120808                                                                                                                                                                                                                      "
DATAFOOTER = "99COTAHIST.2012BOVESPA 2012080800000197525                                                                                                                                                                                                           "
DATARECORD = "012012010202ABCB4       010ABC BRASIL  PN  EJ  N2   R$  000000000122100000000012440000000001175000000000119400000000011850000000001185000000000119300465000000000000131800000000000157420100000000000000009999123100000010000000000000BRABCBACNPR4117"


class TestBovespaParserFunctions(unittest.TestCase):

    def test_parsefile_should_return_correct_number_of_records_for_default_market(self):
        result = self.__parsefile(self.__getfilepath("testdata.txt"))
        self.assertEqual(len(result), 11)

    def test_parsefile_should_return_correct_number_of_records_for_custom_market(self):
        result = self.__parsefile(self.__getfilepath("testdata.txt"), parser.FRACIONARIO)
        self.assertEqual(len(result), 6)

    def test_parsedata_should_ignore_header_and_footer(self):
        data = [DATAHEADER, DATAFOOTER]
        result = parser.parsedata(data)
        self.assertEqual(len(result), 0)

    def test_parsedata_should_return_correct_number_of_records(self):
        result = parser.parsedata([DATAHEADER, DATARECORD, DATARECORD])
        self.assertEqual(len(result), 2)

    def test_parsedata_should_return_correct_default_values(self):
        func = partial(parser.parsedata)
        self.__verify_parsedata_return_values(func, ['ABCB4', datetime.date(2012, 01, 02), 12.21, 11.75, 12.44, 11.85, 157420100])

    def test_parsedata_should_only_return_desired_values(self):
        func = partial(parser.parsedata, opts=[parser.CODNEG])
        self.__verify_parsedata_return_values(func, ['ABCB4'])

    def test_parsedata_should_return_desired_values_order(self):
        func = partial(parser.parsedata, opts=[parser.CODNEG, parser.NOMRES])
        self.__verify_parsedata_return_values(func, ['ABCB4', 'ABC BRASIL'])

    def __verify_parsedata_return_values(self, func, values):
        data = [DATAHEADER, DATARECORD, DATAFOOTER]
        result = func(data)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), len(values))
        self.assertEqual(result[0], values)

    def __parsefile(self, filename, market=parser.VISTA):
        with open(filename) as f:
            return parser.parsedata(f, [], market)

    def __getfilepath(self, name):
        path = os.path.split(__file__)[0]
        return os.path.join(path, name)


if __name__ == '__main__':
    unittest.main()
