#!/bin/bash

# gem dependencies
sudo apt-get install -y libxml2-dev libxslt1-dev

# ruby versioner
\curl -L https://get.rvm.io | bash -s stable
source ~/.profile
rvm install ruby

# gem installer
sudo apt-get install -y rubygems-integration

# gems
sudo gem install bundler
gem install rails
