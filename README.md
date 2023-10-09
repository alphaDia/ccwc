## ccwc.py command line tool  

The unix wc tool challenge is provided by [John crickett](https://www.linkedin.com/in/johncrickett)  

ccwc.py is a command line tool built to generate file metric like:  

- Number of lines  
- Number of words  
- Number of bytes  
- Number of characters  
  
It has multiple file support, which means it can take more than one file, if no file is given it will read **stdin**.  

> try it out: python3 ccwc.py -h a help message will appear like the one below.

usage: ccwc.py [options] FILE [FILE...]  

Print newline, word and byte for each file  

positional arguments:  
  FILE        take a file or a list of files  

optional arguments:  
  -h, --help  show this help message and exit  
  -l, --line  print the line counts  
  -c, --byte  print the byte counts  
  -m, --char  print the character counts  
  -w, --word  print the word counts  

i.e:

> python3 ccwc.py utilities.py

*output:*  
22 56 459 utilities.py  

> python3 ccw.py utilities.py utilities.py

*output:*  
22 56 459 utilities.py  
22 56 459 utilities.py  
44 112 918 total  
