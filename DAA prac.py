#practical01

#METHOD01

def _sum(arr):
    sum=0
    for i in arr:
        sum +=i
    return sum
arr=[20,3,14,15,45,18,25]
ans=_sum(arr)
print("Sum of the array is",ans)

#METHOD02
arr=[20,3,14,15,45,18,25]
ans=sum(arr)
print("Sum of the array is ",ans)

#METHOD1.1
def ls(arr,a,b):
    for i in range(a):
        if(arr[i]==b):
            return i
    return -1
arr=[9,7,3,5,1]
print("The array given is ",arr)
k=3
print("Elemnt to be found is",k)
l=len(arr)
index=ls(arr,l,k)
if(index==-1):
    print("element is not the list")
else:
    print("index of the elemnt is:",index)
#METHOD1.2
def bs(arr,low,high,k):
    mid=(low+high)//2
    if low>high:
        return -1
    if arr[mid]<k:
        return bs(arr,mid+1,high,k)
    elif arr[mid]>k:
        return bs(arr,low,mid-1,k)
    elif arr[mid]==k:
        return mid
arr=[20,30,40,60,80,90]
k=60
print("The given array is",arr)
print("Element to be found is",k)
ans=bs(arr,0,len(arr)-1,k)
if ans==-1:
    print("Elemnt Not Found")
else :
    print("The Index of the element is ",ans)
#METHOD2.1
arr=[10,89,9,56,4,80,8]
min1=arr[0]
max1=arr[0]
for i in range(len(arr)):
    if arr[i]<min1:
     min1=arr[i]
    if arr[i]>max1:
     max1=arr[i]
print(min1)
print(max1)
#METHOD2.2
arr=[10,89,9,56,4,80,8]
arr.sort()
print(arr[0])
print(arr[-1])
#METHOD3.1
arr=[1,7,8,4,5,16,8]
n=len(arr)
countEven=0
countOdd=0
for i in range(0,n):
    if arr[i]%2==0:
        countEven+=1
    else:
        countOdd+=1
print("Even Elment count:",countEven)
print("Odd Elment count:",countOdd)
#METHOD3.2
arr=[1,7,8,4,5,16,8]
n=len(arr)
countEven=0
countOdd=0
for i in range (0,n):
    if arr[i]&1==0:
        countEven+=1
    else:
        countOdd+=1
print("Even Elment count:",countEven)
print("Odd Elment count:",countOdd)
#practical02

#METHOD0.1
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

matrix = []

print("Enter values in Matrix:")
for i in range(row):
    data = []
    for j in range(col):
        data.append(int(input()))
    matrix.append(data)
print("Matrix:")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
for i in range(row):
    sumR = 0
    for j in range(col):
        sumR += matrix[i][j]
    print("Sum of row", i + 1, ":", sumR)

for i in range(col):
    sumC = 0
    for j in range(row):
        sumC += matrix[j][i]
    print("Sum of column", i + 1, ":", sumC)
#METHOD0.2
import numpy as np
a=np.matrix('10 20;30 40')
print("ourMatrix:\n",a)
sumofrow=np.sum(a,axis=1)
print("\nSum of all the rows:" ,sumofrow)
sumofcols=np.sum(a,axis=0)
print("\nSum of all the  coloumns:",sumofcols)
#METHOD1.1
def addm(A,B):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (len(A)):
        for j in range(len (A[0])):
            result [i][j]=A[i][j]+B[i][j]
    for K in result:
        print(K)
    return 0
A=[[1,2,3],[3,4,5],[6,7,8]]
B=[[5,6,6],[1,2,5],[5,3,8]]
print("Result:")
addm(A,B)
#METHOD2.1
def multi(A, B):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for row in result:
        print(row)
    return 0

A = [[1, 2, 3], [6, 7, 4], [8, 10, 11]]
B = [[1, 5, 3], [2, 6, 5], [7, 4, 9]]

print("Result:")
multi(A, B)

#practical03

#METHOD0.1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_data = self.head.data
        self.head = self.head.next
        print(f"{popped_data} popped from the stack.")

    def display(self):
        current = self.head
        if self.is_empty():
            print("Stack is Empty.")
        else:
            print("Current Stack:")
            while current:
                print(current.data)
                current = current.next

# Main Program
stack = Stack()
while True:
    print("\nOptions:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")
    choice = input("Enter Your choice (1/2/3/4): ")

    if choice == '1':
        data = input("Enter the element to push: ")
        stack.push(data)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.display()
    elif choice == '4':
        print("Exiting the Program.")
        break
    else:
        print("Invalid choice. Please enter a valid input.")
#Practical04

#METHOD01
import time

def ls(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

def bns(arr, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] < k:
            return bns(arr, mid + 1, high, k)
        elif arr[mid] > k:
            return bns(arr, low, mid - 1, k)
        else:
            return mid
    else:
        return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key_element = 9

    # Linear search
    start_time = time.time()
    lsr = ls(arr, key_element)
    end_time = time.time()
    lst = (end_time - start_time) * 1000

    # Binary search
    start_time = time.time()
    bsr = bns(arr, 0, len(arr) - 1, key_element)
    end_time = time.time()
    bst = (end_time - start_time) * 1000

    print(f"Linear search result: {lsr}, Time: {lst:.6f} milliseconds")
    print(f"Binary search result: {bsr}, Time: {bst:.6f} milliseconds")
#Practical05
#Tower of Honai
def Tower(disk, source, auxiliary, target):
    if disk == 1:
        print("Move disk 1 from rod {} to rod {}".format(source, target))
        return
    Tower(disk - 1, source, target, auxiliary)
    print("Move disk {} from rod {} to rod {}".format(disk, source, target))
    Tower(disk - 1, auxiliary, source, target)
disk = 3
Tower(disk, 'A', 'B', 'C')
#Fractorial
def get_fac(n):
    result=1
    while n>1:
        result=result *n
        n-=1
    return result
def getfac(n):
    if n<=1:
        return 1
    else:
        return n* get_funrec(n-1)
inp=input("Enter a number")
inp=int(inp)
print (f"Factorial using itration:{get_fac(inp)}")
print(f"factorial using recursion:{get_fac(inp)}")
#Fibonacci
def fib(n):
    if n <= 1:
        return n
    fib_seq = [0, 1] 
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

n = 5
print("\nFibonacci series(Iteration) for n =", n, ":", fib(n))
print("Fibonacci series(Recursive) for n =", n, ": ", end="")
for i in range(n + 1):
    print(fib_rec(i), end=" ")
    
#Practical06
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(1, 10000) for _ in range(10000)]

start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(arr.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

print("Bubble sort time:", bubble_sort_time)
print("Selection sort time:", selection_sort_time)
print("Insertion sort time:", insertion_sort_time)
