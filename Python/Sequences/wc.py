# my own version of wc

lines = 0
words = 0
chars = 0

infileName = input("Input the filename: ")
infile = open(infileName, "r")

for line in infile:
    lines += line.count("\n")
    words += line.count(" ")
    chars += len(line)

print("Lines: ", lines)
print("Word:  ", words)
print("Chars: ", chars)