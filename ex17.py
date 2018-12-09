from sys import argv
from os.path import  exists

script,fromFile,toFile=argv

in_file=open(fromFile)
indata=in_file.read()

print(f"the fromFile's length is {len(indata)}")

print(f"is the {toFile} exist? {exists(toFile)}")

out_file=open(toFile,'w')
out_file.write(indata)

out_file.close()
in_file.close()
