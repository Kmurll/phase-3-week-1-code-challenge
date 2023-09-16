import string

def word_frequency(sentence):
    # Remove punctuation and split the sentence into words
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word in a case-insensitive manner
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Test case 1
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
# Output {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}

# Test case 2
sentence1 = "How are you, my name is Kelvin. I enjoy coding."
result1 = word_frequency(sentence1)
print(result1)
# Output: {'how': 1, 'are': 1, 'you': 1, 'my': 1, 'name': 1, 'is': 1, 'kelvin': 1, 'i': 1, 'enjoy': 1, 'coding': 1}

# Test case 3
sentence2 = "She sells seashells by the seashore. The seashells she sells are surely seashells."
result2 = word_frequency(sentence2)
print(result2)
# Output: {'she': 2, 'sells': 2, 'seashells': 3, 'by': 1, 'the': 1, 'seashore': 1, 'are': 1, 'surely': 1}

# Test case 4
sentence3 = "Programming is fun, and Python programming is even more fun!"
result3 = word_frequency(sentence3)
print(result3)
# Output: {'programming': 2, 'is': 2, 'fun': 2, 'and': 1, 'python': 1, 'even': 1, 'more': 1}


# Test case 5
sentence5 = ""
result5 = word_frequency(sentence5)
print(result5)
# Output: {} (empty input sentence)
