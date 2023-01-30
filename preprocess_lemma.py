lines = open("/content/drive/MyDrive/COHA/wlp_acad_1950.txt", "rb").readlines()
lines = [line.decode(encoding="utf-8", errors='ignore').strip() for line in lines]
coha_lemma = []
coha_lemma_dict = {}
for line in lines:
  all_items = line1.split('	')
  if len(all_items) == 4:
    # if all_items[3].startswith('nn'):
      if all_items[2] not in coha_lemma_dict.keys():
        coha_lemma.append(all_items[2])
        coha_lemma_dict[all_items[2]]=[all_items[3]]
      else:
        coha_lemma.append(all_items[2])
        coha_lemma_dict[all_items[2]].append(all_items[3])
        
filter_nn = []
for each_lemma in coha_lemma_dict.keys():
  current_list = coha_lemma_dict[each_lemma] 
  if 'nn' in Counter(current_list).most_common(1)[0][0]:
    filter_nn.append(each_lemma)
    
nodup_hist_lemmas = []
for ww in filter_nn:
  if ww not in nodup_hist_lemmas and ww in all_hist_word:
    nodup_hist_lemmas.append(ww)
# print(nodup_hist_lemmas)
print(len(nodup_hist_lemmas))
