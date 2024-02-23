#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

packages=(ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base julia octave clisp rustc freeglut3-dev mysql-server)
sudo apt-get -y --ignore-missing install "${packages[@]}"

python=(python3 python3-pip python3-numpy python3-scipy python3-pandas python3-matplotlib 
python3-pymysql python3-pymongo python3-mysql.connector)
sudo apt-get -y --ignore-missing install "${python[@]}"

sudo apt-get clean -y
sudo apt-get autoclean -y
sudo apt-get autoremove -y