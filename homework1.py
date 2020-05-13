def stringManipulation(file):
    file = open(file)
    modifiedWords = []   
    for line in file.readlines():

      line=line.replace('-',' ')
      cleanedLine = line.strip() 
      words = cleanedLine.split()
      
      for word in words:
          word=''.join(e for e in word if e.isalnum())
          word = word.strip(string.punctuation+string.whitespace)       
          word=word.lower()
          modifiedWords = modifiedWords + [word] 
    return modifiedWords 

lst=stringManipulation('book.txt')
file2=stringManipulation('words.txt')
a=[]
for i in lst:
  if i not in file2:
    a.append(i)
print(set(a))

