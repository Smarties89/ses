ses
===

Simple Execution System - run centralized snippets from the commandline

ses helps running snippets of python code from centralized repositories. This can make it easier for sharing code that could be used for bootstrap projects, run daily tasks etc. There are currently two repositories http://localhost:6005 and http://sunday.zone/ses/, but you can change whatever you like and make your own repositority and distribute the *ses* file for your colleagues.


How does ses work
-----------------

First you need to install ses by simply type the following in your command line

```
sudo wget https://raw.githubusercontent.com/Smarties89/ses/master/ses --output-document=/usr/bin/ses
sudo chmod +x /usr/bin/ses
```

Now you can install any snippets in the repositories by calling:

```
ses run <snippetname> <args>
```

e.g you want to bootstrap a python app called awesome_app
```
ses run bootstrappython awesome_app
```

Sunday.zone repository
----------------------
Sunday zone is the default repository, and has so far the following scripts:

* **bootstrappython** - bootstraps a default python environment with python-doit file for running, installing depedencies, run test.
* **cleanlatex** - Cleans common annoying temporary LaTeX files that some LaTeX compilers output.
* **thematrix** - The matrix.
* **installdockerubuntu** - Simple installer script for installing latest (working) version of docker(Wrapper for https://docs.docker.com/installation/ubuntulinux/#ubuntu-trusty-1404-lts-64-bit ).

Running your own repository
---------------------------

Running your own repository is easy, since the only requirement is a HTTP server with exposing the scripts as files. Any HTTP server that will serve files will do. You can also use mine - which is a small script that starts a SimpleHTTPServer(Python). This is found in repo directory, and you should just call ```./run.bash```. Now you need to add your repository to ses - see next section for this.


Adding your own repository to ses
---------------------------------

To add your own repository to ses, simply copy the ses file and edit the line 8 to 11 from
```
repos = [
"http://localhost:6005",
"http://sunday.zone/ses/"
]
```
to
```
repos = [
"http://localhost:6005",
"http://sunday.zone/ses/",
"http://myawesomedomain.io/sesrepository"
]
```
Now you can distribute your *ses* file in your orginasation.
