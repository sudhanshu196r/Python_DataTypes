'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to append one list to another

'''

import itertools

def append_lst(lst1,lst2):
    """
    Description:
        This function will append one list to another
    Parameters:
        lst1 : first list
        lst2 : second list
    Returns:
        Return an appended list

    """
    lst1.extend(lst2)
    #ans1 = lst1+lst2

    return lst1

def main():
    lst1 = [1,2,3,45,6,7,8,9]
    lst2 = [1,2,3,4]
    print(append_lst(lst1,lst2))
    

if __name__=="__main__":
    main()
 