'''
    Pythonic Coding Style
'''
# join() method : list -> str
colors = ['red', 'yellow', 'green']
result = ''.join(colors)
print(result)
result = '/'.join(colors)
print(result)

# split() method : srt -> list
lang_str = 'python,java,c#,scalar'
result = lang_str.split(',')
print(type(result), result)

# split() method : srt -> list
lang_str = 'python java c# scalar'
result = lang_str.split()
print(type(result), result)

# List Comprehension
# for + append
my_list = []
for val in range(10):
    if val % 2 == 0: # multiple of 2
        my_list.append(val)
print(my_list)

# List Comprehension
my_list2 = [i for i in range(10) if i % 2 == 0]
print(my_list2)

my_list3 = [i if i % 2 == 0 else 10 for i in range(10)]
print(my_list3)

# String type List Comprehension
word1 = 'Hello'
word2 = 'World'
my_list_str = [i + j for i in word1 for j in word2]
print(my_list_str)

words = 'Yesterday, all my troubles seemed so far away'.split()
word_lists = []
for w in words:
    word_list = [w.upper(), w.lower(), len(w)]
    word_lists.append(word_list)

print(word_lists)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

# enumerate() method : return index value
for idx, val in enumerate(words, 1): # 1 -> index 1 ~
    print(f'index  = {idx}, value = {val}')

print(enumerate(words)) # return object
print(list(enumerate(words)))

# Dict Comprehension
word_dict = {idx: val for idx, val in enumerate(words)}
print(word_dict)

word_dict = {idx: val.capitalize() for idx, val in enumerate(words, 1)}
print(word_dict)

# Variable Exchange
a = 10
b = 20

a, b = b, a
print(a, b)

# Sequence unpacking
a, *rest = [1, 2, 3]
print(type(a), a)
print(type(rest), rest)

a, *rest, c = [1, 2, 3, 4]
print(type(a), a)
print(type(rest), rest)
print(type(c), c)

# zip()
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300)):
    print(val)

# [111, 222, 333]
sum_list = [sum(val) for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(sum_list)