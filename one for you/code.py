
while True:
    name =  input("Name: ")
    if name == "" or name==" ":
        print("one for you, one for me")
        raise Exception("meaningful message required, you need to put a name")
    else:
        print(f"{name}   :  one for {name}, one for me")