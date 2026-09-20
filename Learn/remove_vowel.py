text = input("Enter a text: ")

# text=text.lower()
result = ""
for t in text:
    if t in "aeiouAEIOU":
        continue
    else:
        pass
    result+=t
    
print("The text without vowel: ", result)
    