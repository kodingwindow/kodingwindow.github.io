#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

packages=(git-all ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp rustc freeglut3-dev mysql-server nasm gnupg curl mongodb-org nmap shc)
sudo apt-get -y --ignore-missing install "${packages[@]}"

python=(python3 python3-pip python3-selenium python3-numpy python3-scipy python3-pandas python3-matplotlib 
python3-pymysql python3-pymongo python3-mysql.connector)
sudo apt-get -y --ignore-missing install "${python[@]}"
pip3 install webdriver-manager

sudo apt-get clean -y
sudo apt-get autoclean -y
sudo apt-get autoremove -y

sudo gem install jekyll bundler
update bundler
bundle install
bundle update
echo "———————————————————————————————————————————"
echo "Current versions on $(lsb_release -d --short)"
echo "———————————————————————————————————————————"
printf "$(ruby -v)\nGem $(gem -v)\n$(jekyll -v)\n$(bundler -v)\n"
echo "———————————————————————————————————————————"
sudo kill -9 $(sudo lsof -t -i:4000) 2> /dev/null
sudo bundle exec jekyll serve