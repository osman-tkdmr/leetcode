def reverse_words(words):
    
    reverseWords = []
    words = words.split(' ')
    for word in words:
        reverseWord = []
        for i in word[::-1]:
            reverseWord.append(i)
        reverseWords.append(''.join(reverseWord))
    return (' '.join(reverseWords))

    #return ' '.join(word[::-1] for word in s.split()) more easily


print(reverse_words('word of list to revverse enter'))