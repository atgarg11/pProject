#!/usr/bin/env python

from pyVmomi import vim
from pyVmomi import vmodl
#from tools import tasks
from pyVim.connect import SmartConnect, Disconnect
import atexit
import argparse
import getpass
import sys

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='this is the argument parser script')

    parser.add_argument('-o', '--host', help='vCentre IP address',
            #        required='false',
            default='localhost')
    parser.add_argument('-p', '--port', 
            #required='false',
            default='8080', 
            help='web server port')
    parser.add_argument('-u', '--user', 
            #required='false',
            default='administrator', 
            help='user name')
    parser.add_argument('-w', '--password', 
            #required='false',
            default='in$1eme', 
            help='password')
    parser.add_argument('-v', '--vmname', 
            #required='false',
            default='Atul-app-1', 
            help='Vm name ')
    parser.add_argument('-n1', '--one', 
            #required='false',
            default='0x39', 
            help='First Number ')
    parser.add_argument('-n2', '--two', 
            #required='false',
            default='0x3e', 
            help='iSecond number ')

    results = parser.parse_args(args)
    return (results)

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(
            content.rootfolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return  obj

def bitwise():
    args = check_arg(sys.argv[1:])
    one = int(args.one, 16)
    two = int(args.two, 16)
    print hex(one), 
    print hex(two)
    print (one ^ two) & two


def main():
    args = check_arg(sys.argv[1:])
    si = SmartConnect(host = args.host, 
           user = args.user,
           pwd = args.password, 
           port= args.port)
    atexit.register(Disconnect, si);

    vm = None
    if args.vmname:
        content = si.RetrieveContent()
        vm = get_obj(content, [vim.VirtualMachine], args.vmname)
        
    if vm: 
        print "vm found"
    else: 
        print "vm not found"

if __name__ == '__main__':
    bitwise() 
