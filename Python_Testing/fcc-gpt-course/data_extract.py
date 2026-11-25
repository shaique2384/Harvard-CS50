# Interact with the operating system
import os
# Handle compressed files
import lzma
# Handle data in JSON format
import json
# Handle data in CSV format
import csv
# Handle data in Excel format
import pandas as pd
# To display progress bars for loops in the terminal
from sympy import false
from tqdm import tqdm

def xz_files_in_dir(directory):
    files=[]
    for filename in os.listdir(directory): # It's just ls command in terminal
        if filename.endswith('.xz') and os.path.isfile(os.path.join(directory,filename)): # os.path.isfile() checks if the path is a file or not
            # os.path.join() joins the directory and filename to create a full path
            files.append(filename)
    return files

# Let's set up some variables
folder_path="/mnt/music/PHD_Prep/github/cogWALLs2384/Python_Testing/fcc-gpt-course/openwebtext.tar/openwebtext"
if False:
    output_file="output{}.txt" # This is a template for the output file name, where {} will be replaced by the index of the file being processed
    # Keep in mind In this giant corpus we can't push it on ram all at once 
    # As we are reading these 20,000 compressedfiles we will be taking all the new characters from them and just push them into a vocab file
    # This will contain all of the different characters so that we can sort them into list as chars
    vocab_file="vocab.txt"
    # How many files we are going to split them into
    split_files=int(input("How many files would you like to split this into? ")) 
    # This file will split into n numbers of files for (output{i}.txt)==n

    files=xz_files_in_dir(folder_path)
    total_files=len(files)


    # Now in here we'll calculate the number of files to process for each output file
    max_count=total_files//split_files if split_files!=0 else total_files
    '''max_count is the number of elements from the files list so that they make split_files number of packets'''
    # If the user has requested more than one output file; this is the total number of files divided by the number of output files requested rounded down to the nearest whole number 

    vocab=set() # This will hold all the unique characters we encounter in the text files


    for i in range(split_files):
        # When count 
        with open(output_file.format(i),'w',encoding="utf-8") as outfile:
            for count,filename in enumerate(tqdm(files[:max_count],total=max_count)):
                if count >= max_count:
                    break
                    # It breaks this loop and start from 1th number 2nd iteration of range(split_files) and after split_files times iteration of this break loop after max_count the outermost loop completes.
                file_path=os.path.join(folder_path,filename)
                with lzma.open(file_path,'rt',encoding='utf-8') as infile:
                    text=infile.read()
                    outfile.write(text)
                    characters=set(text)
                    # organized as unique characters.
                    vocab.update(characters) 
                    # this is the so called append method for sets and in the (split_file)^th times (max_cout)^th iteration it will have all the unique characters from all the files in the folder_path directory
            files=files[max_count:] # This will remove the first max_count files from the list so that we can process the next batch in the next iteration of the outer loop and eventually we will have concatenated all the files into split_files number of output files and also have a vocab set with all the unique characters from all the files in the folder_path directory

    # Finally we will write all our vocabularies as vfile each at newlines 
    with open(vocab_file,'w',encoding='utf-8') as vfile:
        for char in vocab:
            vfile.write(char+'\n') # This will write each unique character on a new line in the vocab.txt file

# It will be really inefficient to just get blocks and then creating train and val splits as we go on every batch
# So we will create separate output_file_train(90% of our data) and output_file_val(10% of our data).
# rewrite the output_file
output_file_train='train_split.txt'
output_file_val='val_split.txt'
vocab_file='vocab.txt'

# apply the custorm func to get the list of files in the folder_path directory
files=xz_files_in_dir(folder_path) # will be used to open(,'w') to mkdir writable *.txt files and lzma.open(,rt) to read *.xz files and wite into the same *.txt files and also to cat into the complete set of unique characters. 
total_files=len(files) 

# Get the total number of files in the folder_path directory
# Calculate the split indices
split_index=int(total_files*0.9) # 90% of the total files for training
files_train=files[:split_index] # First 90% of the files for training
files_val=files[split_index:] # Remaining 10% of the files for validation

# create an updatable empty set
vocab=set()

# Process the training files
with open(output_file_train,'w',encoding='utf-8') as outfile_train:
    # mkdir the output_train.txt
    for filename in tqdm(files_train,total=len(files_train)): # total keyword makes sure we dont get into the val files as we are iterating over the files_train list
        file_path=os.path.join(folder_path,filename)
        # seamlessly creates *.xz files in directory str representation list and assigns to file_path variable
        with lzma.open(file_path,'rt',encoding='utf-8') as infile:
            # Read the content of the *.xz file and write it to the output file
            text=infile.read()
            # read the text from the *.xz file and assign it to text variable
            outfile_train.write(text)
            # appends string to the output_train.txt file
            characters=set(text)
            # organized as unique characters in output_train.txt file
            vocab.update(characters)

# Process the validation files
with open(output_file_val,'w',encoding='utf-8') as outfile_val:
    # mkdir the output_val.txt
    for filename in tqdm(files_val,total=len(files_val)):
        file_path=os.path.join(folder_path,filename)
        with lzma.open(file_path,'rt',encoding='utf-8') as infile:
            text=infile.read()
            outfile_val.write(text)
            characters=set(text)
            vocab.update(characters)
            # This will update the vocab set with unique characters from the validation files as well, so that we have a complete set of unique characters from both training and validation data.

# Write the vocabulary to vocab.txt
with open(vocab_file,'w',encoding='utf-8') as vfile:
    for char in vocab:
        vfile.write(char+'\n')
        # Vertical bar is used to separate the characters in the vocab.txt file, so that each character is on a new line.