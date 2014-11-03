#!/bin/bash

# gem dependencies
sudo apt-get install -y libxml2-dev libxslt1-dev

# ruby versioner
echo "~~ installing RVM ~~"
gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
# TODO - rvm sourcing does not seem to work here
\curl -sSL https://get.rvm.io | bash -s stable --ruby
source ~/.rvm/scripts/rvm
# rvm use --default
# rvm install ruby

# gem installer
sudo apt-get install -y rubygems-integration

# gems
echo "~~ installing bundler gem ~~"
sudo gem install bundler
echo "~~ installing rails gem ~~"
gem install rails --no-rdoc --no-ri
