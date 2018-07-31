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
**SugarPort** started out as WikiPort before I was retasked to work on a similar project with a different aim of setting up the new Activity Server for Sugar Labs called **ASLOv3**. This repository will work as a holdout till the project is ready for all the scripts and code that would be written for its deployment.

**[Sugar Labs](https://sugarlabs.org/)** is a community-run software project whose mission is to produce, distribute, and support the use of **Sugar**, an open source desktop environment and learning platform. Sugar Labs is a member of the **Software Freedom Conservancy**, an umbrella organization for free software (FLOSS) projects. Sugar is widely used by children from under-developed countries, as a medium to learn new things from and improve their skills. 

**Sugar Labs** also participates in **Google Code-in**, **Google Summer of Code** which serves as an outlet for young programmers. 

(_Edited from [Wikipedia](https://en.wikipedia.org/wiki/Sugar_Labs)_)

## Aim
To fix activity metadata by the end of Summer 2018 to facilitate the developement and deployment of the new activity server, ASLOv3 (i.e August according to the timeline given by Google)

## Work Done
- For the successful deployment of ASLOv3, the activity metadata is added/updated in the activity repositories for correct information to be displayed on the web portal. (All 161+ of them present at [sugarlabs](www.github.com/sugarlabs) More details about this are present in the Sugar Tracker. [Refer #`]

- A script automates analyzing repositories present on GitHub using PyGitHub and GitHub API. Parse them with ConfigParser finding parameters that are missing and storing the clean output in a separate file for future reference. This method is the online way of doing things. A bit slow as GitHub induces a delay in API calls hence creating a bottleneck that is not feasilble for out project.

- This was overcome by the bypassing the fixing that was being done online to the fixing these repositories now in the local system of the user as we clone them through an automated script and run multiple checks and processes on them. 

- After analysis gets completed, activities are fixed with their metadata updated as necessary. The changes are either pushed manually or automatically (Alpha) to the fork to create a pull request and suggest changes in the codebase.

## Testing 
1. Fork and clone this repository 
```
git clone [Forked repository URL]
```

2. Create and activate a virtual environment preferably through Python3

```
python3 -m virtualenv env
source env/bin/activate
```
	
3. Install the requirements listed in the `requirements.txt` file

```
pip install -r requirements.txt
``` 

From here we can use both the analysis scripts, further instructions followed are first for online and later for the offline script. 

### Online Script

1. You would be needing a GitHub API access token, refer to this [tutorial](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) for generating your personal token.
2. Open the `online-checker.py` and enter the token where listed. 
3. Run the script using the command. 

```
python3 -u repo-statuschecker.py | tee output.txt
```

4. It takes time to execute completely, after execution you will find output.txt showing you the results of the analysis. 
  
### Offline Script
To be added.

## License
The source code is under [GPLv3 or later](https://github.com/vipulgupta2048/SugarPort/blob/master/LICENSE)

