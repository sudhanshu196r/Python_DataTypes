'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to remove duplicates from a list

'''

def removeDuplicates(lst):
    """
    Description:
        This function will remove duplicates from a list 
    Parameters:
        lst : a list
    Returns:
        Return list after removing duplicates

    """
    unique = []
    for ele in lst:
        if ele not in unique:
            unique.append(ele)
    
    return unique


def main():
    lst = [1,2,3,4,2,4,3,1,5]
    print(removeDuplicates(lst))

if __name__=="__main__":
    main()
 