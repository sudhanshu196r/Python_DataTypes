'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to replace all the occurence of first char except first occurence

'''

def replaceChar(string):
    """
    Description : 
        This function will replace all the occurence of first char except first occurence

    Parameters:
        string: It will take a string as the parameter

    Returns:
        New string after replacing
    """
    power = string[0]
    new_str = string[0]
    for i in range(1,len(string)):
        if power == string[i]:
            new_str+='$'
        else:
            new_str+=string[i]

    return new_str

def main():
    string = "sudhanshu"
    print(replaceChar(string))

if __name__=="__main__":
    main() 