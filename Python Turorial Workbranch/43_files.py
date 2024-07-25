

# # files and models 

# r w a 
# file handle 
# r+ (read and write ) ,   w+ (write and read ) ,  a+ (append and read )




# -------------------------exercises---------------

# read

f=open("44-test.txt","r")

print(f.read())

f.close()


# write 

f=open("44-test.txt","w")

print(f.write("hiii"))

f.close()


# append

f=open("44-test.txt","a")

print(f.write("this is mehdi "))

f.close()



# ----------------changing types of modes-----------



# r+
f=open("44-test.txt","r+")
print(f.read())
f.write("damnnnnnnnnnn you writed ")

f.close()





# w+

f=open("44-test.txt","w+")
f.write("mr.coroger")
f.tell()
f.seek(0)
print(f.read())

f.close()





# a+
f=open("44-test.txt","a+")
f.write("damnnnnnnnnnn you writed ")
print(f.read())
f.close()




