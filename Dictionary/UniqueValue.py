'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to print unique values in a dictionary

'''

def findUnique(my_dict):
    """
    Description:
        Function to find unique values in a dictionary
    Parameters:
        my_dict: Takes a dictionary as argument
    Retuns:
        A set containing unique values
    """
    ans = set(my_dict.values())
    return ans

def main():
    my_dict = {1:"a", 2:"v", 3:"a",4:"c",5:"c",6:'a'}
    ans = findUnique(my_dict)
    print(ans)

if __name__=="__main__":
    main()
