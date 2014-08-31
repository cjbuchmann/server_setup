#!/bin/bash

groupadd admin
adduser --gecos "" deployer --ingroup admin

sudo cp /etc/sudoers /etc/sudoers.old
sudo cp -f ./files/sudoers.template /etc/sudoers

# add github known host
ssh git@github.com
