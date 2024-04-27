#!/bin/bash

function install() {
    sudo apt-get update -y
    sudo apt-get upgrade -y
    packages=(default-jre default-jdk python3-pip ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima rustc freeglut3-dev mysql-server nasm nmap shc finger wget)
    sudo apt-get -y --ignore-missing install "${packages[@]}"
    pip install --user -r requirements.txt --break-system-packages | grep -v 'already satisfied'

    sudo gem install jekyll bundler
    bundle config set --local path vendor/bundle
    bundle install
    bundle update --bundler
    bundle update
}

function clean() {
    sudo apt-get clean -y
    sudo apt-get autoclean -y
    sudo apt-get autoremove -y
}

function start_server() {
    clear
    echo "---------------------------------------------"
    echo "Current versions on $(lsb_release -d --short)"
    echo "---------------------------------------------"
    printf "$(bundle exec ruby -v)
Gem $(bundle exec gem -v)
$(bundle exec jekyll -v)
$(bundle exec bundler -v)\n"
    echo "---------------------------------------------"
    sudo kill -9 $(sudo lsof -t -i:4000) 2>/dev/null
    sudo bundle exec jekyll serve
}

arg="$1"
echo -e "GET https://kodingwindow.com HTTP/1.0\n\n" | nc kodingwindow.com 80 >/dev/null 2>&1
if [ $? -eq 0 ]; then
    if [ "${arg,,}" == "full" ]; then
        install
        clean
    fi
    start_server
else
    if [ "${arg,,}" == "full" ]; then
        echo "No Internet Connection"
        exit 1
    elif ! start_server; then
        clear
        echo "No Internet Connection"
        echo "Unable to start the Jekyll server"
    fi
fi
