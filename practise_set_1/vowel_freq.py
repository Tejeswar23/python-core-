sentence = input("Enter a Sentence: ")
new_sentence = sentence.lower()
count = 0
for i in new_sentence :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        count+=1
print(count)
