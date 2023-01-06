import numpy as np
import pickle

filename = '/content/drive/MyDrive/embedding/twitter-genuine-tweets-master/222syn_finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

TextToTensor_instance = TextToTensor(
tokenizer=loaded_model.tokenizer,
max_len=20
)


m2 = []
for each in new_matrix:
  num1 = each
  m1 = []
  for each2 in new_matrix:
    num2 = each2
    input_string = [str(num1)+' '+str(num2)]
    
    good_nn = TextToTensor_instance.string_to_tensor(input_string)
    p_good = loaded_model.model.predict(good_nn)[0][0]
    
    m1.append(p_good)
  m2.append(m1)
  

m = np.array(m2)
print(len(m[0]))
