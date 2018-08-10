# ResponderLog
A wrapper script for [[https://github.com/SpiderLabs/Responder|Responder's]] log files

Note: As of 08/10/2018, this script works for NTLMv1 and NTLMv2 hashes

After running Responder on a system, the results are written to the logs directory. 
Navigate to that logs directory and insert this script so it's in the same directory 
as the text files. Here's the command to run:

python -u ResponderLog.py {domain name}

The only parameter of the script is the domain name, which is used to find a valid
user hash in each file (since sometimes weird output is mixed in with actual users).
ResponderLog grabs one hash from each file and stores it in a MasterList file, one
for each unique NTLM protocol. This makes it easier to load hashes into Hashcat for
cracking, since all hashes with the same protocol are stored in one file. 
