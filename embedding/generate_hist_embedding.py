import pickle
import numpy as np

def listToString(s):
	# initialize an empty string
	str1 = ""
	# traverse in the string
	for ele in s:
		str1 += ' '+str(ele)
	# return string
	return str1


with open('/content/drive/MyDrive/embedding/eng-fiction-all/sgns/1970-vocab.pkl', 'rb') as f:
    lex_data = pickle.load(f)
    
arry_data = np.load('/content/drive/MyDrive/embedding/eng-fiction-all/sgns/1970-w.npy') 
file3 = open('/content/drive/MyDrive/embedding/Hist-1970-300d_new.txt','w')
for i in range(len(lex_data)):
  first = lex_data[i]+' '+listToString(arry_data[i])
  file3.write(first+'\n')
