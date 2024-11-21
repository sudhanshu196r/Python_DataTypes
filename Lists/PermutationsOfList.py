'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to generate all the permutations of the list

'''

import itertools

def generate_Perm(lst):
    """
    Description:
        This function will generate all the permutations of the list
    Parameters:
        lst : a list
    Returns:
        Return list after generating all its permutation

    """

    return list(itertools.permutations(lst))


def main():
    lst = [1,2,3,4]
    print(generate_Perm(lst))
    

if __name__=="__main__":
    main()
 