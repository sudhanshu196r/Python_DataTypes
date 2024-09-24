'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to count a value in the dictionary

'''

def countValue(my_dict):
    """
    Description:
        This function will count the value in the nested dictionary
    Parameters:
        It takes a nested dictionary as parameter
    Returns:
        Count of success
    """
    count_success = sum(d['success'] for d in my_dict)
    return count_success

def main():
    sample_data = [{'id': 1, 'success': True}, {'id': 2, 'success': False}, {'id': 3, 'success': True}]
    ans = countValue(sample_data)
    print(ans)

if __name__=="__main__":
    main()