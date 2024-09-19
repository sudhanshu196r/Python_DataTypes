'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to generate list and tuple

'''

def genList(sample):
    """
    Description: 
        generate a list using string sample
    Parameters:
        sample: string with comma seprated numbers
    Returns:
        It return generated list
    """
    return sample.split(",")

def genTuple(sample):
    """
    Description: 
        generate a tuple using string sample
    Parameters:
        sample: string with comma seprated numbers
    Returns:
        It return generated tuple
    """
    return tuple(genList(sample))

def main():
    sample = input("Enter comma seprated numbers")
    print(genList(sample))
    print(genTuple(sample))

if __name__=="__main__":
    main()