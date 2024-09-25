'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to sort list according to last element of its tuple elements

'''

def sortList(lst):
    """
    Description:
        This function will sort the tuples of the list
    Parameters:
        lst : a list
    Returns:
        Return sorted list

    """
    return sorted(lst, key=lambda x:x[-1])


def main():
    lst = [(1,2),(2,3),(3,4),(9,2),(5,3)]
    print(sortList(lst))

if __name__=="__main__":
    main()
