# Written with love by Thatyana Morales
# This script compiles all gathered hashes that are stored in the log folder of
# Responder. After running Responder, navigate to the logs file and ensure this
# script is in the same directory as the resulting .txt files (the ones with the
# form of Protocol-IP.txt).
# Run the following on the command line once you're in the same directory:
# python -u ResponderLog.py [domain name]
# Output will be text files of each unique protocol name with the
# _MasterList.txt attached.
# This works for NTLMv1 and NTLMv2 hashes


import os, sys

domainName = sys.argv[1] #name of domain, which is the parameter passed when executing the script

for file in os.listdir(os.path.dirname(os.path.abspath(__file__))): #cycles through files in the directory
    if (file.endswith(".txt") and ('MasterList.txt' not in file)): #grabs only the results (with .txt extension), excluding MasterLists
        protocolName = file[:(file.find('-', file.find('-')+1))] + '_MasterList.txt' #extracts only the protocol name from the .txt file

        if os.path.exists(protocolName):
            fileMode = 'a' # append if it exists already
        else:
            fileMode = 'w' # create file if doesn't exist

        protocolFile = open(protocolName, fileMode) #open protocol-specific MasterList

        originalFile = open(file, 'r') #open original .txt file

        for line in originalFile:
            if line is "": #EOF or nothing there
                break
            else:
                extractedDomain = line[line.find(':', line.find(':')+1)+1:line.find(':', line.find(':')+2)] #grabs domain name from line read. username::domain:[rest of hash]
                if extractedDomain != domainName: #not a valid user
                    continue
                else:
                    protocolFile.write(line) #writes that line to the protocol MasterList
                break

        protocolFile.close() #closes protocol Masterlist
