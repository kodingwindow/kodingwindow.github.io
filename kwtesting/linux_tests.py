from utilities import *


def kw_compile(compiler, filename, extension, args):
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


os.makedirs(kwfied, exist_ok=True)
os.chdir(kwfied)
for filename in os.listdir(datapath):
    paths = read_file(None, filename, "grandparent")
    for i in range(0, len(paths)):
        path = str(paths[i]).split("/")
        subpath = path[0] + "/" + path[1] + "/"
        os.makedirs(subpath, exist_ok=True)
        args = ""
        f1 = open(kw + paths[i] + ".html", "r")
        html_input = f1.read()
        if html_input.__contains__('<pre class="code">{% highlight nasm %}'):
            extension = ".asm"
            compiler = "nasm -felf64"
            kw_compile(compiler, path[2], extension, args)
        elif html_input.__contains__('<pre class="code">{% highlight c %}'):
            extension = ".c"
            compiler = "gcc"
            kw_compile(compiler, path[2], extension, args)
        elif html_input.__contains__('<pre class="code">{% highlight cpp %}'):
            if path[1] == "opengl":
                args = " -lGL -lGLU -lglut"
            elif path[0] == "cg":
                args = " -lgraph"
            extension = ".cpp"
            compiler = "g++"
            kw_compile(compiler, path[2], extension, args)
        elif (html_input.__contains__('<pre class="code">{% highlight java %}') and path[0] == "java"):
            extension = ".java"
            compiler = "javac"
            kw_compile(compiler, path[2], extension, args)
        elif html_input.__contains__('<pre class="code">{% highlight python %}'):
            extension = ".py"
            compiler = "python3 -m py_compile"
            kw_compile(compiler, path[2], extension, args)
        elif html_input.__contains__('<pre class="code">{% highlight rust %}'):
            extension = ".rs"
            compiler = "rustc"
            kw_compile(compiler, path[2], extension, args)
        f1.close

os.system("rm -rf " + kwfied)
