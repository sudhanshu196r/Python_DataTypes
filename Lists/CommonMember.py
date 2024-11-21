'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to check if two lists have atleast 1 common member

'''

def common_member(lst1,lst2):
    """
    Description:
        This function will check if two lists have atleast one common member
    Parameters:
        lst1 : first list
        lst2 : second list
    Returns:
        Return True or False

    """
    for ele in lst1:
        if ele in lst2:
            return True

    return False
    


def main():
    lst1 = [1,2,3,4,2,4,3,1,5]
    lst2 = [2,5,7,8,5,0]
    print(common_member(lst1,lst2))

if __name__=="__main__":
    main()
 