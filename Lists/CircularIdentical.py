'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to check if two lists are circular identical

'''

import itertools

def circular(lst1,lst2):
    """
    Description:
        This function will check if two lists are circular identical
    Parameters:
        lst1 : first list
        lst2 : second list
    Returns:
        Return True or False

    """
    ext_lst = lst1+lst2
    if any(ext_lst[i:i+len(lst2)]==lst2 for i in range(len(lst2))):
        return True
    return False

def main():
    lst1 = [1,2,3,45,6,7,8,9]
    lst2 = [1,2,3,4]
    print(circular(lst1,lst2))
    

if __name__=="__main__":
    main()
 