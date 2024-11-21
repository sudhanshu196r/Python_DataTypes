'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to create dictionary from string and count occurence of characters

'''

def createDict(st):
    """
    Description:
        This function counts the frequency of characters in the string and add it in the dictionary
    Parameters:
        st : Takes string as a parameter
    Returns:
        It returns the dictionary created
    """
    st_dict = {}
    for i in range(0,len(st)):
        if st[i] in st_dict:
            st_dict[st[i]]+=1
        else:
            st_dict[st[i]]=1

    return st_dict

def main():
    st = input("Enter a string : ")
    st_dict = createDict(st)
    print(st_dict)

if __name__=="__main__":
    main()

