'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to convert a list to tuple

'''


def list_To_Tuple(lst):
    """
    Description:
        This function will convert list to tuple
    Parameters:
        lst : a list which we have to convert to tuple
    Returns:
        Returns a list

    """
    return tuple(lst)
    


def main():
    lst1 = [1,1.3,'a',"ddmd",1,2,2,3,4,3]
    print(list_To_Tuple(lst1))
    

if __name__=="__main__":
    main()
 