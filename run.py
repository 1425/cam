#!/usr/bin/env python

from argparse import ArgumentParser
from commands import getstatusoutput
from tempfile import NamedTemporaryFile

def do_or_print(s):
	status,output=getstatusoutput(s)
	if status:
		print 'Command failed:',s
		print output
		exit(1)


def main():
	p=ArgumentParser()
	p.add_argument('-o','--output_file',default='output.svg')
	args=p.parse_args()
	tmp=NamedTemporaryFile(suffix=".dxf")

	do_or_print('openscad parametric_involute_gear_v5.0.scad -o '+tmp.name)

	#25.4 is to convert from inches to mm.
	do_or_print('/usr/share/inkscape/extensions/dxf_input.py --scale=25.4 '+tmp.name+' > '+args.output_file)


if __name__=='__main__':
	exit(main())
