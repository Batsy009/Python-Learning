# 20. Count the Number of Vowels.
# Using Dictionary
print("\nUsing Only Dictionary\n")
vowels = 'aeiou'

sen =input("\nEnter the sentence here : ")
sen = sen.casefold()

count = {}.fromkeys(vowels, 0)

for char in sen:
    if char in count:
        count[char] += 1
print(count)

# Using List and Dictionary Comprehension
print("\nUsing List and Dictionary Comprehension\n")

sen =input("\nEnter the sentence here : ")
sen = sen.casefold()

count = {x : sum([1 for char in sen if char == x]) for x in 'aeiou'}
print(count)
