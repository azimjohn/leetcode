def isAlienSorted(words, rder):
    orders = {l: i for i, l in enumerate(order)}
    prev_word_val = ()

    for word in words:
        word_val = tuple([orders[l] for l in word])
        if prev_word_val > word_val:
            return False
        prev_word_val = word_val

    return True
