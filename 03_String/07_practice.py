# Write a Python function to check if a string is a palindrome.
def is_palindrome(s):
    return s==s[::-1]

s = "racecar"
print(f"{s} is palindrome!") if is_palindrome(s) else print(f"{s} is not palindrome")

# chekc anagram
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1,s2 = "master", "termas"
print(anagram(s1,s2))

#  reverse words in a given string?
s = "my name is khan"
reversed_words = " ".join(word[::-1] for word in s.split())
print(reversed_words)

# count the occurrences of a specific character in a string.
def count_occurance(s, char):
    return s.count(char)
s = "zaid alif"
print(count_occurance(s,"i"))


print(list("zaid"))

# remove duplicate character in a string
def remove_duplicate(s):
    return "".join(sorted(set(s), key=s.index))

print(remove_duplicate("zaaaid"))



# refer: https://medium.com/@mohsin.shaikh324/50-interview-questions-on-python-strings-a3057af7cd2d