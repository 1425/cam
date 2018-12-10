#!/usr/bin/env python

from argparse import ArgumentParser
from commands import getstatusoutput
from tempfile import NamedTemporaryFile

def do_or_print(s):
	#str->void

	status,output=getstatusoutput(s)
	if status:
		print 'Command failed:',s
		print output
		exit(1)


def stl(input_file,output_file):
	#str->str->void
	tmp=NamedTemporaryFile(suffix='.scad')
	print>>tmp,open(input_file,'r').read().replace('projection()','')
	tmp.flush()
	do_or_print('openscad '+tmp.name+' -o '+output_file)


def svg(input_file,output_file):
	#str->str->void
	tmp=NamedTemporaryFile(suffix=".dxf")

	do_or_print('openscad '+input_file+' -o '+tmp.name)

	#25.4 is to convert from inches to mm.
	do_or_print('/usr/share/inkscape/extensions/dxf_input.py --scale=25.4 '+tmp.name+' > '+output_file)


def main():
	p=ArgumentParser()
	p.add_argument('-i','--input_file',default='parametric_involute_gear_v5.0.scad')
	p.add_argument('-o','--output_file',default='output.svg')
	args=p.parse_args()

	if args.output_file.endswith('.stl'):
		run=stl
	elif args.output_file.endswith('.svg'):
		run=svg
	else:
		print>>stderr,'Error: Unrecognized format for output'
		return 1

	return run(args.input_file,args.output_file)


if __name__=='__main__':
	exit(main())
