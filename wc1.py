#!/usr/bin/env python
# coding: utf-8

# In[67]:


#!/usr/bin/env python3
# Juliette Gudknecht
# 2020-02-10
# character, word, and line counting program with #read()
#wc1.py

#read() method
h = open('/Users/juliettegudknecht/Downloads/short-paragraph-3.txt','rt')
data = h.read()
filename = 'short-paragraph-3.txt'

#character count
char = len(data)

#word count
word = data.split()
words = len(word)

#lines count
lines = len(data.split('\n')) - 1
# -1 because of the last line

print(filename,char,'characters',words,'words',lines,'lines')
h.close()


# In[ ]:





# In[ ]:





# In[ ]:




