import os
import socket
from collections import Counter

def ReadFile(path):
    with open(path, 'r') as file:
        return file.read()
    
os.chdir('/home')

# List File Names
textFiles = os.listdir('data')

# Read Files
ifFile = ReadFile('data/IF.txt')
LimerickFile = ReadFile('data/Limerick-1.txt')

# Words
ifFileWords = ifFile.split()
LimerickFile = LimerickFile.split()

# Counts
ifFileWordCount = len(ifFileWords)
LimerickFileCount = len(LimerickFile)

# Top 3 in IF.txt
ifWordCounts = Counter(ifFileWords)
ifTopThree = ifWordCounts.most_common(3)

# Find Ip Address
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

with open('/home/output/result.txt', 'w') as output:
    output.write(f'Files in /data \n')
    for file in textFiles:
        output.write(f'{file}\n')
    
    output.write(f'\nIF.txt word count: {ifFileWordCount} \n')
    output.write(f'Limerick-1.txt word count: {LimerickFileCount} \n')
    output.write(f'Total: {ifFileWordCount + LimerickFileCount}\n\n')

    output.write('Top 3 words in IF.txt:\n')
    for word, count in ifTopThree:
        output.write(f'{word}\n')
    
    output.write(f'\nHost IP address: {hostIP}')

