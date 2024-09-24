'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to create a frozen set

'''

def frozenSet(lst):
    """
    Description:
        This function will create a frozen set
    Parameters:
        lst : a list
    Returns:
        Frozen set of list

    """

    st1 = frozenset(lst)
    
    return st1

def main():
    lst = [1,2,1,3,4,2,4,5]
    #st2 = {5,2,6,7,8}
    print(frozenSet(lst))

if __name__=="__main__":
    main()
