from collections import Counter
word1 = "cabbba"
word2 = "abbccc"

def twoStringsClose(word1, word2):
    if len(word1) != len(word2):
        return False
    freq1 = Counter(word1)
    freq2 = Counter(word2)
    
    print(freq1)
    print(freq2)
    
    return sorted(freq1.values()) == sorted(freq2.values())

print("twoStringsClose: ", twoStringsClose(word1, word2))