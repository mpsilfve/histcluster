######Original file is located at https://colab.research.google.com/drive/1imJlMtm0H6kPxqi42fPOdYCddalYhN2i

lines = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/data.noun", "rb").readlines()
lines = [line.decode(encoding="ascii", errors='surrogateescape').strip() for line in lines]
dict_all = {}
for line in lines[30:]:
    all_items = line.split(" ")
    synset_offset =  all_items[0]
    dict_all[synset_offset] = [all_items[1:]]

noun_all_list = ['!','@' ,'@i','~','~i','#m','#s','#p','%m','%s','%p','=','+',';c','-c',';r','-r',';u','-u']

file_out = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_other_relation.txt','w')
lines2 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/index.noun", "rb").readlines()
lines2 = [line2.decode(encoding="ascii", errors='surrogateescape').strip() for line2 in lines2]

for line2 in lines2[30:]:
    
    all_items2 = line2.split(" ")
    lemma =  all_items2[0]
    pos = all_items2[1]
    synset_cnt = all_items2[2]
    p_cnt = all_items2[3]
    synset_offset = all_items2[-int(synset_cnt):]
#     print(lemma)
#     print(synset_offset)
    find_results = []
    for each in synset_offset:
        try:
            find_results.append(dict_all[each][0])
            for result_candidate in find_results:
                for indivi_candi in result_candidate:
                    if indivi_candi in noun_all_list:
                        if indivi_candi == '!' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Antonym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '@' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Hypernym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '@i':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'InstanceHypernym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '~':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Hyponym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '~i' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'InstanceHyponym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '#m':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Member_holonym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '#s':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Substance_holonym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '#p' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Part_holonym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '%m':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Member_meronym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '%s':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Substance_meronym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '%p' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Part_meronym'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '=':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Attribute'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '+':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Derivationally_related_form'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == ';c' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Domain_of_synset_TOPIC'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '-c':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Member_of_this_domain_TOPIC'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == ';r':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Domain_of_synset_REGION'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '-r' :
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Member_of_this_domain_REGION'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == ';u':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Domain_of_synset_USAGE'+'\t'+str(target_noun[0][3])+'\n')
                        elif indivi_candi == '-u':
                            index = result_candidate.index(indivi_candi)
                            syn_result = result_candidate[index+1]
                            target_noun = dict_all[syn_result]
                            file_out.write(str(lemma)+'\t'+'Member_of_this_domain_USAGE'+'\t'+str(target_noun[0][3])+'\n')
                            
                    
        except:
            break

lines = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/data.noun", "rb").readlines()
lines = [line.decode(encoding="ascii", errors='surrogateescape').strip() for line in lines]
dict_all = {}

for line in lines[30:]:
    all_items = line.split(" ")
    synset_offset =  all_items[0]
    dict_all[synset_offset] = [all_items[1:]]

lines3 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/synonyms.csv", "rb").readlines()
lines3 = [line3.decode(encoding="utf-8").strip() for line3 in lines3]
syn_dict = {}
for line3 in lines3:
    all_items3 = line3.split(",")
    if all_items3[1] =='noun':
#         print(all_items[2])
        all_syn3 = all_items3[2].split(';')
        syn_dict[all_items3[0]] = all_syn3

lines2 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/index.noun", "rb").readlines()
lines2 = [line2.decode(encoding="ascii", errors='surrogateescape').strip() for line2 in lines2]
all_word_index = []
for line2 in lines2[30:]:
    
    all_items2 = line2.split(" ")
    lemma =  all_items2[0]
    pos = all_items2[1]
    synset_cnt = all_items2[2]
    p_cnt = all_items2[3]
    synset_offset = all_items2[-int(synset_cnt):]
    all_word_index.append(synset_offset[0])

all_word_index = set(all_word_index)

print(len(all_word_index))

import random



f22 = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_no_relation.txt','w')
lines2 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/index.noun", "rb").readlines()
lines2 = [line2.decode(encoding="ascii", errors='surrogateescape').strip() for line2 in lines2]

for line2 in lines2[30:]:
    
    all_items2 = line2.split(" ")
    lemma =  all_items2[0]
    pos = all_items2[1]
    synset_cnt = all_items2[2]
    p_cnt = all_items2[3]
    synset_offset = all_items2[-int(synset_cnt):]
#     print(lemma)
#     print(synset_offset)
    find_results = []
    for each in synset_offset:
        
        try:
            find_results.append(dict_all[each][0])
            no_relation =[]
            for result_candidate in find_results:
                have_relation = [each]
                no_relation_word_list = []
                for indivi_candi in result_candidate:
                    if len(indivi_candi) == 8 and indivi_candi.isdigit():
                        have_relation.append(indivi_candi)
#             print(have_relation)
            no_relation = [x for x in all_word_index if x not in have_relation]
#             print(no_relation)
            random_num1 = random.randint(0,70245)
#             print(random_num1)
            candidate1 = no_relation[random_num1]
            candidate1_word = dict_all[candidate1][0][3]
#             print(lemma)
#             print(candidate1_word)
            random_num2 = random.randint(0,70245)
            candidate2 = no_relation[random_num2]
            candidate2_word = dict_all[candidate2][0][3]
            random_num3 = random.randint(0,70245)
            candidate3 = no_relation[random_num3]
            candidate3_word = dict_all[candidate3][0][3]
