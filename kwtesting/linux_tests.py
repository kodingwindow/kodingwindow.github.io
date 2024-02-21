from utilities import *

start = time.time()
os.makedirs(kwtesting, exist_ok=True)
os.chdir(kwtesting)
for filename in os.listdir(datapath):
    paths = read_file(None, filename, "grandparent")
    for i in range(0, len(paths)):
        path = str(paths[i]).split("/")
        args = ""
        if path[0] == "c":
            compiler = "gcc"
            extension = ".c"
        elif path[0] == "cpp":
            compiler = "g++"
            extension = ".cpp"
        elif path[0] == "java":
            compiler = "javac"
            extension = ".java"
        elif path[0] == "cg":
            compiler = "g++"
            extension = ".cpp"
            args = " -lgraph"
            if path[1] == "opengl":
                args = " -lGL -lGLU -lglut"
        elif path[0] == "rust":
            compiler = "rustc"
            extension = ".rs"
        elif path[0] == "asm":
            compiler = "nasm -felf64"
            extension = ".asm"
        else:
            compiler = None
            extension = ""
        if compiler is not None:
            f1 = open(kw + paths[i] + ".html", "r")
            f2 = open(kwtesting + path[2] + extension, "w")
            html_input = f1.read()
            try:
                matches = re.findall('<pre class="code">(.+?){% endhighlight %}</pre>', html_input, flags=re.DOTALL)
                output = "".join(matches[0])
                f2.write(output)
                f2 = open(kwtesting + path[2] + extension, "w")
                os.system("sed -i '1d;' {0}".format(kwtesting + path[2] + extension))
            except IndexError:
                pass
            f1.close
            f2.close
            
            if os.system(compiler + " " + path[2] + extension + args) == 0:
                print("Successful: " + path[1] +"/"+ path[2] + extension)
            else:
                print("Unsuccessful: " + path[1] +"/"+ path[2] + extension)

end = time.time()
m, s = divmod(round(end - start), 60)
h, m = divmod(m, 60)
print("Total Execution Time: "+f'{h:02d}:{m:02d}:{s:02d}')