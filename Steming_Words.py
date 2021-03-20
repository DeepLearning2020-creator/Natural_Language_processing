!pip install nltk
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps =PorterStemmer()
words =["program","programs","programer","programming","programers"]
for w in words:
  print(w,":",ps.stem(w))
