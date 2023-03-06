# Package for data wrangling
import pandas as pd 

# Package for array math
import numpy as np 

# Package for system path traversal
import os

# Package for working with dates
from datetime import date

# K fold analysis package
from sklearn.model_selection import KFold

# Import the main analysis pipeline
from pipeline import Pipeline

# Tensor creation class
from text_preprocessing import TextToTensor

# Reading the configuration file
import yaml
with open("conf.yml", 'r') as file:
    conf = yaml.safe_load(file).get('pipeline')

# Reading the stop words
stop_words = []
try:
    stop_words = pd.read_csv('data/stop_words.txt', sep='\n', header=None)[0].tolist()
except Exception as e:
    # This exception indicates that the file is missing or is in a bad format
    print('Bad stop_words.txt file: {e}')

# Reading the data
train = pd.read_csv('data/train.csv')[['text', 'target']]
test = pd.read_csv('data/test.csv')

# Shuffling the data for the k fold analysis
#train = train.sample(frac=1)

# Creating the input for the pipeline
X_train = train['text'].tolist()
print(X_train[0])
Y_train = train['target'].tolist()
print(Y_train[0])

X_test = test['text'].tolist()


# Running the pipeline with all the data
results = Pipeline(
    X_train=X_train,
    Y_train=Y_train, 
    embed_path='/Users/lenayang/Downloads/twitter-genuine-tweets-master/glove.6B.300d.txt',
    embed_dim=300,
    stop_words=stop_words,
    X_test=X_test,
    max_len=conf.get('max_len'),
    epochs=7,
    batch_size=conf.get('batch_size')
)

# Some sanity checks
good = ["bike bicycle"]
bad = ["bike car"]

TextToTensor_instance = TextToTensor(
tokenizer=results.tokenizer,
max_len=conf.get('max_len')
)

# Converting to tensors
good_nn = TextToTensor_instance.string_to_tensor(good)
bad_nn = TextToTensor_instance.string_to_tensor(bad)

# Forecasting
p_good = results.model.predict(good_nn)[0][0]
p_bad = results.model.predict(bad_nn)[0][0]

print(f'Sentence: {good_nn} Score: {p_good}')
print(f'Sentence: {bad_nn} Score: {p_bad}')

# Saving the predictions
test['prob_is_genuine'] = results.yhat
test['target'] = [1 if x > 0.5 else 0 for x in results.yhat]
 
# Saving the predictions to a csv file
if conf.get('save_results'):
    if not os.path.isdir('output'):
        os.mkdir('output')    
    test[['text', 'target']].to_csv(f'output/submission_{date.today()}.csv', index=False)

import pickle
filename = '/Users/lenayang/Downloads/twitter-genuine-tweets-master_2/new_333_syn_finalized_model.sav'
pickle.dump(results, open(filename, 'wb'))
