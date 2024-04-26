#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

packages=(git-all ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima rustc freeglut3-dev mysql-server nasm nmap shc finger)
sudo apt-get -y --ignore-missing install "${packages[@]}"
pip install -r requirements.txt

sudo apt-get clean -y
sudo apt-get autoclean -y
sudo apt-get autoremove -y

sudo gem install jekyll bundler
bundle config set --local path vendor/bundle
bundle install
bundle update --bundler
bundle update
clear

echo "---------------------------------------------"
echo "Current versions on $(lsb_release -d --short)"
echo "---------------------------------------------"
printf "$(bundle exec ruby -v)
Gem $(bundle exec gem -v)
$(bundle exec jekyll -v)
$(bundle exec bundler -v)\n"
echo "---------------------------------------------"
sudo kill -9 $(sudo lsof -t -i:4000) 2> /dev/null
sudo bundle exec jekyll serve