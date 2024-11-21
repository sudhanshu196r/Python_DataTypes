'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''

def descSort(dict):
    """
    Description:
        It sorts the dict in descending order
    Parameters:
        dict: takes dictionary as a parameter
    Returns:
        Sorted Dictionary
    """
    ans_dict = sorted(dict.items(), key=lambda items:items[1],reverse=True)
    return ans_dict

def ascSort(dict):
    """
    Description:
        It sorts the dict in ascending order
    Parameters:
        dict: takes dictionary as a parameter
    Returns:
        Sorted Dictionary
    """
    ans_dict = sorted(dict.items(), key=lambda items:items[1])
    return ans_dict

def main():
    my_dict = {'apple': 4, 'banana': 2, 'orange': 3, 'grape': 5}
    print("sorted in descending order: ")
    print(descSort(my_dict))
    print("sorted in ascending order: ")
    print(ascSort(my_dict))

if __name__=="__main__":
    main()