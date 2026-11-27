def count_words(sentence):
    words = sentence.lower().split()

    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count



print(count_words("The cat and the dog and the bird"))