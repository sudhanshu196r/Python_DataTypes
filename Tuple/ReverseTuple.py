'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to reverse a tuple

'''


def reverseTuple(tup):
    """
    Description:
        This function will reverse the tuple
    Parameters:
        tup: tuple that we have to reverse
    Returns:
        Return tuple after reversing

    """

    rev_tupe = tup[::-1]
    return rev_tupe
    


def main():
    lst1 = (1,1.3,'a',"ddmd",1,2,2,3,4,3)
    print(reverseTuple(lst1))
    

if __name__=="__main__":
    main()
 