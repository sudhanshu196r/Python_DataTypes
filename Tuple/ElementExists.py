'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to find if an element exists in a tuple

'''


def elementExists(tup,ele):
    """
    Description:
        This function will check if element exists in a tuple
    Parameters:
        tup : a tuple in which we have search the element
        ele : Element which we have to find
    Returns:
        Returns True or false

    """
    if ele in tup:
        return True
    return False
    


def main():
    lst1 = (1,1.3,'a',"ddmd",1,2,2,3,4,3)
    print(elementExists(lst1,2))
    

if __name__=="__main__":
    main()
 