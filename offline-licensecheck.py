# -*- coding: utf-8 -*-
# Copyright (C) 2018, Vipul Gupta

# This file is part of SugarPort.

# The program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# The program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
 Data such as missing license mentions, missing links from
 help activity, missing sections etc. In addition to this, ensuring that
 activity.info file is consistent and containing all information needed

 It does something like this - clones the fork, switches to develop
 branch, makes a .xo, runs the build script, the .xo file name needs to
 be written manually, then it unzips it, then licensechecks and then
 check if necessary files and directory are present or not. When done
 opens a window in the default browser to make a PR.
'''

import configparser
import os
import time
import webbrowser
import subprocess
from zipfile import ZipFile
from pathlib import Path

# Getting ready
def initialise():
    subprocess.call(['python', 'setup.py', "dist_xo"])
    subprocess.call(['python', 'setup.py', "build"])
    print("------------------------------------\n")


# opening the zip file in READ mode
def extractzip():
    # specifying the zip file name that was created of the setup
    x = raw_input("Enter file name = ")
    file_name = activity + "/dist/"+ x +".xo"
    with ZipFile(file_name, 'r') as zip:
        os.chdir(activity + '/dist/')
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
        print("------------------------------------\n")


# LicenseCheck
def licensechecks():
    z = activity + '/dist/'
    subprocess.call(['licensecheck','--recursive',z])
    print("------------------------------------\n")


# Checking through activity.info
def analyse_activityinfo():
    '''Return True if the repository has a license field in
    activity/acitvity.info, else false'''
    if os.path.exists(activityFile):
        cp = configparser.ConfigParser()
        cp.read(activityFile, encoding='utf-8')
        print("Going through activity.info file")
        try:
            for option in OPTIONS:
                print('{}.{:<20}  : {}'.format(ACTIVITY_SECTION, option, cp.has_option(ACTIVITY_SECTION, option)))
                time.sleep(.3)
                if (option=='exec'):
                    print("--------------------------------------------")
                if (option=='repository'):
                    if not cp.has_option(ACTIVITY_SECTION, 'repository'):
                        r = open(activityFile,"a")
                        r.write("\nrepository = https://github.com/sugarlabs/" + x )
                        r.close()
                        print("Repository Replaced")
                if (option=='website'):
                    if cp.has_option(ACTIVITY_SECTION,'website'):
                        print("PROBLEM in URL")
                if (option=='url'):
                    if not cp.has_option(ACTIVITY_SECTION,'url'):
                        url2 = "https://help.sugarlabs.org"
                        webbrowser.open_new_tab(url2)

            print("------------------------------------\n")
        except configparser.NoSectionError as err:
            print(err)


# Finding COPYING file
def findLicense():
    try:
        l = [w for w in os.listdir("./") if "COPYING" in w]
        print("COPYING file found in the repo.\n{}".format(l))
    except Exception as e:
        print(e)
        print("COPYING file not found in the repo.\n")


# Making a .gitignore
def giti():
    giti = Path(activity + "/.gitignore")
    wines = ["*.pyc\n","locale/\n","dist/\n","*.patch\n","*.bak\n","*.swp\n","*~\n"]
    with open(".gitignore","w") as g:
        f = g.readlines()

        if not giti.exists():
            print(".gitignore not present in the repository hence replacing")
            g.writelines(wines)
        else:
            with open(".gitignore","r") as f:
                z = f.readlines()
                if not "locale/" in z:
                    print("Entities not found, replacing")
                    g.writelines(wines)


# Finding if screenshots exist
def screenshot():
    shot = Path(activity + "/screenshots")
    if shot.exists():
        print("\n Screenshots directory found in the repo \n")
    else:
        print("Screenshots directory NOT found in the repo")
        u = open('/home/vipulgupta2048/Desktop/note.txt', "a")
        u.write(x)
        u.close()
        print("Noting it down")
        print("------------------------------------\n")


# Making a PR
def openurl():
    print('Opening {} '.format(url))
    webbrowser.open_new_tab(url)


# Repo Caller
set = []

# Control panel
for x in set:
    url = https://www.github.com/vipulgupta2048/ + x
    subprocess.call(['git','clone','--recursive', url])
    path = "/home/vipulgupta2048/SUGAR/ready/" + x
    os.chdir(path)
    subprocess.call(['git','checkout','-b','develop'])
    activity = os.getcwd()
    print ("We are in {}".format(activity))

    activityFile = activity + '/activity/activity.info'
    ACTIVITY_SECTION = 'Activity'
    OPTIONS = [
    'name', 'activity_version', 'bundle_id', 'license', 'icon', 'exec',
    'mime_types', 'update_url', 'max_participants',  'show_launcher',
    'categories', 'category' ,'single_instance', 'website', 'url',
    'tags','summary','repository',]

    initialise()
    extractzip()
    licensechecks()
    analyse_activityinfo()
    findLicense()
    screenshot()
    y='r'
    while(y=='r')
        y = raw_input("Ready to PR (y) Check again (r) = ")
        if (y=='y'):
            openurl()
        elif (y=='r'):
            licensechecks()
            analyse_activityinfo()
            findLicense()
            screenshot()
