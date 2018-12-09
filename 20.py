from sys import argv

script ,input_file=argv

#能够读的就是文件对象
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

#得到文件对象
current_file=open(input_file)

print_all(current_file)

rewind(current_file)

print_a_line(1,current_file)
print_a_line(2,current_file)

print_a_line(3,current_file)
