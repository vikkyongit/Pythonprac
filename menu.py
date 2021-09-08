d={}
def create_dict():
    global d
    d={}
    ch='y'
    while ch=='y' or ch=='Y':
        print("Enter word: ")
        word=input()
        print("\n Enter meaning: ")
        meaning=input()
        d[word]=meaning
        print("Do you want to continue? y/n")
        ch=input()
def add_word():
    global d
    print("Enter word: ")
    word=input()
    print("\n Enter meaning: ")
    meaning=input()
    d[word]=meaning
def find_meaning(w):
    return d[w]
def disp_sorted():
    for w,m in d.items():
        print(f"{w}==>{m}")
    print("sorted list of words: ")
    print(sorted(d.keys()))
def main():
    ch="y"
    while ch=='y' or ch=='Y':
        print("1: Create dictionary")
        print("2: Add new word")
        print("3: find meaning")
        print("4: display sorted list of words")
        print("5: quit")
        print("Enter choice")
        opt=int(input("Enter option"))
        if opt==1:
            create_dict()
        elif opt==2:
            add_word()
        elif opt==3:
            print("enter word: ")
            word=input()
            print("meaning: %s"%(find_meaning(word)))
        elif opt==4:
            disp_sorted()
        elif opt==5:
            exit()
        print("Continue?")
        ch=input()

main()

