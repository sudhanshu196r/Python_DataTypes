'''

    @Author: Sudhanshu Kumar
    @Date: 25-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 25-09-2024
    @Title : Python program to unpack tuple in multiple variable

'''


def unpackTuple(tup):
    """
    Description:
        This function will unpack tuple in multiple variables
    Parameters:
        tup : a tuple which has to be unpacked
    Returns:
        Returns different variables in which tuple is unpacked

    """
    a,b,c,d = tup
    

    return a,b,c,d

def main():
    lst1 = (1,1.3,'a',"ddmd")
    print(unpackTuple(lst1))
    

if __name__=="__main__":
    main()
 