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
- *opts* parameter: specifies what information should be retrieved for each stock paper tick;
- *market* parameter: specifies the desired market data (filters out other markets)

Calling the function (using the default parameters) would then return a list of records holding:
- _symbol_ - the stock symbol (*str*)
- _date_ - the period of the quotation tick (*datetime.datetime*)
- _open_ - stock tick open value (*float*)
- _min_ - stock tick min value (*float*)
- _max_ - stock tick max value (*float*)
- _close_ - stock tick close value (*float*)
- _volume_ - the volume in the period (*int*)

To find out more about the available parameter options and its meanings, refer to the official BMFBOVESPA documentation (also present on the docs directory).

### Links:
- [BovespaParser Annoucment Blog Post](http://how.i.drycode.it/2012/09/python-bovespa-parser.html)
- [BovespaParser Git Repository]( https://github.com/rhlobo/bovespaParser)
- [Documentation](http://www.bmfbovespa.com.br/shared/iframe.aspx?idioma=pt-br&amp;url=http://www.bmfbovespa.com.br/pt-br/cotacoes-historicas/FormSeriesHistoricas.asp)
 (for Bovespa's Historical Series data files)

---------------------------------------
### Any feedback is always appreciated!
- Write to the author:  <rhlobo+stockExperiments@gmail.com>
