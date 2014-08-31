#!/usr/bin/python

from sys import argv
import re
import argparse
from subprocess import call
import sys

print "Initializing server setup"

params = {
  'environment': 'development',
  'withGitConfig': False
}

gitParams = {
  'name': None,
  'email': None
}

parser = argparse.ArgumentParser(description='Setup a server environment')
parser.add_argument('-e', '--env',
  help='the environment to setup. IE, webserver, sqlserver or development.')
parser.add_argument('-wgc', '--with-git-config', action='store_true',
  help='setup name and email. Your git name and email must be passed.')
parser.add_argument('-gcname', '--git-config-name',
  help='git config name to use')
parser.add_argument('-gcemail', '--git-config-email',
  help='git config email to use')
parser.add_argument('-sshkeygen', '--with_ssh_keygen', action='store_true',
  help='flag to generate an ssh key. If an sshkeygen email is passed, it will use this email. Otherwise it will try to the the gcemail')
parser.add_argument('-sshkeyemail', '--ssh_keygen_email',
  help='if generating an ssh key, this email will be used')

args = vars( parser.parse_args() )

if args['with_git_config'] == True:
  print 'git config is set'
  if args['git_config_name'] == None:
    sys.exit("ERROR: You must declare your git config name if you want to setup the git config")
  if args['git_config_email'] == None:
    sys.exit("ERROR: you must declare your git config email if you want to setup the git config")

if args['with_ssh_keygen'] == True:
  if args['ssh_keygen_email'] == None:
    if args['git_config_email'] == None:
      sys.exit("ERROR: no keygen email specified. See help for details")
    else:
      args['ssh_keygen_email'] = args['git_config_email']


if args['with_ssh_keygen'] == True:
  call(['./scripts/setup_ssh_key.sh', args['ssh_keygen_email'] ])
call('./scripts/core_tools.sh')

if params['environment'] == "webserver":
  print "is development server"
elif params['environment'] == "sqlserver":
  print "is sql server"
elif params['environment'] == "development":
  print "Installing development server"

  call('./scripts/rails_installer.sh')
  call('./scripts/sql_client.sh')
  call('./scripts/sql_server.sh')
