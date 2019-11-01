Title: Moving around on the Linux CLI
Date: 2019-11-1 2019 13:06
Category: Linux
Tags: linux, cli, basics
slug: moving-around-on-the-linux-cli
Author: Jason Hall
status: draft
Summary: Getting familiar with the Linux CLI

## Get your bearings 
Knowing where you are at in the world when trying to navigate somewhere is
important, like really important, trust me. You can't plot a course to somewhere
until you know where you're starting from. So lets look at a couple commands
that will tell you where your at.

The first up is `pwd` or Print Working Directory.  This will tell you where you
are at in the file system.
```shell
jdhall@BLUE02:~$ pwd
/home/jdhall        
jdhall@BLUE02:~$
```

Alright, so here we are.. Somewhere over the middle of the Earth.  This is the
absolute path from what is called the **root** of the directory tree often
represented by a single forward slash, `/`.  A quick aside, this `/` is a
forward slash.  This `\` is a back slash.  Remember these, when explaining things
or paths, URLs, etc to other people verbally it is important to have your slashes straight.
Onward! So, here we are in my home directory. __Welcome__! Let me show you
around a little.

Lets take a look at where we can go from the from here using `ls`, short for
list.  This will give you a list of all the directories and files currently in my home.

```shell
jdhall@BLUE02:~$ ls
pw  repo  vim_plugin_cheater.txt
jdhall@BLUE02:~$
```

It's a modest house, kind of minimalist if you will.  I like to keep things
cleaned up.  But, I mean, what are these things?  Are they items in the rooms, files, or
are they other rooms, directories?  Lets take a more in depth look at the "room".

```shell
jdhall@BLUE02:~$ ls -l
total 12
-rw-r--r-- 1 jdhall jdhall   13 Jan 17  2019 pw
drwxr-xr-x 3 jdhall jdhall 4096 Sep 11 16:43 repo
-rw-r--r-- 1 jdhall jdhall 3448 Nov  1 12:45 vim_plugin_cheater.txt
jdhall@BLUE02:~$
```
If we look at the first column we can get a clue to what these things are.

```
Field 1 Field 2 Field 3 Field4
d		rwx		r-x		r-x
```

### Field 1 - File Type
This is the type of file it is.  Some of the options that it could be are:

* `l` - link (like a windows shortcut)
* `d` - directory
* `c` - character device
* `p` - pipe or fifo (First In First Out)
* `-` \- a place holder for when its actually just a file

There are quite a few of these. I can think of them all, but these are a few of
them that you may run into if you really start tinkering with Linux.

### Field 2 - Owner Permissions
These are the owners permissions on the file. 
* r - read
* w - write
* x - execute

### Field 3 - Group permissions 
The files and directories have have permissions for both the user(owner) and the
group the file belongs to. So you may have owner permissions of read and write,
but members of the group a file belongs to may only be able to read the file.
You can see those exact permissions on both the `pw` and
`vim_plugin_cheater.txt` files.

### Field 4 - Others Permissions
For users that aren't the owner or in the group these are the permissins that
are applied to them. 


