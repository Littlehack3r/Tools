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

x = "/home"
print ("one")
#x = os.getcwd()
#f = open( x, "r")

new_data = "" 

def reverse(file):

    f = open(file, "r")

    for line in f.readlines():
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
        print(line)
        new_data += line 
    
    f.close()

#reverse random lines
#Cannot use the rev command to correct file
#Aggressive punishment
def randReverse(f):
    lines = open(f).read().splitlines()
    
    for line in f.readlines():
       
        if len(line) == 0:
            new_data += "\n"
            continue

        #store comments
        if line.startswith("#"):
            new_data += line
            continue


    myline =random.choice(lines)
    myline = [myline[::-1] for lines in line]  
    new_data += myline 

    f.close()


#reverse /etc/hosts
if x == "./hosts":
    
    f = open( x, "r")
    
    for line in f.readlines():

        #skip and store blank lines
        if len(line) == 0:
            new_data += "\n"
            continue

        #store comments
        #Comments will not be reversed
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

#specific files in directory 

if x == "/home":
  #  print("two")

    path = "/Users/loveofmyfuckinglifewow/Tools/home"
    
    for file in os.listdir(path):
       # print("three")
       # print(file)
        if file.endswith('.txt'):
           # print(file)
            reverse(file)
        




print(new_data)
#f = open(x, "w")
#f.write(new_data)
#f.close() 