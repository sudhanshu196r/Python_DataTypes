'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to find words longer than n in a list

'''

def longer(lst,n):
    """
    Description:
        This function will find the longer words
    Parameters:
        lst : a list
        n : length to compare
    Returns:
        Return list of longer words

    """

    ans_lst = []
    for ele in lst:
        if len(ele)>n:
            ans_lst.append(ele)

    return ans_lst



def main():
    lst = ['sam','ram','shyam','sudhanshu','ab','jdff']
    n=3
    print(longer(lst,n))

if __name__=="__main__":
    main()
 