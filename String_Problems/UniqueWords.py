'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to find unique words and sort them 

'''

def uniqueWord(words):
    
    """
    Description: 
        This function will sort the unique words from a string contaning words

    Parameters:
        words: a string containg comma seprated words
    
    Returns: 
        A sorted list conatining uniqe words
    """

    all_words = list(words.split(','))
    unique_words = list(set(all_words))
    unique_words.sort()
    return unique_words

def main():
    words = 'i,am,going,home,today,are,you,going,?'
    print(uniqueWord(words))

if __name__=="__main__":
    main()