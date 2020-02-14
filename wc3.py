#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python3
# Juliette Gudknecht
# 2020-02-10
# character, word, and line counting program with #readline()
#wc3.py

#readline() method

h = open('/Users/juliettegudknecht/Downloads/short-paragraph-3.txt','rt')
filename = 'short-paragraph-3.txt'

# char, lines and word count all in the same loop
char3 = 0
txt1 = []
ww = 0
while True:
    line = h.readline()
    if not line:
        break;
    char3 += len(line)
    txt = line.split()
    txt1.append(txt) 
    ww += len(line.split())

lines3 = (len(txt1))
words3 = ww
  
print(filename,char3,'characters',words3,'words',lines3,'lines')
h.close()


# In[ ]:




