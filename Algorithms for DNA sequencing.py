Algorithms for DNA sequencing
## Finding the Longest common Prefix in sequence

A= def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

print (A)

## Finding matching string (exactly matching for longer length)

B = def match(s1,s2):
        if not len(s1) == len(s2):
            return False
        
        for i in range (len(s1)):
            if not s1[1] == s2[i]
                return False
        
        return True


## Doing reverse complement

complement = {'A':'T','G':'C', 'C':'G', 'T':'A'}

def reversecomplement(s):
     complement = {'A':'T','G':'C', 'C':'G', 'T':'A'}
     t = ''
     for base in s:
          t = complement[base] + t
    return t 

##Downloading and parsing a genome
def readGenome(filename):
     genome = '' 
     with open(filename, 'r') as f:
          for line in f:
               if not line [0] == '>':
                    genome += line.rstrip()
    return genome
genome = readGenome('FASTAQfile name')    
len (genome) 

### Count the BP in the sequence

counts = {'A':0, 'C':0, 'G':0, 'T':0}
for base in genome:
     counts[base] += 1
print(counts)

or 

import collections
collections.Counter(genome)

## Working with sequencing reads
## Read fastq

def readFastq(filename):
     sequences = []
     qualities = []
     with open (filename) as fh:
          while TRUE:
               fh.readline()
               seq = fh.readline()
               fh.readline ()
               qual = fh.readline() .rstrip()
               if len(seq) == 0:
                    break
               sequences.append(seq)
               qualities.append(qual)
    return sequences, qualities
seqs, quals = readFastq('filename')

## Check quality 

def phred33ToQ(qual):
     return ord(qual) -33
phred33ToQ('#')

## create list of qualities check after substracting with phred 33

def createHist(qualities):
     hist = [0] * 50
     for qual in qualities:
          for phred in qual:
               q = phred33ToQ(phred)
               hist[q] += 1
    return hist
h = createHist(quals)
print(h)

## Visualise the qualities with map

import matplotlib.pyplot as plt
plt.bar (range(len(h), h))
plt.show()

## Analyze reads by position
##find GC by position

def findGCByPos(reads):
     gc = [0] *100
     totals = [0]*100

    for read in reads:
        for i in range(len(read)):
             if read[i] == 'C' or read[i] =='G':
                  gc[i] +=1
              totals[i] += 1
        
        for i in range(len(gc))
            gc[i] /= float(totals[i])
        
        return gc

gc = findGCByPos(seqs)
plt.plot(range(len(gc)), gc)
plt.show()

## Distribution of Bases

import collections
count = collections.Counter()
for seq in seqs:
     count.update(seq)
print(count)

### Making artificial reads

# Check which positions that are matched 
def readGenome(filename):
     genome = '' 
     with open(filename, 'r') as f:
          for line in f:
               if not line [0] == '>':
                    genome += line.rstrip()
    return genome
genome = readGenome('FASTAQfile name')    
len (genome) 

def naive(p,t):
     occurrence = []
     for i in range(len(t) - len(p) + 1):
          match = True
          for j in range (len(p)):
               if not t[i+j] == p[j]:
                    match = False
            if match:
               occurrences.append(i)
    return occurrence 

# making artificial and matching artificial reads
import random 
def generateReads(genome, numReads, readLen):
     '''Generate reads from random position in the given genome. '''

    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)-readLen) - 1
        reads.append(genome[start : start+readLen])
    return reads

numMatched = 0
for r in reads:
     matches = naive(r, genome)
     if len(matches)>0:
          numMatched += 1
print('reads matched exactly !'% (numMatched, len(reads)))

## Matching real reads
# Aligning 

numMatched = 0 
n = 0 
for r in phix_reads:
     matches = naive(r,genome)
     n += 1
     if len(matches) > 0:
          numMatched += 1
print ('reads matched exactly !'% (numMatched, len(reads)))

