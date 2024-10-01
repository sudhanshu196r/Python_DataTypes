'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to clone a tiple

'''


def unpackTuple(tup):
    """
    Description:
        This function make clone of the tuple
    Parameters:
        tup : a tuple which has to be cloned
    Returns:
        Returns cloned tuple

    """
    c_tuple= tup
    

    return c_tuple

def main():
    lst1 = (1,1.3,'a',"ddmd")
    print(unpackTuple(lst1))
    

if __name__=="__main__":
    main()
 