def get_close_cos_sim_list(target_word):
  if target_word in emmbed_dict:
    u = emmbed_dict[target_word] 
    v = all_x
    w = np.array([u.dot(v[i])/(np.linalg.norm(u)*np.linalg.norm(v[i])) for i in range(len(all_hist_word))])
    cos_list = []
    n = 0
    for i in w:
      cos_list.append([all_hist_word[n],i])
      n = n+1
    cos_lis = Sort(cos_list)
    return_cos_syn = []
    for x in cos_lis[:30]:
      return_cos_syn.append(x[0])
    return return_cos_syn
  
  
  
  def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1] ,reverse = True)
    return sub_li
  
    
  def cosine_similarity(a, b):
    nominator = np.dot(a, b)
    
    a_norm = np.sqrt(np.sum(a**2))
    b_norm = np.sqrt(np.sum(b**2))
    
    denominator = a_norm * b_norm
    cosine_similarity = nominator / denominator
    
    return cosine_similarity
  
expand_valid = []
for v in large_dict.keys(): ### v is the center(key) of each small syn cluster
  if v in emmbed_dict.keys():
    sum_cos = []
    distance = []
    for each_syn in large_dict[v]:
      each_cos = emmbed_dict[each_syn]
      sum_cos.append(each_cos)
      center_dis =  emmbed_dict[v]
      each_dis = emmbed_dict[each_syn]
      dist = numpy.linalg.norm(center_dis-each_dis)
      distance.append(dist)
    mean_cos = sum(sum_cos)/len(large_dict[v]) ###calcuate the mean vector of each small syn cluster
    max_dis = max(distance)
    min_dis = min(distance) ###max and min diatances beween all elements and the center(key)
 
    cos_candi = list(set(get_close_cos_sim_list(v)[:10]) - set(return_synonyms(v))) ### find ungrouped word
    
    for u in cos_candi: ## u is each individual candiate waiting to be added
      if u in emmbed_dict.keys():
        candi_u = emmbed_dict[u]
        center_v = emmbed_dict[v]
        input_string = [u+' '+v]
        cos = cosine_similarity(mean_cos,candi_u)  ##cosine similarity between candidate u and the mean vector 
        candi_dis = numpy.linalg.norm(center_dis-candi_u)  #distance beween candidate u and the center(key)
        candi_distance = []
        
        if  dist2 < max_dis and cos > 0.8: ##condition
            if v not in large_dict[u]:
              large_dict[u].append(v)
              expand_valid.append([input_string])
              print(input_string)
      
