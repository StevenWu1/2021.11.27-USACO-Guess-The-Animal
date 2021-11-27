import random
animal = {'bird': ['flies', 'eatsworms'],
'cow': ['eatsgrass', 'isawesome'],
'sheep': ['eatsgrass', 'goesmoo'],
'goat': ['makesmilk', 'eatsgrass']}

randomanimal = random.choice(dict(enumerate(animal)))
print(randomanimal)
guess = ""
attributes = animal[randomanimal]
print(attributes)

print(animal.keys())

while guess != randomanimal:
    if guess in attributes:
        print ("yes")
    elif guess in animal.keys():
        print ("Try Again")
    elif guess != "":
        print ("no")

    guess = input('what animal am I thinking of?')
    
print("You Win")
