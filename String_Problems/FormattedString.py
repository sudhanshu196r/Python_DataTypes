'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to print formatted string with width 50

'''

import textwrap

def formatString(sample):
    """
    Description: 
        This function will return a formatted string of width 50
    Parameters:
        sample: this is the sample text that we have to format
    Returns:
        Formatted string

    """

    formatted_string = textwrap.fill(sample, width=50)

    return formatted_string

def main():
    sample = '''hi where are you going guys please wait for me I also want to join as I am reallly excited for the event. I was really 
waiting for this day to come and now I am so nervous and excited at the same time as I don;t know how it is
to meet your favourite actor. '''
    print(formatString(sample))

if __name__=="__main__":
    main()

