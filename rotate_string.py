############################################################
# for conversion to ascii use functons ord and chr
#   ex : ord("a")
#        chr(99)
#   ascii range for a-z(97-122)
#
#
#############################################################



word =(input("enter your string:"))
index = 0


#def rotate():
   # while index < len(word):
         #tmp = word[0]
        # print (tmp)
         #break
        # ord(tmp) = tmp1
         #tmp2 = tmp1 + 3
         #chr(tmp2) = tmp3
         #print(tmp3)
i = 0     
for letter in word:
    
    tmp = word[i]
    #print (tmp) 
    tmp1 = ord(tmp)
    #print (tmp1)
    tmp2 = tmp1 + 3
    #print (tmp2)
    tmp3 = chr(tmp2)
    print(tmp3) 
    i = i+1      
