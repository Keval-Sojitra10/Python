with open("practice.txt", "r") as f:
    data = f.read()
    new = data.replace("java","python")
    print(new)