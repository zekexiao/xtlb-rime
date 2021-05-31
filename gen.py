#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Tool for parse 小小码表 to rime码表

out = open("xtlb.dict.yaml", "w+", encoding='utf-8')
out.write('''#	Rime	dictionary
#	encoding:	utf-8
#

---
name:	xtlb
version: "final"
sort:	original
use_preset_vocabulary: false
columns:
 -	text
 -	code
 -	weight
 -	stem
encoder:
 exclude_patterns:
  -	'^i.*$'
 rules:
   - length_equal: 2
     formula: "AaAbBaBb"
   - length_equal: 3
     formula: "AaAbBaCa"
   - length_in_range:	[4,	10]
     formula: "AaBaCaZa"
     
...

''')

k = 0
with open("xtlb.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        if(k < 12):
            k = k + 1 #前十来行没用，中间还有空格，直接跳过
            continue
        line = line.strip('\n')
        d = line.split(' ')
        for i in range(1, len(d)):
            if(d[i].find("$") == -1):
                out.write(d[i] + "	" + d[0] + "\n")
out.close()
