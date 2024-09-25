'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to remove duplicate from list of lists

'''

import itertools

def removeDuplicates(lst):
    """
    Description:
        This function will remove duplicates from list of lists
    Parameters:
        lst: input list
    Returns:
        List after removing duplicates

    """
    ans_lst = []
    for ele in lst:
        if ele not in ans_lst:
            ans_lst.append(ele)

    return ans_lst

    

def main():
    lst = [1,[2,3],[4,3],[2,3],[1,2],2,1]
    print(removeDuplicates(lst))
    

if __name__=="__main__":
    main()
 