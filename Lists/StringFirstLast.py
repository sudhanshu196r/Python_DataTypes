'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to count if string have same first and last char in list

'''

def firstLast(lst):
    """
    Description:
        This function will check and count if string first and last char are same
    Parameters:
        lst : a list
    Returns:
        Count of such strings

    """
    count = 0
    for ele in lst:
        if len(ele)>=2:
            if ele[0]==ele[-1]:
                count+=1
    
    return count


def main():
    lst = ['aba','abc','xyx','xyz','ded']
    print(firstLast(lst))

if __name__=="__main__":
    main()
