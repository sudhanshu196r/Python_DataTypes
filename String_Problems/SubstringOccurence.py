'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to find occurence of substring inside a string

'''

def countSub(string,sub):
    """
    Description: 
        This method will return the count of substring in the string

    Parameters:
        string: in which we have to  look for the substring
        sub: substring that we have to count
    
    Returns:
        returns count of substring
    """


    return string.count(sub)

def main():
    string = 'sudhanshu'
    print(countSub(string,'u'))


if __name__=="__main__":
    main()