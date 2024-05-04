import sys, os, subprocess, requests, platform


def install():
    if env.lower() == "ubuntu":
        os.system("sudo wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub")
        os.system("sudo gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub")
        os.system("echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list")
        packages = "gnome-terminal google-chrome-stable openjdk-21-jre openjdk-21-jdk python3-pip ruby-full build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima rustc freeglut3-dev mysql-server nasm nmap shc finger"
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get upgrade -y")
        cmd = "sudo apt-get -y --ignore-missing install "
        for pkg in packages.split():
            command = str(cmd) + str(pkg)
            subprocess.run(command.split())
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
        requests.get("https://kodingwindow.com")
        connection = True
    except:
        connection = False
    finally:
        return connection


def start_server():
    try:
        print("---------------------------------------------")
        print("The following versions are getting used")
        print("---------------------------------------------")
        print(subprocess.check_output("ruby -v", shell=True).rstrip().decode("utf-8"))
        print("Gem", subprocess.check_output("gem -v", shell=True).rstrip().decode("utf-8"))
        print(subprocess.check_output("bundle exec jekyll -v", shell=True).rstrip().decode("utf-8"))
        print(subprocess.check_output("bundler -v", shell=True).rstrip().decode("utf-8"))
        print("---------------------------------------------")
        if env.lower() == "ubuntu":
            if "CI" in os.environ:
                os.system("gnome-terminal -- bash -c 'sudo bundle exec jekyll serve; exec bash'")
            else:
                os.system("sudo bundle exec jekyll serve")
    except KeyboardInterrupt:
        pass
    except:
        print("Unable to start the Jekyll server")


def start_setup():
    full = False
    try:
        if sys.argv[1].lower() == "full":
            full = True
    except:
        full
    os.system("sudo kill -9 $(sudo lsof -t -i:4000) 2>/dev/null")
    if connected_to_internet():
        if sys.platform == "linux" and full:
            install()
            clean() 
            start_server()
        elif sys.platform == "win32" and full:
            install()
            start_server()
        else:
            start_server()
    elif full:
        print("A full setup requires an internet connection. You may continue without the full option if the necessary resources are installed.")
    else:
        start_server()


if sys.platform == "linux":
    env = platform.freedesktop_os_release().get("ID")
else:
    env = platform.system()

if env.lower() == "ubuntu" or env.lower() == "windows":
    start_setup()
else:
    print("Setup works on Windows and Ubuntu only")
    