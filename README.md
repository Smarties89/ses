ses
===

Simple Execution System - run centralized snippets from the commandline


**This is not maintaned anymore**

ses helps running snippets of python code from centralized repositories. This can make it easier for sharing code that could be used for bootstrap projects, run daily tasks etc. There are currently one main repository(https://sundayzone.com/ses/), but you can make your own reposititory, and distribute a modified *ses* file for your colleagues. You can see a list of the main public repository at https://github.com/Smarties89/ses/blob/master/sundayzonerepository.MD

**Table of Contents**

- Features
- How does ses work
- Some use cases of ses
- Running your own repository
- Adding your own repository to ses
- Upcoming features
- Design considerations


Features
--------

- Easy to run snippets from central repositories
- Ses file is small, easy to install, easy to modify, and very compatabile.
- Repositories can be any fileserveing http server.
- List all snippets in all repositories
- Find information about each individual snippet.
- Works on Linux, Mac, and soon Windows

How does ses work
-----------------
Ses can be run as local user, but installing it to e.g. */usr/local/bin* helps you run snippets even faster.

**Linux install**

```
sudo wget https://raw.githubusercontent.com/Smarties89/ses/master/ses --output-document=/usr/local/bin/ses
sudo chmod +x /usr/local/bin/ses
```

**Mac install**
```
sudo curl "https://raw.githubusercontent.com/Smarties89/ses/master/ses" -o "/usr/local/bin/ses"
sudo chmod +x /usr/local/bin/ses
```

**Running snippets**

Now you can run any snippets in the repositories by calling:

```
ses run <snippetname> <args>
```

e.g you want to bootstrap a python app called awesome_app
```
ses run bootstrappython awesome_app
```

**Docstring information**

Some snippets may have docstring information. If you want to see this you can use ```ses info <snippetname>```. E.g.
```
user@host:~/Documents$ ses info update
Trying repository 'http://localhost:6005'
Trying repository 'http://sunday.zone/ses/'
FOUND  update script!

    Updates ses to newest version. Executes the same commands as
    https://github.com/Smarties89/ses section "How does ses work"
```

**Listing all snippets available**

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

* You have some snippets that you can never find, they are on your github account, in a folder, or in another folder, etc. Add the snippet to this github page and make a pull request. Then you can always find it, and share it with your friends. If you have many specialized snippets, you can also make your own repository and add them there.
* You are a team(or a larger organisation) that have complex infrastructure. You make a repository for your internal company repository(just a HTTP server), which contains snippets for bootstrapping new software components, doing routine task, etc. Then you change the ses file to include your internal repository and distribute it to your colleagues.
* Ses is simple, so you can change it to fit your needs.


Running your own repository
---------------------------

Running your own repository is easy, since the only requirement is a HTTP server that supports exposing the snippets as files. Any HTTP server that will serve files will do. You can also use mine - which is a small script that starts a SimpleHTTPServer(Python). This is found in repo directory, and you should just call ```./run.bash```. Now, all you need to do, is adding your repository to a ses file and distribute it - see next section for this.


Adding your own repository to ses
---------------------------------

To add your own repository to ses, simply copy the ses file and edit the line 8 to 11 from
```
repos = [
"http://localhost:6005",
"https://sundayzone.com/ses/",
"http://sundayzone.com/ses/"

]
```
to
```
repos = [
"http://localhost:6005",
"https://sundayzone.com/ses/",
"http://sundayzone.com/ses/",
"http://myawesomedomain.io/sesrepository"
]
```
Now you can distribute your *ses* file in your organisation. Of course you can remove and change the order of repositories as it fit you, and your organisation. E.g. the repository could be defined as following:
```
repos = [
 "http://myawesomebusiness.io/sesrepository"
]
```
which could comply with some organisations rules that requires snippets to be validated.

Upcoming features
-----------------

The plan for new features are the following:

* *ses search* command to search snippets.
* Some kind of usersystem for restricting download - not sure about how or if this is going to be implemented.
* More useful snippets.
* Autocorrection of snippet - so **ses run clea\<TAB\>** will show list of possible snippets starting with *clea*.
* Maybe some kind of explicit cache mechanism, so running snippets does not demand Internet.
* Make it more compatible, by testing different Python environments.

The plan is pretty loose, so it will properly change.

Design considerations
---------------------

ses is designed after certain principles. If you want to make changes to the ses file(not the repository), then you should strive for:

* Making it simple to understand and change(if other people feel needed).
* Make use of **no** extern libraries.
* Make sure you use features/method/classes there are in older/newer version of Python.

In other words, ses should be as compatible as possible, as it might run on Python 2.x, where x is low or Python 3.x.
