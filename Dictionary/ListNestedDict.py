'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to count a value in the dictionary

'''

def list_to_nested_dict_keys(lst):
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