#             no_relation_word_list.append(candidate1_word,candidate2_word,candidate3_word)
#             print(no_relation_word_list)
            f22.write(lemma+'\t'+'Norelation'+'\t'+candidate1_word+'\n')
            f22.write(lemma+'\t'+'Norelation'+'\t'+candidate2_word+'\n')
            f22.write(lemma+'\t'+'Norelation'+'\t'+candidate3_word+'\n')
            
            
            

        except:
            break



import os
import urllib.request
import matplotlib.pyplot as plt
from scipy import spatial
from sklearn.manifold import TSNE
import numpy as np

emmbed_dict_glove = {}
glove_word = []
with open('/content/drive/MyDrive/embedding/glove.6B.300d.txt','r') as f:
  for line in f:
    values = line.split()
    word = values[0]
    glove_word.append(word)
    vector = np.asarray(values[1:],'float32')
    emmbed_dict_glove[word]=vector

# file_out = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/glove_filter_syn_other_relation.txt','w')
lines = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_other_relation.txt", "rb").readlines()
lines = [line.decode(encoding="utf-8").strip() for line in lines]
other_relation_word_all = []
for line in lines:
    all_items = line.split("\t")
    word1 = all_items[0]
    word2 = all_items[2]
    other_relation_word_all.append(word1)
    other_relation_word_all.append(word2)
    # if word1 in glove_word and word2 in glove_word and len(word1) >1 and len(word2) >2:
    #   file_out.write(line+'\n')

lines1 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_no_relation.txt", "rb").readlines()
lines1 = [line1.decode(encoding="utf-8").strip() for line1 in lines1]
no_relation_word_all = []
for line1 in lines1:
    all_items1 = line1.split("\t")
    word11 = all_items1[0]
    word21 = all_items1[2]
    no_relation_word_all.append(word11)
    no_relation_word_all.append(word21)

lines2 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_relation_noun.txt", "rb").readlines()
lines2 = [line2.decode(encoding="utf-8").strip() for line2 in lines2]
syn_relation_word_all = []
for line2 in lines2:
    all_items2 = line2.split("\t")
    word21 = all_items2[0]
    word22 = all_items2[2]
    syn_relation_word_all.append(word21)
    syn_relation_word_all.append(word22)

find_all_common = set(glove_word).intersection(other_relation_word_all, no_relation_word_all,syn_relation_word_all)

print(find_all_common)
print(len(find_all_common))

file_out = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_other_relation.txt','w')
lines = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_other_relation.txt", "rb").readlines()
lines = [line.decode(encoding="utf-8").strip() for line in lines]
# other_relation_word_all = []
for line in lines:
    all_items = line.split("\t")
    word1 = all_items[0]
    word2 = all_items[2]
    # other_relation_word_all.append(word1)
    # other_relation_word_all.append(word2)
    if word1 in find_all_common and word2 in find_all_common and len(word1) >2 and len(word2) >2:
      file_out.write(word1+' '+word2+'\t'+'0'+'\n')
      file_out.write(word2+' '+word1+'\t'+'0'+'\n')

file_out1 = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_no_relation.txt','w')
lines1 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_no_relation.txt", "rb").readlines()
lines1 = [line1.decode(encoding="utf-8").strip() for line1 in lines1]
# no_relation_word_all = []
for line1 in lines1:
    all_items1 = line1.split("\t")
    word11 = all_items1[0]
    word21 = all_items1[2]
    # no_relation_word_all.append(word11)
    # no_relation_word_all.append(word21)
    if word11 in find_all_common and word21 in find_all_common and len(word11) >2 and len(word21) >2:
      # print(word11+' '+word21+'\t'+'0')
      file_out1.write(word11+' '+word21+'\t'+'0'+'\n')
      file_out1.write(word21+' '+word11+'\t'+'0'+'\n')

file_out2 = open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_relation.txt','w')
lines2 = open("/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/syn_relation_noun.txt", "rb").readlines()
lines2 = [line2.decode(encoding="utf-8").strip() for line2 in lines2]
# syn_relation_word_all = []
for line2 in lines2:
    all_items2 = line2.split("\t")
    word21 = all_items2[0]
    word22 = all_items2[2]
    # syn_relation_word_all.append(word2)
    # syn_relation_word_all.append(word2)
    if word21 in find_all_common and word22 in find_all_common and len(word21) >2 and len(word22) >2:
      # print(word11+' '+word21+'\t'+'0')
      file_out2.write(word21+' '+word22+'\t'+'1'+'\n')
      file_out2.write(word22+' '+word21+'\t'+'1'+'\n')

import random
with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_no_relation.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/shuffle_filter_double_syn_no_relation.txt','w') as target:
    for _, line in data:
        target.write( line )

with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_other_relation.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/shuffle_filter_double_syn_other_relation.txt','w') as target:
    for _, line in data:
        target.write( line )

with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/filter_double_syn_relation.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/shuffle_filter_double_syn_relation.txt','w') as target:
    for _, line in data:
        target.write( line )

with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/shuffle_filter_double_all.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('/content/drive/MyDrive/wordshape4run/syn_model/generate_data4model_trainning/shuffle_shuffle_filter_double_all.txt','w') as target:
    for _, line in data:
        target.write( line )

#intotal 247115 pairs

