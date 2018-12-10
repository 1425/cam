#This is designed to install the software that will be used by the scripts
#It is assumed that this script is run as root
#Tested on Ubuntu 18.04

apt-get install inkscape

#The extra lines here are needed because OpenSCAD isn't in the 18.04 repo
add-apt-repository ppa:openscad/releases
apt-get update
apt-get install openscad
