import os
from sys import argv
 
def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter
 
legend = {
'.png':'.jpg',
'.jpeg':'.jpg',
}
 
for file_old in os.listdir('.'):
 
    file_new = latinizator(file_old, legend)
 
    #Uncomment to capitalize first letter of filename
    #file_new = file_new.capitalize()
 
    if '-p' in argv:
        if file_old == file_new:
            print ('{0: <30}'.format(file_old), 'will not be renamed' )
        else:
            print ('{0: <30}'.format(file_old), 'will be renamed to ', file_new )
    else:
        if file_old != file_new:
            print ('{0: <30}'.format(file_old), 'renamed to ', file_new )
            os.rename(file_old, file_new)
 
input("Расширение файлов изменено. Нажмите Enter для закрытия окна")

#lisakov
#softy_plug