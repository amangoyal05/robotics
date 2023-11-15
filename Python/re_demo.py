# regex rules
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

github.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# r - Makes Python handle a string literally
print(r'\tTab')

# compile - compiles a regular expression pattern
pattern = re.compile(r'abc')
pattern1 = re.compile(r'\.')                                # \ is used for escaping meta-characters and only referring to the instances where they are actually used
url_find = re.compile(r'github\.com')
num_pat = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')       # [] - character set
# num_pat = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')     # This will only match numbers that begin with 800 or 900
range_num = re.compile(r'[1-5]')                            # Finds all number in the range 1 to 5
# range_find = re.compile(r'[1-5a-zA-Z]')                   # Finds all characters in the range 1 to 5 or a to z or A to Z
word_search = re.compile(r'[^b]at')                         # Matches all 3 letters word that not beginning with b and ending in at
num_pat = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')            # {} - Specifies the number of characters
pattern2 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')            # ? - Each either one or zero occurence of the character just before

matches = pattern.finditer(text_to_search)
matches1 = pattern1.finditer(text_to_search)
url_search = url_find.finditer(text_to_search)
range_search = range_num.finditer(text_to_search)
word_find = word_search.finditer(text_to_search)
matches2 = pattern2.finditer(text_to_search)

with open('data.txt', 'r') as f:
    contents = f.read()
    number_search = num_pat.finditer(contents)

    for match in number_search:
        print(match)

for match in matches:
    print(match)

for match in matches1:
    print(match)

for match in url_search:
    print(match)

for match in range_search:
    print(match)

for match in word_find:
    print(match)

for match in matches2:
    print(match)


emails = '''
AmanGoyal@gmail.com
aman.goyal@university.edu
aman-321-goyal@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+.[a-zA-Z0-9-.]+

matches = pattern.finditer(emails)

for match in matches:
    print(match)


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

subbed_urls = pattern.sub(r'\2\3', urls)

for match in matches:
    print(match)

print(subbed_urls)