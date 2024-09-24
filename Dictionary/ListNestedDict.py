'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to convert list to nested dictionary

'''

def list_to_nested_dict_keys(lst):
    """
    Description:
        This function will convert list to nested dictionary
    Parameters:
        lst: It takes a list as argument
    Returns:
        Nested list
    """
    ans=my_dict = {}
    for item in lst:
        my_dict[item]={}
        my_dict = my_dict[item]

    return ans

def main():
    lst = [1,2,3,4]
    print(list_to_nested_dict_keys(lst))

if __name__=="__main__":
    main()