- scan_readavi.py : change the `file` variable tot he path of the .avi you want to read. It will read it and set the [x, z] data into an array of size (Nframe, 2, Npoints)

- slk_tocsv.py : converts the .slk files given as export by the micro-epsilon software into a csv file. Can be used to check the output of the previous script.
NOTE: the export via the software has been seen to miss some time stamps, so be carefull when you cant to make a frame to frame comparison.

CREDITS: 

- sylk_parser.py and 'sylk.py' have been taken from https://github.com/majerteam/sylk_parser
- code from `laser.py` has been largely inspired from a script written by Chris Johnson (University of Manchester)