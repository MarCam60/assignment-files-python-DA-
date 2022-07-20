__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from codecs import ignore_errors
from functools import cache
from pathlib import Path
from posixpath import abspath
import shutil
from tkinter import X
from zipfile import ZipFile

dir_path = "C:/Users/Gebruiker/Documents/WINC/files/cache"

def clean_cache():
    import os
    #import shutil
    directory = 'cache'
    #if dir_path:
    shutil.rmtree(dir_path, ignore_errors)
    os.makedirs(dir_path)
    return print (f"Directory {'%s'} cleaned"% directory) 

clean_cache()
         
  

def cache_zip (zip_file_path, cache_dir_path):
    
    zipfile = "C:/users/gebruiker/documents/winc/files/data.zip"
    zip_file_path
    cache_dir_path = "C:/users/gebruiker/documents/winc/files/cache"
    shutil.unpack_archive (zipfile,cache_dir_path)
    
    


def cached_files ():    
    
    import os
 
    file_paths= []
    path = os.path.abspath(dir_path)
 
    obj = os.scandir(path)

    
    for entry in obj :
      if entry.is_dir() or entry.is_file():
        file_paths.append (entry.path)
        print (entry.path)
    return file_paths

cached_files()
        



def find_password (file_paths):
   file_paths = cached_files()
   for file in file_paths:
    with open (file,"r") as f:
   #f = open('file_paths', "r")
        lines = f.readlines()
        for words in lines:
         if 'password' in words:
          return words.split()[1]


find_password(cached_files())


    #if 'password'in list1:
     #   print ('password')
