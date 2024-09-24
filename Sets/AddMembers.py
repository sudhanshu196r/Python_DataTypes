'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to add members to a set

'''

def addMembers(st):
    """
    Description:
        This function will add members to a set
    Parameters:
        st: a set
    Returns:
        A set after adding members

    """
    n = int(input("Number of members you want to add : "))
    for i in range(n):
        st.add(int(input()))

    return st

def main():
    st = {1,2,1,3,4,2,4,5}
    print(addMembers(st))

if __name__=="__main__":
    main()
