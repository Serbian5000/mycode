#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil   # shell utilities will need to move files
import os    # provides access to low level os operations


def main():
    """called at runtime"""

    os.chdir('/home/student/mycode/') # move into this working directory

    shutil.move('raynor.obj', 'ceph_storage/') # try moving the file raynor.obj into ceph_storage/ dir

    # program will pause to accept input from user
    xname = input('What is the new name for kerrigan.obj?') # collect string input from user

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into ceph_storage? with new name


# xname new file location be(queen_of_blades.zerg)?
