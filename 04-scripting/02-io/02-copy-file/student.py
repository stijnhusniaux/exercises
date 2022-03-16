import sys,shutil

shutil.copy(sys.argv[1],sys.argv[2])

# with open(sys.argv[1],'r') as file:
#     with open(sys.argv[2],'w') as file2:
#         file2.write(file.read())
#         print(file.read())
