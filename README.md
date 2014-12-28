ses
===

Simple Execution System - run centralized snippets from the commandline

ses helps running snippets of python code from centralized repositories. This can make it easier for sharing code that could be used for bootstrap projects, run daily tasks etc. There are currently one main repository(http://sunday.zone/ses/), but you can make your own reposititory, and distribute a modified *ses* file for your colleagues.

**Table of Contents**

- How does ses work
- Some use cases of ses
- Sunday.zone repository
- Running your own repository
- Adding your own repository to ses
- Upcoming features


How does ses work
-----------------

First you need to install ses by simply type the following in your command line

```
sudo wget https://raw.githubusercontent.com/Smarties89/ses/master/ses --output-document=/usr/local/bin/ses
sudo chmod +x /usr/local/bin/ses
```

Now you can install any snippets in the repositories by calling:

```
ses run <snippetname> <args>
```

e.g you want to bootstrap a python app called awesome_app
```
ses run bootstrappython awesome_app
```

Some snippets may have docstring information. If you want to see this you can use ```ses info <snippetname>```. E.g.
```
user@host:~/Documents$ ses info update
Trying repository 'http://localhost:6005'
Trying repository 'http://sunday.zone/ses/'
FOUND  update script!

    Updates ses to newest version. Executes the same commands as
    https://github.com/Smarties89/ses section "How does ses work"
```

If you want to see more snippets, there is a list command
```
user@host:~/Documents$ ses list
cleanlatex - Cleans common annoying temporary LaTeX files that some LaTeX compilers output.
testscript - used for testing purposes.
bootstrappython - bootstraps a default python environment with python-doit file for running, installing depedencies, run test.
...
``` 

Some use cases of ses
---------------------
Here are some use cases.

* You have some snippets that you can never find, they are on your github, in a folder, in another folder, etc. Make a pull request and add it. Then you can always find it, and share it with your friends.
* You are a team(or larger organisation) that have complex infrastructure. You make a repository for your internal company repository(just a HTTP server), which contains scripts for bootstrapping new software components, doing routine task, etc. Then you change the ses file to include your internal repository and distribute it to your colleagues.
* Ses is simple, so you can change it to fit your needs.

Sunday.zone repository
----------------------
Sunday zone is the default repository, and has so far the following scripts:

* **bootstrappython** - bootstraps a default python environment with python-doit file for running, installing depedencies, run test.
* **cleanlatex** - Cleans common annoying temporary LaTeX files that some LaTeX compilers output.
* **cleanubuntucrashes** - Deletes crash reports, so Ubuntu reporting system stops spamming.
* **installdockerubuntu** - Simple installer script for installing latest (working) version of docker(Wrapper for https://docs.docker.com/installation/ubuntulinux/#ubuntu-trusty-1404-lts-64-bit ).
* **thematrix** - The matrix.
* **update** - update ses to latest version by running the first two commands in section "How does ses work".

If you have a nice script, add it to the repo folder and make a pull request, and I will add it to the sunday.zone server

Running your own repository
---------------------------

Running your own repository is easy, since the only requirement is a HTTP server with exposing the scripts as files. Any HTTP server that will serve files will do. You can also use mine - which is a small script that starts a SimpleHTTPServer(Python). This is found in repo directory, and you should just call ```./run.bash```. Now, all you need to do, is adding your repository to a ses file and distribute it - see next section for this.


Adding your own repository to ses
---------------------------------

To add your own repository to ses, simply copy the ses file and edit the line 8 to 11 from
```
repos = [
"http://localhost:6005",
"https://sunday.zone/ses/",
"http://sunday.zone/ses/"

]
```
to
```
repos = [
"http://localhost:6005",
"https://sunday.zone/ses/",
"http://sunday.zone/ses/",
"http://myawesomedomain.io/sesrepository"
]
```
Now you can distribute your *ses* file in your organisation. Of course you can remove and change the order of repositories as it fit you, and your organisation

Upcoming features
-----------------

ses is far from complete, but it includes basic functionality making it useful for developers.
The plan for new features is the following:

* *ses search* command to search snippets.
* Some kind of usersystem for restricting download - not sure about how or if this is going to be implemented.
* More useful snippets
* Autocorrection of scripts - so **ses run clea\<TAB\>** will show list of possible scripts starting with *clea*.
