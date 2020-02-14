#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python3
# Juliette Gudknecht
# 2020-02-10
# character, word, and line counting program with #readlines()
#wc2.py

#readlines() method
filename = input('what file?')
h = open(filename,'rt')
data = h.readlines()


#word count
w = []
for line in data:
    for word in line.split():
        w.append(word) 
words2 = len(w)

#lines count
line2 = []
for l in data:
    line2.append(l)
lines2= len(line2)

#char count
char2 = 0
for l in line2:
    char2 += len(l)

    
print(filename,char2,'characters',words2,'words',lines2,'lines')
h.close()


# In[ ]:




