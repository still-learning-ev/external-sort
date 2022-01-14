# written by zeeshan ahmad lone

from ntpath import join
import random
from datetime import datetime
import tempfile
import os
import time
import sys
import pandas as pd
import matplotlib.pyplot as plt
from hashlib import md5
from time import localtime
import string
import shutil
import heapq
from pathlib import Path


sortedTempFileHandlerList=[]



class heapnode:
    def __init__(self,item,fileHandler,):
        self.item = item
        self.fileHandler = fileHandler




def create_hugefile(number_of_numbers,range_of_numbers):
    n=number_of_numbers
    ll=[]
    file1 = open('hugenumbers.txt', 'w')
    random.seed(1)
    for i in range(n):
        temp_num=random.randrange(1,range_of_numbers,1)
        file1.write(str(temp_num)+"\n")
        # file1.writelines(str(temp_num))
    # print(i)
    file1.close





def create_random_file_name():
    cwd=os.getcwd()
    f_n='_number.txt'
    pref=''.join(random.choice(string.ascii_lowercase))
    pp=f"{pref}{f_n}"
    twd=cwd+r'\tempe'
    ppe=os.path.join(twd,pp)
    return ppe




#create a function to split the huge file in small files
def splitFiles(hugefilename,smallfilesize):
    hugefilename=hugefilename
    smallfilesize=smallfilesize
    tempbuffer=[]
    size=0
    cwd=os.getcwd()
    shutil.rmtree('tempe')
    os.makedirs('tempe')
    f_n='_number.txt'
    largefile=open(hugefilename)
    
    while True:
        pref=''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase+string.ascii_letters,k=40))
        size+=1
        pp=f"{pref}{f_n}"
        twd=cwd+r'\tempe'
        ppe=os.path.join(twd,pp)
        number=largefile.readline()
        if not number:
            n=len(tempbuffer)
            tempbuffer=mergeSort(tempbuffer,0,n-1)
            f=open(ppe,'w')
            # print('jhgjhgfjhdgjh',tempbuffer)
            tempbuffer=[str(i) for i in tempbuffer]
            for i in tempbuffer:
                f.write(i+"\n")
            # f.writelines(tempbuffer)
            # f.seek(0)
            sortedTempFileHandlerList.append(f.name)
            # print(tempbuffer)
            tempbuffer=[]
            f.close()
            break
        number_1=number.strip()
        tempbuffer.append(int(number_1))
        # print(tempbuffer)
        if(len(tempbuffer)==smallfilesize):
            # print(tempbuffer)
            tempbuffer=mergeSort(tempbuffer,0,smallfilesize-1)
            f=open(ppe,'w')
            # print('jhgjhgfjhdgjh',tempbuffer)
            tempbuffer=[str(i) for i in tempbuffer]
            for i in tempbuffer:
                f.write(i+"\n")
            # f.writelines(tempbuffer)
            # f.seek(0)
            sortedTempFileHandlerList.append(f.name)
            # print(tempbuffer)
            tempbuffer=[]
            # print(f.name)
            # print(twd)
            f.close()

#################################################################

def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m
  L = [0] * (n1)
  R = [0] * (n2)
  for i in range(0, n1):
    L[i] = arr[l + i]
  for j in range(0, n2):
    R[j] = arr[m + 1 + j]
  i = 0  # Initial index of first subarray
  j = 0  # Initial index of second subarray
  k = l  # Initial index of merged subarray
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

def mergeSort(arr, l, r):

    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr



