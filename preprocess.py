def process_text(filename):

    # read the text
    file1 = open (filename,"r", encoding="utf-8", errors = 'ignore')
    print(file1)
    # file1 = open (filename,"r")
    text1 = file1.read()
    file1.close()

    # convert text to words and process
    tokens = word_tokenize(text1)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)        
    stripped = [w.translate(table) for w in tokens]          
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    return words
  
 def pos_process(words):
    wnl = WordNetLemmatizer()
    
    lemmas = []
    for word in words:
      if get_wordnet_pos(word) == 'n' and len(word) > 2:
        lemmas.append(wnl.lemmatize(word,get_wordnet_pos(word)))

    return lemmas 
  
    
  
filename1='/content/drive/MyDrive/COHA/coha-text/text_acad_1860.txt'
hist_lemmas = process_text(filename1)
pos_lemmas = pos_process(hist_lemmas)
nodup_hist_lemmas = []
for ww in pos_lemmas:
  if ww not in nodup_hist_lemmas:
    nodup_hist_lemmas.append(ww)
print(len(nodup_hist_lemmas))
