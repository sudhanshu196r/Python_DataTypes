'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to get sum of elements of list

'''

def freqCount(string):
    """
    Description:
        This function will count the frequency of each character
    Parameters:
        string: It takes a string as parameter
    Returns:
        It returns a dictionary containing the character as key and it's frquency as value
    """
    freq = {}
    for ele in string:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    
    return dict(sorted(freq.items(), key= lambda val: val[1], reverse=True ))

def main():
    string = "Applegames"
    print(freqCount(string))

if __name__=="__main__":
    main()