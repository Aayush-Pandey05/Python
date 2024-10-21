'''
Question:- design a python program to computee the number of 
charecters, words and lines in a file and also print the most
frequent words read from the file 

'''

def counter(fname):
    num_words = 0
    num_lines = 0
    num_char = 0
    num_spaces = 0
    with open(fname,"r") as f:
        for lines in f:
            num_lines += 1
            word = "Y"
            for letter in lines:
                if(letter!=" " and word == "Y"):
                    num_words += 1
                    word = "N"
                elif(letter == " "):
                    num_spaces += 1
                    word = "Y"
                for i in letter:
                    if(i!=" " and i!="\n"):
                        num_char += 1
    print(f"Number of words in text file:-{num_words}")
    print(f"Number of lines in text file:-{num_lines}")
    print(f"Number of charecters in text file:-{num_char}")
    print(f"Number of spaces in text file:-{num_spaces}")

if __name__ == "__main__":
    fname = "File1.txt"
    try:
        counter(fname)
    except:
        print("file not found")
                
