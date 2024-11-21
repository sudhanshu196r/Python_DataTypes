'''

    @Author: Sudhanshu Kumar
    @Date: 24-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 24-09-2024
    @Title : Python program to create dictionary from string and count occurence of characters

'''
def printDict(my_dict):
    """
    Description:
        This function will print dictionary in tabular format
    Parameters:
        It takes a dictionary as parameter
    Returns:
    """

    print(f"{'Key':<10}{'Value':<10}")
    for key,value in my_dict.items():
        print(f"{key:<10}{value:<10}")

def main():
    my_dict = {1: 'Apple', 2: 'Banana', 3:'Mango', 4:'Guava'}
    printDict(my_dict)

if __name__=="__main__":
    main()




