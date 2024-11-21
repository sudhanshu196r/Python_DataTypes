'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to concat dictionary

'''

def concatDictionary(dict1, dict2, dict3):
    """
    Description:
        This function concats the dictionary
    Parameters:
        dict1, dict2, dict3 : These are the dictionaries that we have to concat
    Result:
        Final dictionary after concatination
    """
    final_dict = dict1.copy()
    final_dict.update(dict2)
    final_dict.update(dict3)

    return final_dict

def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}

    result = concatDictionary(dic1, dic2, dic3)
    print(result)

if __name__=="__main__":
    main()