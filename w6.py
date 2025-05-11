#create, append, and remove lists in Python.
#creating an empty list
empty_List=[]
print("Empty List is:", empty_List)
#creating a list with elements 
my_List=[10,507,"python"]
print("created list is:",my_List)
#Inserting new elements using append()
my_List.append(20)
my_List.append("program")
my_List.append([3,7])
print("After adding elements the new list is:",my_List)
#deleting elements using pop() method
d1=my_List.pop()
d2=my_List.pop(2)
#deleting the elements using remove
my_List.remove(10)
print("After deleting elements the new list is:",my_List)
#Removing all the elements using clear() 
print("After removing all the elements the new list is:",my_List)

#write a program to demonstrate working with tuples in python
#creating an empty tuple
empty_tup=()
print("Empty tuple=",empty_tup)
#creating single element tuple
single_tup=(10,)
print("single element tuple=",single_tup)
#creating a tuple with multiple elements 
my_Tup=(10,3.7,'program','a')
print("Tuple with multiple elements is:",my_Tup) 
print("Length of the tuple is:",len(my_Tup)) 
T1=(10,20,30,40,70.5,33.3)
print("Maximum value of the tuple T1 is:",max(T1))
print("Minimum value of the tuple T1 is:",min(T1)) 
str1='tuple'
T=tuple(str1)#convering string into tuple
print("After converting a string into tuple,the new tuple is:",T)
L=[2,4,6,7,8]
T2=tuple(L)#convering string into tuple
print("After converting a List into tuple,the new tuple is:",T2)


#write a program to demonstrate working with dictionaries in python
#empty dictionary
my_dict={}
print("Empty dictionary is:",my_dict)
#dictionary with integer keys 
my_dict={1:'apple',2:'ball'}
print("dictionary with integer keys",my_dict)
#dictionary with mixed keys
my_dict={'name':'rishi',1:[2,4,3]}
print("dictionary with mixed keys",my_dict)
#using dicy.fromkeys()
my_dict=dict.fromkeys("abcd",'alphabet')
print("dictionary created by using dict.fromkeys method=",my_dict)
#using get method 
my_dict={'name':'jack','age':25}
print(my_dict['name']) #ouput jack
#changing and adding dictionary elements
my_dict['age']=18 #upadte vaue
my_dict['class']="B.Tech" #updating vlaue
print("After changing and adding the values,the new dictionary=",my_dict)
#using items()
print("items in the dictionary is:",my_dict.items())
#using keys() 
print("Keys in the dictionary is:",my_dict.keys())
#using values() 
print("Values in the dictionary is:",my_dict.values())

#Write a program to demonstrate a) arrays b) array indexing such as slicing, integer
#array indexing
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("entered array is:",a,"and its dimension is:",a.ndim)
print("entered array is:",b,"and its dimension is:",b.ndim)
print("entered array is:",c,"and its dimension is:",c.ndim)
print("entered array is:",d,"and its dimension is:",d.ndim) 

#)array indexing such as slicing, integer array indexing and Boolean array indexing
import numpy as np
a=np.arange(10,1,-2)
print("a sequential array with nagative step value:",a)
newarr=[a[3],a[1],a[2]]
print("elements at these indices are:",newarr) 
a=np.arange(20)
print("Array is:",a)
print("a[-8:17:1]=",a[-8:17:1]) 
print("a[10:]=",a[10:]) 


#mean, median, mode
import numpy as np
a= np.array([[1,23,78],[98,60,75],[79,25,48]])
print("Entered array=",a) 
#Minimum Function
print("minimum=",np.amin(a))
#Maximum Function
print("maximum=",np.amax(a))
#Mean Function 
print("mean=",np.mean(a))
#Median Function 
print("median=",np.median(a))
#std Function 
print("standarad deviation=",np.std(a))
#var Function 
print("variance=",np.var(a))
