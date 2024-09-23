'''

    @Author: Sudhanshu Kumar
    @Date: 23-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 23-09-2024
    @Title : Python program to create an array and print the array

'''
import array
def countFreq(arr):
    freq_count = {}

    for ele in arr:
        if ele in freq_count:
            freq_count[ele]+=1
        else:
            freq_count[ele] = 1

    return freq_count

def main():
    arr = array.array('i')
    n = int(input("Enter size: "))
    for i in range(n):
        ele = int(input())
        arr.append(ele)

    freq_count = countFreq(arr)
    print(freq_count)

if __name__=="__main__":
    main()