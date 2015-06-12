 #!/usr/bin/env python
import argparse
import os
import sys
import yaml
import subprocess as subp
import shlex

yaml_file = 'tibco.yml'
config = open(yaml_file)

data = yaml.load(config)

def yaml_loop(yaml_file):
    return 0

def proto_get_pkg(pkg):
    for i in range(len(v[pkg])):
        args= "wget -P pkg -nc dest"
        pr = subp.call(args)
#        print "{}/{}".format(v['main']['server'], v['set_rv'][i]['package'])

def proto_install_pkg(pkg):
    for i in range(len(v['set_rv'])):
        print "{}/{}".format(v['main']['server'], v['set_rv'][i]['package'])

def install_pkg(package):
    download_pkg(package)
    print "Installing package {}".format(package)

def download_pkg(pkg):
    print "Downloading package {}".format(pkg)

def main():
    parser = argparse.ArgumentParser(description='Install Tibco package')
    parser.add_argument('-i','--install', nargs=1, type=install_pkg, help='Dwonload and install the package.')
    parser.add_argument('-d','--download', nargs=1, type=download_pkg, help='Download the package.')
    args = parser.parse_args()

    
if __name__ == '__main__':
    main()
