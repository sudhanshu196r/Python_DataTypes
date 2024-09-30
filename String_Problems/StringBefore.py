'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to get string before specified character

'''

def getString(string,ele):
    """
    Description:
        This function will return string before specified character
    Parameter:
        string: string on which operation has to be performed
        ele: character before which we have to return the string
    Returns: 
        a string before the specified characters
    """

    new_str = ''
    for char in string:
        if char==ele :
            break
        else:
            new_str+=char

    return new_str

def main():
    string = 'https://www.linked.in'
    print(getString(string,'.'))

if __name__=="__main__":
    main()

