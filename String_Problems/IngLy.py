'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to add 'ing' at the end of a string and if it is already present add 'ly' and if
            length <3 leave it as it is.

'''

def add_ing_ly(string):
    """
    Description: 
        This function add 'ing' at the end of a string and if it is already present add 'ly' and if
            length <3 leave it as it is.
    Parameters:
        string: a string as an parameter.
    Returns:
        A new string with required changes
    """

    new_str = string
    if len(string)<3:
        return new_str
    elif string[-3:]=='ing':
        return new_str+'ly'
    else:
        return new_str+'ing'

def main():
    string = 'kn'
    print(add_ing_ly(string))

if __name__=="__main__":
    main()