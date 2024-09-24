'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to iterate over a set

'''

def iterateSet(st):
    """
    Description:
        This function will iterate over a set
    Parameters:
        st: a set
    Returns:

    """
    for ele in st:
        print(ele)

def main():
    st = {1,2,1,3,4,2,4,5}
    iterateSet(st)

if __name__=="__main__":
    main()
