def anagrams(word, array):
    total = []
    word = sorted(word)
    for row in array:
        if sorted(row) == word:
            total.append(row)
    return total

if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    print(anagrams('laser', ['lazing', 'lazy',  'lacer']))