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
    easy_install bovespaparser
or
    pip install bovespaparser

### Usage
´´´python
import bovespaparser.bovespaparser as bvparser

with open('filename', 'rU') as f:
	result = bvparser.parsedata(f)

print result
´´´

### Links:
- [BovespaParser Annoucment Blog Post](http://how.i.drycode.it/2012/09/python-bovespa-parser.html)
- [BovespaParser Git Repository]( https://github.com/rhlobo/bovespaParser)
- [Documentation](http://www.bmfbovespa.com.br/shared/iframe.aspx?idioma=pt-br&amp;url=http://www.bmfbovespa.com.br/pt-br/cotacoes-historicas/FormSeriesHistoricas.asp)
 (for Bovespa's Historical Series data files)

---------------------------------------
### Any feedback is always appreciated!
- Write to the author:  <rhlobo+stockExperiments@gmail.com>
