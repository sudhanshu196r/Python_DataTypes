'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to count number of list values in dictionary

'''

def isList(my_dict):
    """
    Description:
        This function will count number of list value in dictionary
    Parameters:
        my_dict : dictionay in which we have to count
    Returns:
        count of list values 
    """

    count = 0
    check_list = type([])
    for value in my_dict.values():
        if type(value) == check_list:
            count+=1

    return count

def main():
    my_dict = {1:['a'], 2:['d'], 3: 'Ab', 4:['x']}
    ans = isList(my_dict)
    print(ans)

if __name__=="__main__":
    main()