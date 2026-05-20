# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\n We are learning file I/O\n")
#     f.write("using java.\n I like programming in java.")
# with open("practice.txt", "r") as f:
#     data = f.read()
#     new = data.replace("java","python")
#     print(new)
# with open("practice.txt", "w") as f:
#     data = f.write(new)
def check_word():
    word="writing"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
check_word()