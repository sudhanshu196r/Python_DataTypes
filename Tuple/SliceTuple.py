'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to slice tuple

'''


def sliceTuple(my_tuple):
    """
    Description:
        This function will slice the tuple 
    Parameters:
        tup: tuple which we have to slice
    Returns:

    """
    slice1 = my_tuple[1:4]   # Elements from index 1 to 3
    slice2 = my_tuple[:5]    # Elements from the start to index 4
    slice3 = my_tuple[3:]    # Elements from index 3 to the end
    slice4 = my_tuple[-4:-1] # Negative indexing to slice last few elements
    slice5 = my_tuple[::2]   # Slice with a step of 2

    # Printing the sliced tuples
    print("Slice from index 1 to 3:", slice1)
    print("Slice from start to index 4:", slice2)
    print("Slice from index 3 to end:", slice3)
    print("Slice from -4 to -1:", slice4)
    print("Slice with a step of 2:", slice5)
    


def main():
    lst1 = (1,1.3,'a',"ddmd",1,2,2,3,4,3)
    sliceTuple(lst1)
    

if __name__=="__main__":
    main()
 