Title: Limit the blast radius - Ansible
Date: 2020-02-27 19:39
Category: Ansible
Tags: Ansible, Python
slug: ansible-limit-blast-radius
Author: Jason Hall
status: draft
Summary: Keep the damage to a minimum when your automating your network

It's been said that automation is a good way to break things at scale. This is very true. If you realize, or not, in the middle of a play that something is not going the way you wanted it to this could trigger a CEE, Career Ending Event.  Neither you or I want to see that happen to anyone, or maybe you do? Not judging here, we all have our reasons.

## Check yo'self before you wreck yo'self
In Ansible there are ways that you can limit or prevent breakage.  The first of these is `--check`.  When your running your playbook for the first time in production, I would highly recommend you use the check option.  This will show you what the fruits of your labor are going to reap without actually reaping.  This is a good thing. It will tell you whats going to happen and hopefully you will see any fat finger mistakes you have made.

## Hitting the rev limitter
Before you go whole hog and turn this thing up to 11 lets start smalll.  Applying changes to a small subset is a good thing.  This allows you to do verifications on a per host or per group basis before the changes are spread across your entire environment.  Much like finding the "right" data model, inventory strategies can be a controversial subject and somewhat subjective.  If you're managing a small set of hosts apply the KISS methodology.  One hosts inventory file should get you by. Apply as many of the variables as you can in the group\_vars and stay very specific in the host\_var files. Lets look at some examples.

### Small'ish environment
For a small environment, say a small office, you may have a couple of core switches, a hand full of access swithces, and a wan router or two.
```yaml
all:
    hosts:
        wanrtr:
        coresw01:
        coresw02:
        accssw01:
        accssw02:
        accssw03:
    children:
        wan:
            hosts:
                wanrtr01:
                wanrtr02:
        core:
            hosts:
                coresw01:
                coresw02:
        access:
            hosts:
                accssw01:
                accssw02:
                accssw03:
        nxos:
            children:
                core:
                access:
        ios:
            children:
                wan
```
There, thats a good example of a network just barely large engough to automate.  The astute amongst you will notice there are no variables defined in the inventory file.  I try an refrain mixing in variables into the inventory directoy and puth them in their corresponding host and group var files.


[Targeting hosts with patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html)

[Passing extra vars on the command line](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#passing-variables-on-the-command-line)
