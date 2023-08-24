text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."
split_text = text.split()

find = input()
replace = input()

count = 0

for i in split_text:
  if find in i:
    text = text.replace(find, replace)
    count = count + 1


print(count)
print(text)

  # print(i)

# if find in text:
#     found = text.replace(find, replace)
#     count = count + 1