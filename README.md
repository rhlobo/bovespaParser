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

The `parsedata` function accepts an `opts` parameter, which specifies what information should be retrieved for each stock paper tick. The default information retrieved, when `opts` is not passed, is:
- symbol
- date
- open
- min
- max
- close
- volume

### Links:
- [BovespaParser Annoucment Blog Post](http://how.i.drycode.it/2012/09/python-bovespa-parser.html)
- [BovespaParser Git Repository]( https://github.com/rhlobo/bovespaParser)
- [Documentation](http://www.bmfbovespa.com.br/shared/iframe.aspx?idioma=pt-br&amp;url=http://www.bmfbovespa.com.br/pt-br/cotacoes-historicas/FormSeriesHistoricas.asp)
 (for Bovespa's Historical Series data files)

---------------------------------------
### Any feedback is always appreciated!
- Write to the author:  <rhlobo+stockExperiments@gmail.com>
