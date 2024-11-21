'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to sort three integers without using loop or conditional statement

'''

def sort_three_numbers(a, b, c):

    """
    Description: 
        This method sorts the three integers
    Parameters:
        a, b, c : Three integers
    Returns:
        It returns the creation and modification time

    """
    
    smallest = min(a, b, c)
    largest = max(a, b, c)
    
    
    middle = (a + b + c) - smallest - largest
    
    return smallest, middle, largest

def main():
    a, b, c = 15, 9, 23
    
    sorted_numbers = sort_three_numbers(a, b, c)
    
    print(f"Sorted numbers: {sorted_numbers}")

if __name__ == "__main__":
    main()
