formatter="{} {} {}"

print(formatter.format(1,3,2))
print(formatter.format("1,","2.","3"))

print("""
123
2342
3411324,
2343242,
4124
""")
#rint("how old are you?",end='')
#age=int(input("your age?"))

#print(f"you are {age} old")

from sys import argv

script,filename=argv

txt=open(filename,mode='a')

print(f"Here is your file {filename} ")
print(txt.write("jdfklsj"))

print("input your file again")

file_again=input(">")

print(f"your third argument is {file_again}")

txt_again=open(file_again)
print(txt_again.read())
print(txt_again.close())
