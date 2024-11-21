'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to create copy of a list

'''

def copyList(lst):
    """
    Description:
        This function will return the copy of the list
    Parameters:
        lst : a list
    Returns:
        Return the copy of the list

    """
    new_lst = lst.copy()
    return new_lst


def main():
    lst = [1,2,3,4,2,4,3,1,5]
    print(copyList(lst))

if __name__=="__main__":
    main()
 