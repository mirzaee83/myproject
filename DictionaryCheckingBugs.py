#!/usr/bin/env python
# coding: utf-8

# In[1]:


dictionary = {'this': 'این', 'is': 'هست', 'a': 'یک', 'chair': 'صندلی', '.': '.', '?': '؟', '!': '!'}
import matplotlib
    
text = input()

text = text.replace('.', " .")
text = text.replace('?', " ?")
text = text.replace('!', " !")
words = text.split()
l = len(words)

l_final = []
for i in range(l):
    x = words[i]
    for word in dictionary.keys():
        if word == x:
            translation = dictionary[word]
            l_final.append(translation)
            print(translation)#, end = " ")

#spec_chars = ["!",'.',"?",]

count = len(l_final)            
l_count_chars = []
for j in range(count):
    if l_final[j] == '.':
        l_count_chars.append(j)

for k in range(len(l_count_chars)):
    l_final[(l_count_chars[k] - 1):l_count_chars[k]] = [''.join(map(str,l_final[(l_count_chars[k] - 1):l_count_chars[k]]))]
    print(l_final)


# In[ ]:




