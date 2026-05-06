file = open("demo.txt")

print(file.read())

with open("demo.txt", "a") as f :
    f.write("testing writing capabilities")

with open("demo.txt") as f :
    print(f.read())