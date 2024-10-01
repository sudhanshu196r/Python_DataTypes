'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to remove a element from tuple

'''


def reomve_Element(tup,ele):
    """
    Description:
        This function will remove an element from tuple
    Parameters:
        tup: tuple from which we have to remove the element
    Returns:
        Return tuple after removing the Element

    """
    li = list(tup)
    li.remove(ele)
    return tuple(li)
    


def main():
    lst1 = (1,1.3,'a',"ddmd",1,2,2,3,4,3)
    print(reomve_Element(lst1,1))
    

if __name__=="__main__":
    main()
 