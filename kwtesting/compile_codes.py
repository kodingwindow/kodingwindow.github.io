from utilities import *

passed = failed = 0


def is_compiled(html_input, compiler, subpath, file_name, extension, args):
    code = re.findall('<pre class="code">(.+?){% endhighlight %}</pre>', html_input, flags=re.DOTALL)
    if code is not None:
        output = "".join(code[0])
        f2 = open(subpath + file_name + extension, "w")
        f2.write(output)
        f2 = open(subpath + file_name + extension, "w")
        os.system("sed -i '1d;' {0}".format(subpath + file_name + extension))
        f2.close

        global passed, failed 
        try:
            subprocess.check_output(
                compiler + " " + subpath + file_name + extension + args,
                shell=True,
                stderr=subprocess.DEVNULL,
            )
            # Code compilation is successful as it is bug-free
            print("Successful: " + website + subpath + file_name + extension)
            passed += 1
        except:
            # Code compilation is unsuccessful due to required resources are unfound (e.g. graphics.h)
            print("Unsuccessful: " + website + subpath + file_name + extension)
            failed += 1


def compile_codes(source, destination, data_path):
    os.makedirs(destination, exist_ok=True)
    os.chdir(destination)
    for file_name in os.listdir(data_path):
        paths = read_file(None, data_path, file_name, "grandparent")
        for i in range(0, len(paths)):
            path = str(paths[i]).split("/")
            subpath = path[0] + "/" + path[1] + "/"
            os.makedirs(subpath, exist_ok=True)
            args = ""
            f1 = open(source + paths[i] + ".html", "r")
            html_input = f1.read()
            if html_input.__contains__('<pre class="code">{% highlight nasm %}'):
                extension = ".asm"
                compiler = "nasm -felf64"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight c %}'):
                extension = ".c"
                compiler = "gcc"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight cpp %}'):
                if path[1] == "opengl":
                    args = " -lGL -lGLU -lglut"
                elif path[0] == "cg":
                    args = " -lgraph"
                extension = ".cpp"
                compiler = "g++"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif (
                html_input.__contains__('<pre class="code">{% highlight java %}')
                and path[0] == "java"
                and path[1] != "jdbc"
            ):
                extension = ".java"
                compiler = "javac"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight shell %}'):
                extension = ".sh"
                compiler = "shc -f"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight python %}'):
                extension = ".py"
                compiler = "python3 -m py_compile"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight rust %}'):
                extension = ".rs"
                compiler = "rustc"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            f1.close
    print("---------------------------------")
    print("Compilers Version Used")
    print("---------------------------------")
    print("gcc/g++", subprocess.check_output("g++ -dumpfullversion", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("javac --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("python3 --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("rustc --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("nasm --version", shell=True).rstrip().decode("utf-8"))
    os.system("rm -rf " + destination)
    return passed, failed
