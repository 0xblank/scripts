import re
import fileinput

with fileinput.input(inplace=True,encoding='utf-8') as f:
    for line in f:
        if re.search('!\[\]\((http[^)\!\[\]\(]+)\)', line):
            link = re.search('!\[\]\((http[^)\!\[\]\(]+)\)', line).group(1)
            new_line = '<img src="{}" alt="drawing" width="350"/>'.format(link)
            print(new_line,end='\n')
        else:
            print(line,end='')