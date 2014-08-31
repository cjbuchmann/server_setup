#!/usr/bin/python

from sys import argv
import re
import argparse
from subprocess import call

print "Initializing server setup"

params = {
  'environment': 'development',
  'withGitConfig': False
}

gitParams = {
  'name': None,
  'email': None
}

# def get_arguments( arguments ):
#   global environment
#
#   for argument in arguments:
#     print "argument is " + argument
#     if re.search('=', argument):
#       print "is not flag"
#       arg = argument.split("=")
#       print arg[1]
#
#
#   params['environment'] = "development"

# get_arguments( argv )

parser = argparse.ArgumentParser(description='Setup a server environment')
parser.add_argument('-e', '--env', help='the environment to setup. IE, webserver, sqlserver or development.')

args = vars( parser.parse_args() )

if args['env'] == "development":
  print "IT WORKS!"

call('./scripts/core_tools.sh')

if params['environment'] == "webserver":
  print "is web server"
elif params['environment'] == "sqlserver":
  print "is sql server"
elif params['environment'] == "development":
  print "is development server"
