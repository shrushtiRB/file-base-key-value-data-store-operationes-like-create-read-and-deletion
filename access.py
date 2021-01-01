#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import code1 as s 
#importing the main file("code" is the name of the file I have used) as a library 


s.create("shrushti",)
#to create a key with key_name,value given and with no time-to-live property


s.create("ravinath",50,6300)

#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


s.create("bhange",40)

s.read("shrushti")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


s.read("ravinath")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


s.create("bhange",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


s.modify("bhange",55)
#it replaces the initial value of the respective key with new value 

 
s.delete("shrushti")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
