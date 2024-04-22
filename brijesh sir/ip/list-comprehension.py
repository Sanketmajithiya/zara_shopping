

# print([(word, len(word)) for word in input("Enter your name: ").strip().split(' ') if len(word) % 2 != 0])

print([{word:len(word)} for word in input("Enter your name: ").strip().split(' ') if len(word) % 2 != 0])
