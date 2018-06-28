from zipfile import ZipFile
import os
# specifying the zip file name
#~ file_name = input("Enter file name")
file_name = "CookieSearch-10.xo"
activity = "cookie-search-activity"
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
    #~ os.mkdir("temp")
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    path = "~/vipulgupta2048/SUGAR/" + activity + '/' + 'dist/'
    os.chdir(path)
    command = 'licensecheck dist/*'
    os.system(command)
    print('Done!')
