'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to remove 0th, 4th and 5th element

'''

def removeIndexEle(lst):
    """
    Description:
        This function will remove 0th, 4th and 5th element
    Parameters:
        lst : a list
    Returns:
        Return list after removing those elements

    """
    lst.pop(0)
    lst.pop(4)
    lst.pop(5)
    return lst


def main():
    lst = [1,2,3,4,2,4,3,1,5]
    print(removeIndexEle(lst))
    

if __name__=="__main__":
    main()
 