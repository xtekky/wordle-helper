words = []
letter="a"
position=1
wordlist=[]
with open('words.txt') as w:
  words = w.readlines()

while letter!='':
  del wordlist[:]
  letter=input("What letter do you know? ")
  color=input("What color is it? (Y,G,B): ")
  if color == 'g' or color == 'G' or color == 'y' or color == 'Y':
    position=int(input("What position is it? (1-5)"))-1
  for word in words:
    if color == 'g' or color == 'G':
      if word[position]==letter:
        wordlist.append(word)
    elif color == 'b' or color == 'B':
      if letter not in word:
        wordlist.append(word)
    elif color == 'y' or color == 'Y':
      if letter in word:
        if word[position]!=letter:
          wordlist.append(word)
  words=wordlist.copy()
  print(*wordlist)
