# -*- coding: utf-8 -*-
"""uri1255.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dm141Qgq2xtuaSWWoxZ2OsgoLtNm7LSl
"""

N = int(input())


for l in range(N):

  s = input()
  s = s.lower()
  s2 = ''
  for j in range (len(s)):
    if s[j].isalpha():
      s2 = s2 + s[j];
  x = sorted(s2)

  #Dictionary to map repeated strings
  my_dict = {i:x.count(i) for i in x}

  #Most Frequence String
  itemMaxValue = max(my_dict.items(), key=lambda z: z[1])
 
 
  listOfKeys = list()
  # Iterate over all the items in dictionary to find keys with max value
  for key, value in my_dict.items():
      if value == itemMaxValue[1]:
         listOfKeys.append(key)

  s3 = '';
  for a in listOfKeys:
    s3 = s3 + a;
  print(s3);