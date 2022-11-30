from os import listdir, walk
from os.path import isfile, join
import argparse

def get_file_names(folderpath, out='output.txt'):
    """takes a path to a folder and writes all filenames in the folder to a specified output file"""
    onlyfiles = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    with open(out, 'w') as file_object:
        for f in onlyfiles:
            file_object.write(f+'\n')

def get_all_file_names(folderpath, out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders too)"""
    filenames = [f for (dirpath, dirnames, filenames) in walk(folderpath) for f in filenames]
    with open(out, 'w') as file_object:
        for f in filenames:
            file_object.write(f+'\n')

def print_line_one(file_names):
    """takes a list of file names and print the first line of each"""
    for f in file_names:
        with open(f, 'r') as file_object:
            print(file_object.readline())

def print_emails(file_names):
    """takes a list of file names and print each line that contains an email (just look fot the @)"""
    for f in file_names:
        if f.endswith('.csv') or f.endswith('.txt') or f.endswith('.xml):
            with open(f, 'r') as file_object:
                for line in file_object:
                    if('@' in line):
                        print(line)

def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    headlines = []
    for f in md_files:
        with open(f, 'r') as file_object:
            for line in file_object:
                if(line[0]=='#'):
                    headlines.append(line)
    with open(out, 'w') as file_object:
        for l in headlines:
            file_object.write(l+'\n')
            
parser = argparse.ArgumentParser(description="does stuff with files")