def heapify(arr,i,n):

    # left =2 * i 
    # # print(left)
    # right = 2 * i
    # # print(right)
    # print('hello pod',arr[left].item,arr[i].item)
    # if left < n and arr[left].item< arr[i].item:
    #     smallest = left
    # else:
    #     smallest = i

    # if right < n and arr[right].item < arr[smallest].item:
    #     smallest = right

    # if i != smallest:
    #     (arr[i], arr[smallest]) = (arr[smallest], arr[i])

    #     heapify(arr, smallest, n)
    nums=[]
    list_of_objects=arr
    # print('len of obj is ',len(arr))
    for i in arr:
        z=i.item
        z=int(z)
        nums.append(z)
    # print('unsorted numerbers ',nums)
    heapq.heapify(nums)
    temp_sort=[]
    for num in nums:
        # for obj in list_of_objects:
        #     if num==obj.item:
        #         temp_sort.append(obj)
        #         break
        for i in range(len(list_of_objects)):
            if list_of_objects[i].item==num and list_of_objects[i] not in temp_sort:
                temp_sort.append(list_of_objects[i])
                break
            
    list_of_objects=[]
    list_of_objects=temp_sort
    temp_sort=[]
    nums=[]
    return list_of_objects





def reading(ans,smallfilesize):
    # this function is for reading the small chunk files storing them to the buffer and flushing
    # the buffer to a file


    list_of_objects=[]
    nums=[]
    sorted_output=[]

    if os.path.exists('output.txt'):
        os.remove('output.txt')

    for temps in sortedTempFileHandlerList:
        f=open(temps,'r')
        element=f.readline().strip()
        lines=f.readlines()
        open(temps, 'w').writelines(lines[0:])
        f.close()
        # element is of type str and it is the number in the file
        if element:
            element=int(element)
            nums.append(element)
        # created a list containg element as heap node object
        list_of_objects.append(heapnode(element,temps))
        #list[0] is the first object of heapnode list[0].item=element
        #list[0].fileHandler=filename for first object
    
    # sort the elemets first then on that basis sort the object(heapnode)
    # print(nums)
    heapq.heapify(nums)
    temp_sort=[]
    for num in nums:
        for obj in list_of_objects:
            if num==obj.item:
                temp_sort.append(obj)
    list_of_objects=[]
    list_of_objects=temp_sort
    temp_sort=[]
    # print(list_of_objects[1].item)
    count=0
    while True:
        # first object is minimum
        min_object=list_of_objects[0]
        if min_object.item==sys.maxsize:
            break
            
        sorted_output.append(min_object.item)
        #  #read another line from the same file
        ff=open(Path(min_object.fileHandler),'r')
        element=ff.readline().strip()
        lines=ff.readlines()
        open(Path(min_object.fileHandler), 'w').writelines(lines[0:])
        ff.close()
        if not element:
            element=sys.maxsize
        else:
            element=int(element)
        list_of_objects[0]=heapnode(element,ff.name)
        # print(list_of_objects[0].item)
        tem=[]
        tem=heapify(list_of_objects,0,len(list_of_objects))
        list_of_objects=tem
        list_of_objects=[]
        list_of_objects=tem
        count+=1
        if ans=='yes':
            if count==smallfilesize:
                out_file=open('output.txt','w')
                for temp_line in sorted_output:
                    out_file.write(str(temp_line)+'\n')
            else:
                out_file=open('output.txt','a')
                for temp_line in sorted_output:
                    out_file.write(str(temp_line)+'\n')               
            sorted_output=[]
            
    if answer!='yes':
        print(sorted_output)
    else:
        print('file produced at location: {}'.format(os.path.join(os.getcwd(),'output.txt')))

if __name__=='__main__':
    # written by xishan lone
    # means number of numbers =the no of elemts you want to generate
    inp=input("Enter the number of numbers to sort: ") 
    # means in what range do you want to generate numbers
    inp_2=input('Enter the rage of numbers to generate: ')
    # creates a file having numbers based on input
    create_hugefile(int(inp),int(inp_2))
    inp_1=input('Enter the chunk size: ')
    # splits the huge file in small files
    splitFiles('hugenumbers.txt',int(inp_1))
    answer=input('do you want to produce .txt output file by(external-sorting) enter yes or no: ')
    if answer=='yes':
        reading(answer,inp_1)
    else:
        reading(answer,inp_1)