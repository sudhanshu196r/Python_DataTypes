'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to remove an element if it is present in set

'''

def removeElement(st,ele):
    """
    Description:
        This function will remove members from a set if it is present
    Parameters:
        st: a set
        ele : element to be removed
    Returns:
        A set after removing members

    """

    if ele in st:
        st.remove(ele)

    return st

def main():
    st = {1,2,1,3,4,2,4,5}
    ele = int(input("Enter element to be removed : "))
    print(removeElement(st,ele))

if __name__=="__main__":
    main()
