# coding=utf-8
# this script calculates previous / following informativity for a set of target words
# across a range of decades based on the google ngrams corpus
#
# this is done by reading in *every* line from the google ngrams bigram corpus for 
# english, and updating a set of metrics if the line contains relevant information
#
# to give an example: let's say the current line in the google ngrams corpus is
#
# go home   1967    6547812
#
# i.e. the bigram "go home" has a frequency of 6547812 in 1967. let's say "home" is
# a target word, but "go" is not. in this case, the previous informativity of "home"
# (i.e. informativity based on the previous word) in the 1960s will be updated by 
# using the predictabilities of "home" from previous "go" in the 1960s.
# this predictability is defined as 
# 
# p(W_D | C_D) =  p(W_D,C_D) / p(C_D)
#
# p(W_D,C_D) is simply the sum of the figures in the third column, so 6547812 will be
# one part of this sum (the rest will come from the remaining 9 years of the 1960s). 
# P(C_D) is the sum of the unigram frequencies of "go" in the 10 years of the 1960s, 
# which is extracted efficiently from a separate unigram frequency data set.
#
# these by-decade predictability figures are used to update two weighted sums that
# represent the previous and following informativity of a given word in a given
# decade. once all the 2gram files are read in, the final weighted sums are the
# informativity figures.

# START OF SCRIPT
from __future__ import division
from string import uppercase
from math import log, exp
from time import time
import gzip
import cPickle
import os.path
import sys

# google ngrams has _START_ for start of sentence, and allegedly _END_ as well
# I'm not sure why I decided to treat _END_ differently here, but these symbols
# are used to identify the following context as the end of a sentence
ends = ["!", ":", ".", ")", "...", "?", ";"]

# the list of all google 2gram files to use – though all of the files are downloaded,
# some of them (e.g. the ones with POS tags instead of specific words) are not used
f = open("/home/changbing/word_change/data/2gram/gzs")
filelist = ["/home/changbing/word_change/data/2gram/" + x.strip() for x in f.readlines()]
f.close()

# the files that contain unigram frequencies; these are in small ~10 MB chunks
# for reasons of efficiency
#
# the last two chunks are _START_ and _END_
paths_to_uni = ["/home/changbing/word_change/data/chunks/" + str(x) for x in range(1658)]

# an index file that contains the start locations of every word in the google
# unigram corpus in the unigram chunks; I think _START_ and _END_ were manually 
# assembled, because they weren't included in the original unigram frequency 
# dictionary
f = open("/home/changbing/word_change/data/index_dic.pickle", "rb")
index_dic = cPickle.load(f)
index_dic["_START_"] = ('1656', 0)
index_dic["_END_"] = ('1657', 0)
f.close()

# these are the output files
out_prev_info = "/home/changbing/word_change/data/out_prev_info.pickle"
out_foll_info = "/home/changbing/word_change/data/out_foll_info.pickle"

# the target words (all the Ws)
f = open("/home/changbing/word_change/data/targets.csv")
targets = [x.strip() for x in f.readlines()]
f.close()

# what range of dates to look at
year_min = 1850
year_max = 1990

# setting up the dictionaries that represent the output files
# the structure is
# {W_1: {1850: [0,0], 1860: [0,0], ...}, W_2: {...}}
# where the Ws are the target words, and the [0,0]'s represent 
# the summed surprisals and weights that can be used to calculate
# the weighted average corresponding to informativity
target_dic_prev = {}
target_dic_foll = {}
for row in targets:
	target_dic_prev[row] = dict(zip(map(str,range(year_min,year_max,10)), [[0,0] for x in range(15)]))
	target_dic_foll[row] = dict(zip(map(str,range(year_min,year_max,10)), [[0,0] for x in range(15)]))

# for reasons of efficiency, this unigram output dictionary is
# created outside the get_unigram_freqs function
out_dic_proto = zip(map(str,range(year_min,year_max,10)), [0]*15)

# obtain a dictionary that contains the unigram frequency of
# context C in each decade under investigation
#
# this needs to be done many thousands of times, so doing this 
# efficiently using the chunks + address index that are loaded
# at the beginning
def get_unigram_freqs (word):
	address = index_dic[word]
	f_uni = open(paths_to_uni[int(address[0])])
	f_uni.seek(address[1])
	out_dic = dict(out_dic_proto)
	while True:
		line = f_uni.readline().split('\t')
		if line == ['']:
			break
		elif line[0] == word:
			if int(line[1]) >= year_min and int(line[1]) < year_max:
				out_dic[line[1][0:3] + '0'] += int(line[2])
		else:
			break
	f_uni.close()
	return out_dic

