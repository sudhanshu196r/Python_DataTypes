'''

    @Author: Sudhanshu Kumar
    @Date: 26-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 26-09-2024
    @Title : Python program to find the repeated item in the tuple

'''


def repeated_Item(tup):
    """
    Description:
        This function will find the repeated item in the tuple
    Parameters:
        tup : a tuple in which we have to find duplicates
    Returns:
        Returns items which are repeated

    """
    seen = []
    repeated = []
    for ele in tup:
        if ele in seen:
            if ele not in repeated:
                repeated.append(ele)
        else:
            seen.append(ele)
    
    return repeated
    


def main():
    lst1 = (1,1.3,'a',"ddmd",1,2,2,3,4,3)
    print(repeated_Item(lst1))
    

if __name__=="__main__":
    main()
 