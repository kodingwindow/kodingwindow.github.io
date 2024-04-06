from utilities import *


def extract_compile(html_input, compiler, subpath, filename, extension, args):
    code = re.findall('<pre class="code">(.+?){% endhighlight %}</pre>', html_input, flags=re.DOTALL)
    if code is not None:
        output = "".join(code[0])
        f2 = open(subpath + filename + extension, "w")
        f2.write(output)
        f2 = open(subpath + filename + extension, "w")
        os.system("sed -i '1d;' {0}".format(subpath + filename + extension))
        f2.close

        if os.system(compiler + " " + subpath + filename + extension + args) == 0:
            print("Successful: " + subpath + filename + extension)
        else:
            print("Unsuccessful: " + subpath + filename + extension)

def compile_all(source, kwdata, destination):
    os.makedirs(destination, exist_ok=True)
    os.chdir(destination)
    for kwfile in os.listdir(kwdata):
        paths = read_file(None, kwdata, kwfile, "grandparent")
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
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight c %}'):
                extension = ".c"
                compiler = "gcc"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight cpp %}'):
                if path[1] == "opengl":
                    args = " -lGL -lGLU -lglut"
                elif path[0] == "cg":
                    args = " -lgraph"
                extension = ".cpp"
                compiler = "g++"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif (html_input.__contains__('<pre class="code">{% highlight java %}') and path[0] == "java" and path[1] != "jdbc"):
                extension = ".java"
                compiler = "javac"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight shell %}'):
                extension = ".sh"
                compiler = "shc -f"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight python %}'):
                extension = ".py"
                compiler = "python3 -m py_compile"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            elif html_input.__contains__('<pre class="code">{% highlight rust %}'):
                extension = ".rs"
                compiler = "rustc"
                extract_compile(html_input, compiler, subpath, path[2], extension, args)
            f1.close
    os.system("rm -rf " + destination)
