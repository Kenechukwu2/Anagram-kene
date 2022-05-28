# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if (sorted(word) == sorted (anagram)):
        answer = True
    else:
        answer = False
        print (answer)
        
        str1 = input ("Type in the First word")
        str2 = input ("Type in the Second word")

    return True

