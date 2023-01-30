lines2 = open("/content/drive/MyDrive/syn/synonyms.csv", "rb").readlines()
lines2 = [line2.decode(encoding="utf-8", errors='ignore').strip() for line2 in lines2]
noun_dict = {}
for line2 in lines2:
  all = line2.split(',')
  if all[1] =='noun':
    noun_dict[all[0]] = all[2]  


def return_synonyms(word): 

    return_syn = []

    if word in noun_dict.keys():
      all_syns = noun_dict[word]
      synonyms = all_syns.split(';')
      for each in synonyms:
        if each in nodup_hist_lemmas:
          return_syn.append(each)

    return(set(return_syn))

  
all_append= []
large_find_syn = []
large_dict = {}
for node1 in nodup_hist_lemmas:
  small_find = [node1]
  large_dict[node1] = [node1]
  synset = return_synonyms(node1)
  for node2 in nodup_hist_lemmas:
    if node2 in synset:
      if node2 != node1:
        small_find.append(node2)
        large_dict[node1].append(node2)      
  
  large_find_syn.append(small_find)
