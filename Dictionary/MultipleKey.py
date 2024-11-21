'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to check if multiple key exists in the dictionary

'''

def multiKey(dict, keys):
    """
    Description:
        This function will check if all the key exists or not
    Parameters:
        dict : dictionay in which we have to check the keys
        keys : list of keys to look for
    Returns:
        true or false
    """
    return all(key in dict for key in keys)

def main():
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    keys = ['name','age']
    ans = multiKey(my_dict,keys)
    print(ans)

if __name__=="__main__":
    main()