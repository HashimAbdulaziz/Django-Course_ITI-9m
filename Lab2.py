# Task 1
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ")

for letter in word:
   if letter.lower() in vowels:
      word = word.replace(letter, "")

print("Word without vowels: " + word)

# Task 2
str = input("Enter a string: ")
c = input("Enter a character: ")
indx = []
for i in range(len(str)):
    if str[i] == c:
        indx.append(i)
print(indx) 


# Task 3
n = int(input("Enter a number: "))
mult = []

for i in range(1, n + 1):
   numMult = []
   for j in range(1, i + 1):
      numMult.append(i * j)
   
   mult.append(numMult)

print(mult)

# Task 4
def getArea(*args):
   if args[0] == 't':
      return 0.5 * args[1] * args[2]
   elif args[0] == 'r':
      return args[1] * args[2]
   elif args[0] == 'c':
      return 3.14 * args[1] ** 2
   elif args[0] == 's':
      return args[1] ** 2
   else:
      return "Invalid: type (t, r, c, or s)"

# Task 5
words = input("Enter a sentence: ").split()
words.sort(key=str.lower) 
dictionary = [{}]

for word in words:
   dictionary.append({word[0]: word})

print(dictionary)

# Task 6
n = int(input("Enter a number: "))
for i in range(1, n + 1):
   print(" " * (n - i) + "*" * i)
   