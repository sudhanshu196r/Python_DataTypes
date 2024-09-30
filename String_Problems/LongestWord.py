'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to add find the longest word from a list of words

'''

def findLongest(words):
    long_length = len(words[0])
    ans = ''
    for word in words:
        if len(word)>long_length:
            long_length = len(word)
            ans = word
    
    return ans

def main():
    words = ['ram','shyam','word','apple','mango','encantus']
    print(findLongest(words))

if __name__=="__main__":
    main()
