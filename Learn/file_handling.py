content = open('/Users/anurag/Downloads/Python /Learn/text.txt', 'a')

print(content.write('I am using the file in append mode.'))

content.close()

content=open('/Users/anurag/Downloads/Python /Learn/text.txt', 'r')
print(content.read())
content.close()

content = open('')
