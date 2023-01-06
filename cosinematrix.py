def get_close_cos_sim_list(target_word):
  u = emmbed_dict[target_word] 
  v = all_x
  
  w = np.array([u.dot(v[i])/(np.linalg.norm(u)*np.linalg.norm(v[i])) for i in range(len(all_hist_word))])
  return w

cosine_all= []
for inlist in new_matrix:
  cosine_all.append(get_close_cos_sim_list(inlist))
