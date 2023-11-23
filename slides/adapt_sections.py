#!/usr/bin/env python3

"""
This is a utility script:
    It counts ALL '\section' entries in all *tex
    files in this folder. It does not expect one
    '\section' per file (even though there should
    only be one). BUT it will enforce one '\section'
    per file for downstream processing!
    Finally it adapts the outline, in all *tex
    files to be split according the the section
    count.
"""

import argparse
from glob import glob
import math
import os
import re
import sys

section_re = re.compile('\\\section\{')
infile_re =  re.compile(r'(\\input)|(\\include)')
extract_re = re.compile(r'(?<=\{).+?(?=\})')

def check_suffix(fnames):
    checked = list()
    for fname in fnames:
        if not fname.endswith(".tex"):
           fname = fname + ".tex"
        checked.append(fname)
    return checked

def screen_master(masterdoc):
    fnames = list()
    with open(masterdoc) as infile:
        for line in infile:
            if infile_re.match(line):
                fnames.extend(extract_re.findall(line))
    return check_suffix(fnames)

def count_matching_lines(fp):
    count = 0
    for line in fp:
        if section_re.match(line):
            count += 1
    return count

def count_sections(file_list):
    count = 0
    for fname in file_list:
        with open(fname) as fp:
            count += count_matching_lines(fp)
    return count

def define_boundaries(section_count):
    fhe = math.floor(section_count/2)
    return {'lower': 1,
            'upper': section_count,
            'first_half_end': fhe,
            'second_half_start': fhe + 1}

def find_and_replace(boundaries, fname):
    # tex files aren't big, read all content in memory
    with open(fname) as infile:
        lines = infile.readlines()

    # get the matching 'currentsection' lines
    first_done, second_done = False, False
    for lcount, line in enumerate(lines):
        if not first_done:
            if 'currentsection' in line:
                first_done = lcount
                break
    for lcount, line in enumerate(lines[first_done + 1:]):
        if not second_done:
            if 'currentsection' in line:
                second_done = lcount + first_done + 1
                break

    if not (first_done and second_done):
        print("no outline found for %s -> skipping" % fname)
        return 

    # adapt the two lines with our new boundaries:
    lines[first_done] = "            \\tableofcontents[sections={%d-%d},currentsection]\n" % (boundaries['lower'], boundaries['first_half_end'])
    lines[second_done] = "            \\tableofcontents[sections={%d-%d},currentsection]\n" % (boundaries['second_half_start'], boundaries['upper'])
    
    with open(fname, 'w') as outfile:
        for line in lines:
            outfile.write(line)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--master-tex', required = True,
      help = "indicate a TeX master document")
    args = parser.parse_args()
    file_list = screen_master(args.master_tex)
    count      = count_sections(file_list)
    print('Found %d sections.' % count)
    boundaries = define_boundaries(count)
    for fname in file_list:
        find_and_replace(boundaries, fname)
