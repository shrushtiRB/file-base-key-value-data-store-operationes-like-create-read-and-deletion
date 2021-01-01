import threading 

from threading import*
import time

dic={} #'dic' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dic:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(a[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(a[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]: #comparing the current time with expiry time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del dic[key]
            print("key is successfully deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    a=dic[key]
    if a[1]!=0:
        if time.time()<a[1]:
            if key not in dic:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(a[1])
                dic[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dic:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(a[1])
            dic[key]=l
