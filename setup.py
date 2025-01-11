"""
Author: Shubham Darda
Description: The Kodingwindow website can be set up and operated on localhost with the aid of this script.
"""

import sys, os, subprocess, platform, socket, shutil

cwd = os.getcwd() + "/"
kw = "kodingwindow.github.io"
ubuntu = False
githubactions = False
total, used, free = shutil.disk_usage(cwd)
freedisk = free // (2**30)

def install_chrome():
    chrome_version = os.system("google-chrome --version > /dev/null")
    if chrome_version != 0:
        os.system("sudo wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub")
        os.system("sudo gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub")
        os.system("echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list")
        os.system("sudo apt-get -y install google-chrome-stable")


def install():
    if ubuntu:
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get full-upgrade -y")
        install_chrome()

        if githubactions:
            packages = "ruby-full clisp rustc freeglut3-dev nasm shc"
        else:
            packages = "git-all openjdk-21-jre openjdk-21-jdk ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima rustc freeglut3-dev mysql-server nasm nmap shc finger"

            snap = os.system("snap --version > /dev/null")
            vscode = os.system("code --version > /dev/null")
            julia = os.system("julia --version > /dev/null")
            if snap == 0 and vscode != 0:
                os.system("sudo snap install --classic code")
            if snap == 0 and julia != 0:
                os.system("sudo snap install julia --classic")

        cmd = "sudo apt-get -y --ignore-missing install "
        for pkg in packages.split():
            command = str(cmd) + str(pkg)
            subprocess.run(command.split())
    
        if not githubactions:
            if kw not in os.getcwd():
                os.system("git clone https://github.com/kodingwindow/kodingwindow.github.io.git")
                os.chdir(cwd + kw + "/")

    os.system("sudo gem install jekyll bundler")
    os.system("pip install --user -r requirements.txt --break-system-packages --no-warn-script-location")
    os.system("bundle config set --local path vendor/bundle")
    os.system("bundle install")
    os.system("bundle update --bundler")
    os.system("bundle update")


def clean():
    os.system("sudo apt-get clean -y")
    os.system("sudo apt-get autoclean -y")
    os.system("sudo apt-get autoremove -y")


def connected_to_internet():
    connection = None
    try:
        socket.create_connection(("8.8.8.8", 53))
        connection = True
    except:
        connection = False
    finally:
        return connection


def start_server():
    try:
        if kw not in os.getcwd():
            os.chdir(cwd + kw + "/")
        print("---------------------------------------------")
        print("The following versions are getting used")
        print("---------------------------------------------")
        print(subprocess.check_output("ruby -v", shell=True).rstrip().decode("utf-8"))
        print("Gem", subprocess.check_output("gem -v", shell=True).rstrip().decode("utf-8"))
        print(subprocess.check_output("bundle exec jekyll -v", shell=True).rstrip().decode("utf-8"))
        print(subprocess.check_output("bundler -v", shell=True).rstrip().decode("utf-8"))
        print("---------------------------------------------")
        if ubuntu:
            if githubactions:
                os.system("sudo bundle exec jekyll build")
            else:
                os.system("sudo bundle exec jekyll serve")
        else:
            os.system("bundle exec jekyll serve")
    except KeyboardInterrupt:
        pass
    except:
        print("Unable to start the Jekyll server: required resources are not found\nRecommended: python3 setup.py full")


def start_setup():
    full = False
    try:
        if sys.argv[1].lower() == "full":
            full = True
    except:
        full
    if connected_to_internet():
        if freedisk >= 2:
            if full: 
                if ubuntu:
                    install()
                    clean() 
                elif not ubuntu:
                    install()
        else:
            print("Insufficient disk space. Required 2 GB or more for full setup.")
        start_server()
    elif full:
        print("A full setup requires an internet connection. You may continue without the full option if the necessary resources are installed.")
    else:
        start_server()


if sys.version_info.major == 3 and sys.version_info.minor >= 4:
    if sys.platform == "linux":
        env = platform.freedesktop_os_release().get("ID").lower()
        os.system("sudo kill -9 $(sudo lsof -t -i:4000) 2>/dev/null")
        if env == "ubuntu":
            ubuntu = True
            if os.getenv("GITHUB_ACTIONS") == "true":
                githubactions = True
            start_setup()
        else:
            print("Setup only works on Ubuntu Linux distribution.")
    elif sys.platform == "win32":
        env = platform.system().lower()
        start_setup()
    else:
        print("Setup only works on Windows and Ubuntu OS.")
else:
    print("Python 3.4 or later is needed for setup.")
