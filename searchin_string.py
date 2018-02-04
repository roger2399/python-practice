def find(word,letter):
    index = 0
    counter = 0
    while len(word) > index:
          if word[index] == letter:
             counter += 1
             print (counter)
            # return index
             index += 1
    return -1
