'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to reverse the name provided by the user

'''

def printReverse(fName,lName):
    """
    Description:
        Function to reverse first name and last name
    Parameters:
        fName: Represents first name
        lName: Represents last name
    Returns:
        Returns fName and lName reversed
    """
    return lName+' '+fName

def main():
    fName = input("Enter First name: ")
    lName = input("Enter Last Name : ")
    ans = printReverse(fName,lName)
    print(ans)

if __name__=="__main__":
    main()