'''

    @Author: Sudhanshu Kumar
    @Date: 30-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 30-09-2024
    @Title : Python program to convert first n character to lower case

'''

def lowerN_char(string,n):
    ans_str = string[0:n].lower()+string[n:]
    return ans_str

def main():
    string = 'SUDhanSHU'
    print(lowerN_char(string,4))

if __name__=="__main__":
    main()