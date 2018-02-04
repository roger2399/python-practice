def is_pallindrome(word):
    i = 0
    j = len(word)-1
    
    for letter in word:
        if word[i] != word[j]:
           print ("word is not pallindrome")
        else:
           print ("word is pallnidrome")
