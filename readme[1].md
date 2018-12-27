# **Log Analysis Project**

This is a project for FULL STACKS WEB-DEVELOPER NANO DEGREE

## **Project Description**

It is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

- Q1. What are the most popular three articles of all time?
- Q2. Who are the most popular article authors of all time?
- Q3. On which days did more than 1% of requests lead to errors?

## **Prerequisite**

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

**Use a terminal**

You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

**Install VirtualBox**

VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

**Install Vagrant**

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

**Download the VM configuration**

We can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

**Start the virtual machine**

From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

## **Running The Project**

- Run vagrant up
- Run vagrant ssh
- Change the directory to the vagrant file
- Run the python file log_analysis.py

