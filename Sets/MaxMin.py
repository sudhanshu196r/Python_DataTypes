'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to find max and min in a set

'''

def maxMin(st1):
    """
    Description:
        This function will find max and min value in set
    Parameters:
        st1: set
    Returns:
        max and min value

    """

    max_val = max(st1)
    min_val = min(st1)
    
    return max_val,min_val

def main():
    st1 = {1,2,1,3,4,2,4,5}
    #st2 = {5,2,6,7,8}
    max_val,min_val=maxMin(st1)
    print("Max Value : ",max_val)
    print("Min Value : ",min_val)

if __name__=="__main__":
    main()
