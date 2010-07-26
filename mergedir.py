#!/usr/bin/env python

import os
import shutil

def merge(dir_from, dir_to, copy=True):
    assert os.path.exists(dir_from)
    assert os.path.exists(dir_to)

    if copy:
        copy_func = shutil.copy
        copytree_func = shutil.copytree
    else:
        copy_func = copytree_func = shutil.move

    #Look at each dir_from child
    for child in os.listdir(dir_from):
        child_path = os.path.join(dir_from, child)
        if os.path.exists(os.path.join(dir_to, child)):
            if os.path.isdir(child_path):
                print 'Merging', child_path
                merge(child_path, os.path.join(dir_to, child), copy)
            else:
                #do we want to overwrite?
                #ask the user!
                if raw_input('Do you want to overwrite %s ?' % child_path)\
                        == 'y':
                    copy_func(child_path, dir_to)


                
        else: #File/dir doesn't exist, we can just copy
            if os.path.isdir(child_path):
                print 'Copying entire dir:', child_path
                copytree_func(child_path, dir_to)
            else:
                print 'Copying file:', child_path
                copy_func(child_path, dir_to)




if __name__ == '__main__':
    import sys
    #TODO: handle options
    #Option -m: move, not copy
    #Option -c: copy [default]
    merge(sys.argv[1], sys.argv[2])


