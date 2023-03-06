# Data introduction

Files under this folder show the process of generating data for model training. The data pairs contains three types of relations: synonym, other relations, and no relations.

# synonym

All the pairs are extracted from wordnet(synonym.csv). We only use nouns here. All results are stored in synonym_relation_noun.txt

# Other relations

All word pairs are from wordnet (taking advatange of data.noun and noun.index). All results are stored in syn_other_relation.txt

# No relations

The two words to form a word pair are both randomly slected in a intersection set among synonym set, other-relation sets, and GloVe word embeddings.