# updating target_dic_prev and target_dic_foll using the information
# from the current line
#
# this is a horrible function that reads and writes info to/from global
# variables...
def write_out ():
	global target_dic_prev, target_dic_foll
    # if the current bigram has a target word as W1, update following
    # informativity metrics
	if curr_sides[0]:
        # P(W_D,C_D) / p(C_D)
		prob = log(curr_count) - log(word_2_freqs[curr_year])
        # m = weighted average of surprisal
        # all_counts = summed weights (counts) so far
        # retrieving old values
		m, all_counts = target_dic_foll[words[0]][curr_year]
        # updating weighted average (based on some algebra)
		target_dic_foll[words[0]][curr_year][0] += (curr_count / (all_counts + curr_count)) * (prob - m)
		target_dic_foll[words[0]][curr_year][1] += curr_count
    # same: if the current bigram has a target word as W2, update following
    # informativity metrics
	if curr_sides[1]:
		prob = log(curr_count) - log(word_1_freqs[curr_year])
		m, all_counts = target_dic_prev[words[1]][curr_year]
		target_dic_prev[words[1]][curr_year][0] += (curr_count / (all_counts + curr_count)) * (prob - m)
		target_dic_prev[words[1]][curr_year][1] += curr_count

# main loop: going through all google 2gram files!
for fname in filelist:
	a = time()
    # unzip file
	to_open = os.path.splitext(fname)[0]
	if not os.path.exists(to_open):
		print("unzipping " + os.path.split(fname)[1] + "...")
		cmd = "gzip -k -d " + fname
		os.system(cmd)
    # now read through file
	print("processing " + os.path.split(to_open)[1] + "...")
	f_in = open(to_open, 'r')
    # c: line counter
	c = 0
    # curr_pair: current bigram
    # curr_sides: which side(s) of the bigram have a target word
	curr_pair = ''
	curr_sides = [False, False]
    # seek through file...
	while True:
        # read next line
        # data structure:
        # word1 word2   year    frequency
        # a book    1780    19876123
        # a book    1781    18716221
        # a book    1782    26712931
        # (note: word1 and word2 are separated by spaces;
        # but there are \t's before year and frequency)
		line = f_in.readline().split("\t")
        # if end of file:
		if line == ['']:
            # if w1 or w2 for the previous bigram is a target,
            # update informativity metrics
			if True in curr_sides:
				write_out()
			break
        # status report (not sure why I used file.tell() here... I guess this is 
        # meant to be MB's? but I don't know if it really is)
		if c % 100000 == 0:
			sys.stdout.write(str(int(f_in.tell() / 1000000)) + "\r")
    		sys.stdout.flush()
        # only consider the line if it's within the relevant year range
		if int(line[1]) >= year_min and int(line[1]) < year_max:
            # if it's a new bigram (not the same bigram at a different year)
			if line[0] != curr_pair:
                # if w1 or w2 for the previous bigram is a target,
                # update informativity metrics
				if True in curr_sides:
					write_out()
                # curr_pair <- bigram
				curr_pair = line[0]
				words = line[0].split(" ")
                # if w1 is the _START_ symbol
				if words[0] == "_START_":
                    # if the next word starts with a capital letter,
                    # check if it's among the targets
					if words[1][0] in uppercase:
						curr_sides = [False, words[1] in targets or words[1].lower() in targets]
                        # change to lowercase
						if words[1].lower() in targets and curr_sides[1]:
							words[1] = words[1].lower()
                    # if the next word does not start with a capital letter,
                    # dismiss bigram (i.e. sentence-initial words should be capitalised)
					else:
						curr_sides = [False, False]
				# which of w1 and w2 are targets?
				else:
					curr_sides = [words[0] in targets, words[1] in targets]
                # if the context has a _ (except _START_) or is not in the unigram data set
                # (i.e. filter out rubbish)
				if curr_sides[0]:
					if "_" in words[1] or words[1] not in index_dic:
						curr_sides[0] = False
				if curr_sides[1]:
					if ("_" in words[0] and words[0] != "_START_") or words[0] not in index_dic:
						curr_sides[1] = False
                # if we have a target word...
				if True in curr_sides:
                    # look at decade instead of year
					curr_year = line[1][0:3] + '0'
                    # start bigram freq counter
                    # (bear in mind, this is still initialising a new
                    # bigram!)
					curr_count = 0
                    # if target word is w1
					if curr_sides[0]:
                        # replace punctuation with _END_
						if words[1] in ends:
							words[1] = "_END_"
                        # w2 to lowercase
						word_2_lower = words[1].lower()
                        # what's P(C) in the relevant decade?
						word_2_freqs = get_unigram_freqs(words[1])
                    # same for w2
					if curr_sides[1]:
						word_1_lower = words[0].lower()
						word_1_freqs = get_unigram_freqs(words[0])
                # end of initialisation for new bigram
            # if current bigram has a target word...
			if True in curr_sides:
                # if new decade, update info stats
				if line[1][0:3] + '0' != curr_year:
					write_out()
					curr_year = line[1][0:3] + '0'
					curr_count = 0
                # update bigram frequency count
				curr_count += int(line[2])
		c += 1
    # close & remove file
	f_in.close()
	cmd = "rm " + to_open
	os.system(cmd)
    # update output pickles
	f_out = open(out_prev_info, 'wb')
	cPickle.dump(target_dic_prev, f_out, protocol=-1)
	f_out.close()
	f_out = open(out_foll_info, 'wb')
	cPickle.dump(target_dic_foll, f_out, protocol=-1)
	f_out.close()
	print("took " + str(time() - a) + " seconds")
