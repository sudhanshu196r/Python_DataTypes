'''

    @Author: Sudhanshu Kumar
    @Date: 18-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 18-09-2024
    @Title : Write a Python program to print number of days between two dates

'''

from datetime import datetime

def printDays(date1,date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1,date_format)
    d2 = datetime.strptime(date2,date_format)

    return abs((d2-d1).days)

def main():
    date1 = input("Enter first date in format 'YYYY-MM-DD' : ")
    date2 = input("Enter second date in format 'YYYY-MM-DD' : ")

    print(printDays(date1,date2))

if __name__=="__main__":
    main()