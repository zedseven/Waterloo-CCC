word = input("")

largestPalindrome = 0
palindromes = []

if len(word) > 1:
    
    for letter in range(len(word) - 1):
        done = False
        loopIndex = -1
        palindrome = ""
        while done == False:
            loopIndex += 1
            if len(word) >= (loopIndex * 2 + 2):
                #print(len(word))
##                print(letter)
##                print(loopIndex)
##                print(len(word) - (loopIndex + 1))
##                print("--------")
                if word[letter + loopIndex] == word[len(word) - (loopIndex + 1)]:
                    palindrome += word[letter+loopIndex:len(word) - (loopIndex + 1)]
                elif word[letter + loopIndex] == word[len(word) - (loopIndex + 2)]:
                    done = True
            elif (len(word) - (loopIndex * 2 + 2) - 3) == 1:#>= ((loopIndex * 2 + 2) - 1):
                palindrome += word[letter+loopIndex:len(word) - (loopIndex + 1)]
                #print("only one letter nao")
            else:
                palindromes.append(palindrome)
                done = True

    for i in range(len(palindromes)):
        palindromes[i] = len(palindromes[i])
    palindromes = sorted(palindromes, reverse = True)
    #print(palindromes)
    print(palindromes[len(palindromes) - 1])
else:
    print(1)
