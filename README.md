ses
===

Simple Execution Environment - run snippets from the commandline

ses helps running snippets of python code from centralized repositories. This can make it easier for sharing code that could be used for bootstrap projects, run daily tasks etc. There are currently localhost:6005 and http://sunday.zone/ses/ as repositories, but you can change whatever you like and make your own repositority and ses file for your colleagues.


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
Sunday zone is the default repository.

* **bootstrappython** - bootstraps a default python environment with python-doit file for running, installing depedencies, run test.
* **cleanlatex** - Cleans common annoying temporary LaTeX files that some LaTeX compilers output.

