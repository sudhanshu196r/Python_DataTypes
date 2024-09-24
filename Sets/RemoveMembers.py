'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to remove members from a set

'''

def addMembers(st):
    """
    Description:
        This function will remove members from a set
    Parameters:
        st: a set
    Returns:
        A set after removing members

    """
    n = int(input("Number of members you want to remove : "))
    for i in range(n):
        st.discard(int(input())) #at.remove(3) if not found it will throw KeyError

    return st

def main():
    st = {1,2,1,3,4,2,4,5}
    print(addMembers(st))

if __name__=="__main__":
    main()
