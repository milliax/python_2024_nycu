s1 = 'How do you do who are you'
s2 = 'What do you think how are you' # just for example

""" to find the duplicated words in s1 and s2 """

# split the strings into lists

s1_list = s1.split()
s2_list = s2.split()

# find the duplicated words in s1 and s2

duplicated_words = set(s1_list) & set(s2_list)

print(duplicated_words)