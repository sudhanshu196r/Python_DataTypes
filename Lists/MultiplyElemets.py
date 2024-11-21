'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to multiply all the elements of the list

'''

def proElements(lst):
    """
    Description:
        This function will multiply all the elements of the list
    Parameters:
        lst : a list
    Returns:
        Product of all the elements

    """

    pro = 1
    for i in range(len(lst)):
        pro*=lst[i]
    
    return pro

def main():
    lst = [1,2,1,3,4,2,4,5]
    print(proElements(lst))

if __name__=="__main__":
    main()
