import sys
import glob
import os
import wget
import shutil


print("Baixando blibiotecas do Bootstrap\n")

urlJS = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
urlCSS = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"

fileCSS = wget.download(urlCSS)
FILEjs = wget.download(urlJS)

params = sys.argv
projectName = params[2]
projectType = params[1]

os.mkdir(projectName)
path = projectName

os.mkdir(path+"/css")
os.mkdir(path+"/js")

shutil.move("bootstrap.min.css", path+'/css')
shutil.move("bootstrap.min.js", path+'/js')

fileCSS = open(path+"/css/style.css", "w")
fileCSS.close()

fileJS = open(path+"/js/scripts.js", "w")
fileJS.close()

fileType = open(path+"/index."+projectType, "w")

fileType.write("<!DOCTYPE html>\n")
fileType.write("<html lang=\"pt-br\"\n>")
fileType.write("<head>\n")
fileType.write("<meta charset=\"UTF-8\">\n")
fileType.write("<title>"+projectName+"</title>\n")
fileType.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n")
fileType.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\">\n")
fileType.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.min.css\">\n")
fileType.write("</head>\n")
fileType.write("<body>\n")
fileType.write("<div class=\"container\">\n")
fileType.write("</div>\n")
fileType.write("<script type=\"text/javascript\"></script>\n")
fileType.write("</body>\n")
fileType.write("</html>\n")

fileType.flush()
fileType.close()
print("\n")
print("Projeto '"+params[2]+"' criado!")
print("Arquivos criados>\n\tindex."+params[1]+"\n\tcss/style.css\n\tjs/scripts.js")
print("\n")
print("Arquivos baixados>")
print("\tcss/bootstrap.min.css\n\tjs/bootstrap.min.js")