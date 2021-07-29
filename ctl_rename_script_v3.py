'''
author@ Rohit Sharma
Date : 19-Mar-2021

Purpose: 
	- This script will generate .ctl files automatically from .grd files.

Command line arguments:
  - path where grid data files are stored
  - make sure your script and all .grd .ctl file in same path
  - date in "yyyymmdd" format

Generates following csv & json files:
  - generates/replace .ctl file with latest date

Assumptions:
  - files are stored inside the input_path folder.

How to Run: - for 10-mar-2021 bias_crctd files
  - python3 script_name.py 20210310 20210317 /home/rohit/Documents/bias_20210224/input_path/ 
  
Updated Script:
	- update line no 47 & 66 from "tmax_biascrct_" to "tmax_biascrct_test" only.

'''
import os
import sys
import fileinput
from datetime import datetime

old_date = str(sys.argv[1]) # old date on file 
current_date = str(sys.argv[2]) # current date on file
dt = datetime.strptime(current_date, "%Y%m%d")
date_format = dt.strftime("%d%b%Y") 
print(date_format)
path = str(sys.argv[3]) #path where the files are stored

#MAX_File
#rename filename of max file
os.rename(path + 'tmax_biascrct_' + old_date + '00.ctl', path +'tmax_biascrct_' + current_date + '00.ctl')	

#open file
file_max = path +"tmax_biascrct_" + current_date + "00.ctl"
max_file = open(file_max, 'r')
list_of_lines = max_file.readlines()
#rename lines
first_line = "dset " + path + "tmax_biascrct_test" + current_date + "00.grd\n"
twelve_line = "tdef 32 linear " + date_format + " 1dy\n"
list_of_lines[0] = first_line
list_of_lines[11] = twelve_line

#writing lines
max_file = open(file_max, 'w')
max_file.writelines(list_of_lines)
max_file.close()

#MIN_File
#rename filename of min file
os.rename(path + 'tmin_biascrct_' + old_date + '00.ctl', path +'tmin_biascrct_' + current_date + '00.ctl')	

#open file
file_min = path+ "tmin_biascrct_" + current_date + "00.ctl"
min_file = open(file_min, 'r')
list_of_lines = min_file.readlines()
#rename lines
first_line = "dset " + path + "tmin_biascrct_test" + current_date + "00.grd\n"
twelve_line = "tdef 32 linear " + date_format + " 1dy\n"
list_of_lines[0] = first_line
list_of_lines[11] = twelve_line

#writing lines
min_file = open(file_min, 'w')
min_file.writelines(list_of_lines)
min_file.close()
