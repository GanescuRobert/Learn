import re

text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography'''

text2 = 'peter piper picked a peck of pickled peppers'

text3 = 'crypto-bot that is trading Bitcoin and other currencies'

text4 = 'cryptographic encryption methods that can be cracked easily with quantum computers'

print(re.findall('b...k', text))
print(re.findall('\w*y.*y', text))
print(re.findall('blocks?', text))

print(re.findall('p\w*?e\w*?r',text2))

pattern = re.compile('crypto(.{1,30})coin')

print (pattern.match(text3))

print (pattern.match(text4))

## Data
report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
'''

dollars = [d+f for d,f in re.findall('(\$\d+)(\.\d+)?',report)]
print(dollars)