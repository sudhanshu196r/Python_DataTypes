'''

    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 19-09-2024
    @Title : Write a Python program to get execution time of a method

'''


import time

def example_method():
    
    time.sleep(2)  # Sleep for 2 seconds

def measure_time():
    start_time = time.time()

    example_method()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Execution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    measure_time()
