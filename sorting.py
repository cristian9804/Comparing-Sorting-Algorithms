
import time
import random

def sortTimeUsing(sortf,A):
    t = time.time()
    sortf(A)
    t = time.time()-t
    print(t)
    
    
def insertionSort(A):
    if len(A)>0:
        for i in range(1,len(A)):
            insert(A[i],A,i)
    else:
        print("Array is already sorted ")

def insert(k, A, hi):
    for i in range (hi,0,-1):
        if k >= A[i-1]:
            A[i] = k
            return
        A[i] = A[i-1]
    A[0] = k

def selectionSort(A):
    for i in range(len(A)):
        imin = findMin(i,A)
        swap(i,imin,A)
            
def findMin(i, A):
    imin = i
    for j in range(i+1,len(A)):
        if A[j] < A[imin]:
            imin = j
    return imin

def swap(i, j, A):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

    
def mergeSort(A):
    if len(A) <= 1:
        return
    mid = len(A)//2
    half1 = A[:mid]
    half2 = A[mid:]
    mergeSort(half1)
    mergeSort(half2)
    merge(half1,half2,A)
    
def merge(h1, h2, A):
    i=0; j1=0; j2=0
    while j1<len(h1) and j2<len(h2):
        if h1[j1] < h2[j2]:
            A[i] = h1[j1]
            j1 += 1; i += 1
        else:
            A[i] = h2[j2]
            j2 += 1; i += 1
    while j1 < len(h1):
        A[i] = h1[j1]
        j1 += 1; i += 1
    while j2 < len(h2):
        A[i] = h2[j2]
        j2 += 1; i += 1

def quickSort(A):
     quickSortRec(A,0,len(A))
        
def quickSortRec(A, lo, hi):
# sorts A[lo:hi]
    if hi-lo <= 1:
        return
    iPivot = partition(A,lo,hi)
    quickSortRec(A,lo,iPivot)
    quickSortRec(A,iPivot+1,hi)
    
def partition(A, lo, hi):
    pivot = A[lo]
    B = [0 for i in range(lo,hi)]
    loB = 0
    hiB = len(B)-1
    for i in range(lo+1,hi):
        if A[i] < pivot:
            B[loB] = A[i]
            loB += 1
        else:
            B[hiB] = A[i]
            hiB -= 1
    B[loB] = pivot
    for i in range(lo,hi):
        A[i] = B[i-lo]
    return lo+loB

myArray=[0 for i in range(1000000)] 
for i in range (len(myArray)-1):
    myArray[i] =  random.randint(0,9999)


sortTimeUsing(insertionSort,myArray)
sortTimeUsing(selectionSort,myArray)
sortTimeUsing(mergeSort,myArray)
sortTimeUsing(quickSort,myArray)


# Below are some of the results that i've obtained, you can have a look at them to get a rough idea

#100
#insertionSort = 0.0
#selectionSort = 0.0009965896606445312
#mergeSort     = 0.0
#quickSort     = 0.0009970664978027344

#1000
#insertionSort = 0.0249330997467041
#selectionSort = 0.020943403244018555
#mergeSort     = 0.0019948482513427734
#quickSort     = 0.07087373733520508

#10000
#insertionSort = 2.730440378189087
#selectionSort = 2.231842041015625
#mergeSort     = 0.025944948196411133
#quickSort     = error,'maximum recursion depth exceeded in comparison'

#100000
#insertionSort = 279.7318022251129
#selectionSort = 239.53459286689758
#mergeSort     = 0.33127403259277344
#quickSort     = error,'maximum recursion depth exceeded in comparison'

#1000000
#insertionSort = 
#selectionSort = 
#mergeSort     = 4.89026665687561
#quickSort     = 
