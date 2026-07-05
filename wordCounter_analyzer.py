paragraph = input("Enter a paragraph: ")

words = paragraph.split()

print("Total Words:", len(words))

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)

vowels = "aeiouAEIOU"
count = 0

for ch in paragraph:
    if ch in vowels:
        count += 1

print("Total Vowels:", count)