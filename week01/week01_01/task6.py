def count_vowels(n):
    cv = 0
    n = n.lower()
    for x in n:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y":
            cv += 1
    return cv


# count_vowels("Python")

# count_vowels("Theistareykjarbunga")

# count_vowels("grrrrgh!")

# count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")

# count_vowels("A nice day to code!")
