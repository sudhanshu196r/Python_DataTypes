'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to generate dictionary for n like {1:1*1, ... , n:n*n}

'''

def generate(n):
    """
    Description:
        This function generates a dictinory where key is n and value is n*n
    Parameters:
        n : Specifies no. of elements to be in dict
    Returns:
        Returns the generated dictionary
    """

    my_dict = {}

    for i in range(1,n+1):
        my_dict[i]=i*i

    return my_dict

def main():
    n = int(input("Enter number of elements you want in the dictionary : "))
    my_dict = generate(n)
    print(my_dict)

if __name__=="__main__":
    main()