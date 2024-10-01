'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to create a tuple with different types of data

'''


def createTuple(lst):
    """
    Description:
        This function will create a tuple with different type of data
    Parameters:
        lst : list as input because we cannot take individual input for tuple as its immutable
    Returns:
        Return a tuple

    """
    ans = tuple(lst)
    #ans1 = lst1+lst2

    return ans

def main():
    lst1 = [1,1.3,'a',"ddmd"]
    print(createTuple(lst1))
    

if __name__=="__main__":
    main()
 