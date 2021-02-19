import random

def karinafier(l):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print(random.choice(alpha))
    splitList = l.split()
    randomSentence = ''
    for word in splitList:
        someRandInt = random.randint(1,4)
        randomLetter = random.choice(alpha)
        if someRandInt == 4:
            randomWords = word + randomLetter
            print("randomWords is: ", randomWords)
        else:
            randomWords = word
            print(randomSentence)
        randomSentence += randomWords + " "
    print(randomSentence)
if __name__ == '__main__':
    l = input("Say something: ")
    karinafier(l)