# -*- coding: utf-8 -*-
import re
import os
import pprint
import re_test as ret

def visit_path(arg, dirpath, namelist):
    if ".git" not in dirpath:
        org_path = os.path.abspath(os.curdir)
        d_path = os.path.abspath(dirpath)
        os.chdir(d_path)
        
        for name in namelist:
            if os.path.isfile(name):
                ret.git("log %s" % name)
        
        os.chdir(org_path)
            

if "__main__" == __name__:
    # read file
    found = ret.get_proj_id_list(ret.txt_fname)
    
    # sample git log example
    '''git log --format="%h, %ai" [path]/[file]'''
    
    '''
    project id loop : for all project id's
        go in
        get list
        if doesn't start with '.'
            if file, get log
                # commits
                # begin ~ end
                # average commit interval
    '''
    
    proj_id = found[4]

    # change directory to project repository    
    original_path = ret.cd_proj_repo(proj_id)
    
    # initialize student directory
    student_dict = {}

    os.path.walk(os.curdir, visit_path, student_dict)

    os.chdir(original_path)
    
