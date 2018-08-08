                              ____                         ____            _   
                             / ___| _   _  __ _  __ _ _ __|  _ \ ___  _ __| |_ 
                             \___ \| | | |/ _` |/ _` | '__| |_) / _ \| '__| __|
                              ___) | |_| | (_| | (_| | |  |  __/ (_) | |  | |_ 
                             |____/ \__,_|\__, |\__,_|_|  |_|   \___/|_|   \__|
                                          |___/                                

[![HitCount](http://hits.dwyl.io/vipulgupta2048/sugarport.svg)](http://hits.dwyl.io/vipulgupta2048/sugarport) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


All source code related to the project that was used and made for Google Summer of Code 2018 under Sugar Labs is housed here. 
**Project Details** - [GSoC Official Website](http://tiny.cc/vgsoc) | Blogs - **Mixster** --> [GSoC#2018](https://mixstersite.wordpress.com/gsoc2018/) | **Progress Tracker** and meeting MoM's - [Sugar Tracker](https://docs.google.com/document/d/1VdzjA-DnEBh0ntHY17ktXlp7c2pIofq8458gSCTwiSM/edit?usp=sharing)

## Introduction
**SugarPort** started out as WikiPort before I was retasked to work on a similar project with a different aim of setting up the new Activity Server for Sugar Labs called **ASLOv3**. This repository will work as a holdout until the project is ready for all the scripts and code that would be written for its deployment and maintenance.

**[Sugar Labs](https://sugarlabs.org/)** is a community-run software project whose mission is to produce, distribute, and support the use of **Sugar**, an open source desktop environment and learning platform. Sugar Labs is a member of the **Software Freedom Conservancy**, an umbrella organization for free software (FLOSS) projects. Sugar is widely used by children from under-developed countries, as a medium to learn new things from and improve their skills. 

**Sugar Labs** also participates in **Google Code-in**, **Google Summer of Code** which serves as an outlet for young programmers. 

(_Edited from [Wikipedia](https://en.wikipedia.org/wiki/Sugar_Labs)_)

## Aim
The aim of the project is to fix metadata of programs called as **activities** that run on the Linux-based distro, Sugar, and other related platforms to facilitate the development and deployment of the new activity server, ASLOv3. 

_Extended work, also includes the deployment of the activity server. Hence the work for the same will be done parallelly._

## Work Done
- To properly deploy **ASLOv3**, the activity metadata is fixed in activity repositories hosted on Github under the organization, **SugarLabs**. With correct metadata, accurate information can be displayed on the web portal. 
( Stats - There are about 161+ activities present. Out of them, only 84 are working. )

- Hence, to automate analyzes and fixing of metadata, Python scripts were created that work as a **Repo-Analyzer** online and offline separately to facilitate the fixing of scripts.

- **Online_checker.py** uses PyGitHub and GitHub APIv3 to parse data through ConfigParser finding parameters that are missing and storing the clean output in a separate file for future reference. This method is the online way of doing things. A bit slow as GitHub induces a delay in API calls hence creating a bottleneck that is not feasible for our project. Hence, I had to find a way around it. 

- **offline_license.py** - Clones repositories and runs multiple checks and processes on user-defined parameters on the activity. These are very flexible and easy to maintain. After analysis gets completed, activities are fixed with their metadata updated as necessary.

The offline checker makes it easier and more efficient to fix activity metadata with least manual work involved.  The changes are either pushed manually or automatically (Alpha phase) to the fork that was created of the upstream GitHub repo to create a pull request and suggest changes in the codebase. The repo-caller function has been tested with over 50 activities at once. 

*For a detailed methodology behind the scripts, [refer here](https://docs.google.com/document/d/1VdzjA-DnEBh0ntHY17ktXlp7c2pIofq8458gSCTwiSM/edit?disco=AAAABzrX54M). 
*
# Testing (For Ubuntu 16.04 or above)
-  Fork and clone this repository 
```
git clone [Forked repository URL]
```

- Create and activate a virtual environment preferably through Python3

```
python3 -m virtualenv env
source env/bin/activate
```
    
- Install the requirements listed in the `requirements.txt` file

```
pip install -r requirements.txt
``` 

From here we can use both the analysis scripts, further instructions followed are first for online and later for the offline script. 

### Online Script (GitHub APIv3 + PyGitHub)

- A GitHub API access token would be needed for authentication, hence refer to this [tutorial](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) to generate a personal token.
- Open the `online_checker.py` and enter the token where listed. 
- Run the script using the command. 

```shell
python3 -u online_checker.py | tee output.txt
```

- It takes time to execute completely. After execution, output.txt is generated containing the result of the analysis. 
  
### Offline Script (ConfigParser + OS + Subprocess)
 
- Run the script using the command. 
```shell
python3 -u offline_checker.py | tee output.txt
```
- Enter your `GitHub` username when prompted. 
- Enter one or more repository names that you have forked when prompted (Press `enter` to stop adding to the list)
- Every repository listed which is forked under the username provided will be cloned. 
- Fix the errors and anomalies listed, get the changes committed and pushed to your fork. When ready, press either 'r' to run the tests again or 'y' to make a pull request. 
- When the list is exhausted, and the script has finished execution output.txt is generated containing the result of the analysis.

## License
The source code is under [GPLv3 or later](https://github.com/vipulgupta2048/SugarPort/blob/master/COPYING)
