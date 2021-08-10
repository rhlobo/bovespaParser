#!/usr/bin/python
# Filename: bovespaparser.py


try:
    import parsingutils as util
except:
    import bovespaparser.parsingutils as util


TIPREG, DATA, CODBDI, CODNEG, TPMERC, NOMRES, ESPECI, PRAZOT, MODREF, PREABE, PREMAX, PREMIN, PREMED, PREULT, PREOFC, PREOFV, TOTNEG, QUATOT, VOLTOT, PREEXE, INDOPC, DATEN, FATCOT, PTOEXE, CODISI, DISMES = [util.DataSegment(*i) for i in [(0, 2), (2, 10, util.DATE), (10, 12), (12, 24, util.RTRIM), (24, 27), (27, 39, util.RTRIM), (39, 49), (49, 52), (52, 56), (56, 69, util.MONEY), (69, 82, util.MONEY), (82, 95, util.MONEY), (95, 108, util.MONEY), (108, 121, util.MONEY), (121, 134, util.MONEY), (134, 147, util.MONEY), (147, 152, util.INT), (152, 170, util.INT), (170, 188, util.INT), (188, 201), (201, 202), (202, 210, util.DATE), (210, 217), (217, 230), (230, 242), (242, 245)]]
VISTA, EXERCICIO_OPCAO_COMPRA, EXERCICIO_OPCAO_VENDA, LEILAO, FRACIONARIO, TERMO, OPCAO_COMPRA, OPCAO_VENDA = ['010', '012', '013', '017', '020', '030', '070', '080']


def parsedata(data, opts=[CODNEG, DATA, PREABE, PREMIN, PREMAX, PREULT, QUATOT], market=VISTA):
    return [[opt.parse(line) for opt in opts] for line in data if TIPREG.parse(line) == '01' and TPMERC.parse(line) == market]
