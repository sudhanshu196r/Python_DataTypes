'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to create symmetric difference set

'''

def symmDiffSet(st1,st2):
    """
    Description:
        This function will create set of symmetric difference of sets
    Parameters:
        st1: first set
        st2: second set
    Returns:
        Set of symmetric difference of sets

    """

    ans_set = st1^st2
    return ans_set

def main():
    st1 = {1,2,1,3,4,2,4,5}
    st2 = {5,2,6,7,8}
    print(symmDiffSet(st1,st2))

if __name__=="__main__":
    main()
