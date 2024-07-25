


# -------------------------exercises---------------

# read

f=open("14-2 files.txt","r")

print(f.read())

f.close()


# write 

f=open("14-2 files.txt","w")

print(f.write("hiii"))

f.close()


# append

f=open("14-2 files.txt","a")

print(f.write("this is mehdi "))

f.close()



# ----------------changing types of modes-----------



# r+
f=open("14-2 files.txt","r+")
print(f.read())
f.write("damnnnnnnnnnn you writed ")

f.close()





# w+

f=open("14-2 files.txt","w+")
f.write("mr.coroger")
f.tell()
f.seek(0)
print(f.read())

f.close()





# a+
f=open("14-2 files.txt","a+")
f.write("damnnnnnnnnnn you writed ")
print(f.read())
f.close()




