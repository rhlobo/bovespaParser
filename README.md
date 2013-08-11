bovespaParser
=============
A Python parser for BM&amp;F Bovespa Historical Series Files


### Features:
- Parses COTAHISTXXXX.TXT files
- Parses data passed as string array
- Configurable to retrieve specific data:
    * Contains market type filters (VISTA, OPCOES, ...)
    * Accepts configuration of desired data fields to be retrieved
    * Data fields order can be freely specified

### Installing:
    pip install bovespaparser
There are no external dependencies.

### Usage
#### Getting started
In the sample code presented bellow, you can check out how to parse a file and print it's data out:
```python
import bovespaparser.bovespaparser as bvparser

with open('filename', 'rU') as f:
	result = bvparser.parsedata(f)

print result
```

The results returned by the `parsedata` function consists of a list of lists: a list of records, where a record holds some information-data for a stock paper in a certain day (a line on the given file).

The `parsedata` function has two optional parameters:
```python
def parsedata(data, opts=[CODNEG, DATA, PREABE, PREMIN, PREMAX, PREULT, QUATOT], market=VISTA):
    # implementation ...
```
- **opts** parameter: specifies what information should be retrieved for each stock paper tick;
- **market** parameter: specifies the desired market data (filters out other markets)

Calling the function (using the default parameters) would then return a list of records holding:
- **symbol** - the stock symbol (str)
- **date** - the period of the quotation tick (datetime.datetime)
- **open** - stock tick open value (float)
- **min** - stock tick min value (float)
- **max** - stock tick max value (float)
- **close** - stock tick close value (float)
- **volume** - the volume in the period (int)

So, it easy to analyse results:
```python
for symbol, datetime, f_open, f_min, f_max, f_close, volume in results:
    # process data ...
```

To find out more about the available parameter options and its meanings, refer to the official BMFBOVESPA documentation (also present on the docs directory).

#### Importing data into pandas
Bellow, a (not so pretty/optimized) example of how to import data from a file and creating `pandas dataframes` for each stock symbol:
```python
# -*- coding: utf-8 -*-


import pandas
import collections
import bovespaparser.bovespaparser as bvparser


class CotahistImporter(object):

    def __init__(self, f):
        self.dataFrameMap = {}

        dataMap = collections.defaultdict(list)
        mapping = [("open", 1), ("high", 2), ("low", 3), ("close", 4), ("volume", 5)]

        for symbol, datetime, openv, minv, maxv, close, volume in bvparser.parsedata(f):
            symbolData = dataMap.get(symbol)
            symbolData.append([datetime, openv, maxv, minv, close, volume])

        for symbol in dataMap.keys():
            dataMap.get(symbol).sort()
            data = zip(*dataMap.get(symbol))
            timeseries = dict((column_name, pandas.TimeSeries(data[column_index], index=data[0], name=column_name)) for column_name, column_index in mapping)
            self.dataFrameMap[symbol] = pandas.DataFrame(timeseries, columns=['open', 'high', 'low', 'close', 'volume'])

    def getDataFrameMap(self):
        return self.dataFrameMap
```

### Links:
- [BovespaParser Annoucment Blog Post](http://how.i.drycode.it/2012/09/python-bovespa-parser.html)
- [BovespaParser Git Repository]( https://github.com/rhlobo/bovespaParser)
- [Documentation](http://www.bmfbovespa.com.br/shared/iframe.aspx?idioma=pt-br&amp;url=http://www.bmfbovespa.com.br/pt-br/cotacoes-historicas/FormSeriesHistoricas.asp)
 (for Bovespa's Historical Series data files)

---------------------------------------
### Any feedback is always appreciated!
- Write to the author:  <rhlobo+stockExperiments@gmail.com>
