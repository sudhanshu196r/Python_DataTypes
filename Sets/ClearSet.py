'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to clear a set

'''

def clearSet(st1):
    """
    Description:
        This function will clear the set
    Parameters:
        st1: first set
    Returns:
        Empty set

    """

    st1.clear()
    
    return st1

def main():
    st1 = {1,2,1,3,4,2,4,5}
    #st2 = {5,2,6,7,8}
    print(clearSet(st1))

if __name__=="__main__":
    main()
