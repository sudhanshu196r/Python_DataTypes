'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to create a set

'''

def createSet():
    """
    Description:
        This function will create a set
    Parameters:
    Returns:
        New Set
    """
    st = set()
    for i in range(5):
        st.add(int(input()))
    return st

def main():
    ans = createSet()
    print(ans)

if __name__=="__main__":
    main()