####1. Write a function which returns sum of the list of numbers

def sumlist(lis):
    listout=0
    for i in range(0,len(lis)):
        listout=listout+lis[i]
    return listout
    
    
lis=[1,3,3,]
out=sumlist(lis)
print("sum of all the numbers inside list: -",out)

### 2. Write a function in python in python, which will return maximum i.e function should return dictionary

def maxv(dicts):
    mkey=max(dicts,key=dicts.get)
    value=dicts.values()
    mvalue=max(value)
    mydict=dict([(mkey,mvalue)])
    return mydict

dicts={1:105,2:102,3:98}
out=maxv(dicts)
print("dictionary of contain maximum value is : -", out)

### 3 . Write a python function to the number of maximum consecutive  one’s present in the array. 
def getMaxLength(arr): 
    n = len(arr) 
    count = 0 

    result = 0 
  
    for i in range(0, n): 

        if (arr[i] == 0): 
            count = 0
        else: 
            count+= 1 
            result = max(result, count)  
          
    return result  

arr=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

out=getMaxLength(arr)
print("maximum consecutive number one's present in array: ", out)



### for answer in number 4 please open app.py and run that