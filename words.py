import random


def get_random_word(min_word_length):
    """Get a random word from the word.txt using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open('words.txt', 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word
