##########################################################
#                                                        #
#    EXERCISE 9.1 READS A FILE AND PRINT WORDS WITH 	 #
#             MORE THAN 20 CHARACTERS			 #
#							 #
##########################################################
fin = open("words.txt")
line = fin.readline()
for line in fin:
    #line =fin.readline()
    word = line.strip()
    if len(word) > 20:
        print (word)


















