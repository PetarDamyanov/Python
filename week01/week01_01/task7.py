from task6 import count_vowels


def count_consonants(n):
    cv = 0
    n = n.lower()
    n = n.replace(" ", "")
    for x in n:
        if not count_vowels(x) and x.isalpha():
            cv += 1
    return cv

# count_vowels("Python")

# count_vowels("Theistareykjarbunga") #It's a volcano name!

# count_vowels("grrrrgh!")

# count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")

# count_vowels("A nice day to code!")
