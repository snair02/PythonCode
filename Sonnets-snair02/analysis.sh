#!/usr/bin/env bash 
## analysis.sh

# Download the sonnets
curl -o  sonnets/sonnets.txt "http://www.gutenberg.org/files/1041/1041.txt"

# Trim introduction and concluding lines
tail -n 2986 sonnets/sonnets.txt | head -2618 > sonnets/cleaned_sonnets.txt  

# Remove leading blank characters 
cut -c 3- sonnets/cleaned_sonnets.txt> sonnets/temp_sonnets.txt 
cp sonnets/temp_sonnets.txt sonnets/cleaned_sonnets.txt
rm sonnets/temp_sonnets.txt
# Split sonnets into individual files. This will involve *many* commands.
cd sonnets
#Sonnets 1 to 98
#--additional-prefix can be used to specify file extension
#E.g :--additional-prefix=.txt
head -1666 cleaned_sonnets.txt>sonnets1_98.txt
split -l 17 sonnets1_98.txt sonnet-1- 
rm sonnets1_98.txt

#Sonnet 99
head -1685 cleaned_sonnets.txt | tail -n 18 > sonnets-99.txt

#Sonnets 100-125
head -2127 cleaned_sonnets.txt | tail -n 442 >sonnets100_125.txt
split -l 17 sonnets100_125.txt sonnet-100-
rm sonnets100_125.txt
#Sonnet 126
tail -n 491 cleaned_sonnets.txt | head -14 >sonnet-126- 
#Sonnets 127-154
tail -n 476 cleaned_sonnets.txt>temp.txt
split -l 17 temp.txt sonnet-127-
rm temp.txt

# Find the longest sonnet (most words)
wc -w sonnet-*|sort -r > lengths.txt

# Search for specific words in  the sonnets
grep 'truth' sonnet-* > truth.txt
