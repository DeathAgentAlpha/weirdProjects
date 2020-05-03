import random

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    randomWord = ""
    randomInt = random.randrange(0,len(english_words))
    counter = 0
    for x in english_words:
        if(counter == randomInt):
            randomWord = x
            break
        counter+=1
    print (randomWord)