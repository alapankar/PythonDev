import os
os.chdir('D:\Python Apps\Mywishlist')
print (os.getcwd())
#
# planets=['The Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
#
# for i in range(1,11):
#     filename=planets[i-1]+' - Our Solar System - '+'#'+str(i)+'.txt'
#     with open(filename, 'w') as wf:
#         wf.write('')

for file in os.listdir():
    filename, fileext=os.path.splitext(file)
    file1, file2, file3= filename.split('-')
    file1=file1.strip()
    file2=file2.strip()
    file3=file3.strip()[1:].zfill(2)
    finalfilename=f'{file3}-{file1} {file2}'
    os.rename(file, finalfilename)

