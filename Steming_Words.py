import numpy as np
from ntlk.stem import PortStemer
from nltk.tokenize import word_tokenize
ps =PortStemer()
words =["program","programs","programer","programming","programers"]
for w in word:
  print(w,":",ps.stem(w))
