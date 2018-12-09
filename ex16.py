from sys import argv

script,filename=argv
print(f"We're gonging to erase {filename}")
print("If you don't want that,hit CTRL-C")
print("If you want that,hit RETURN.")

#input("?")

target=open(filename,'w')
print("Truncate the file")
#target.truncate()

print("going to write something")

line1=input("line1: ")
line2=input("line2: ")

print(f"going to write something to {filename}")

target.write(line1)

target.write(" ")

target.write(line2)

target.close()
