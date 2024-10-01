
def lenCheck(lst):

    return [len(item)>4 for item in lst]

def main():
    lst = ['ram','shyam','gyaan','rohan']
    print(lenCheck(lst))

if __name__=="__main__":
    main()