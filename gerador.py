import sys
import glob
import os
import wget

urlCSS = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
fileCSS = wget.doenload(urlCSS)

params = sys.argv
projectName = params[2]
projectType = params[1]

os.mkdir(projectName)
path = projectName

os.mkdir(path+"/css")
os.mkdir(path+"/js")



fileCSS = open(path+"/css/style.css", "w")
fileCSS.close()

fileType = open(path+"/index."+projectType, "w")

fileType.write("<!DOCTYPE html>\n")
fileType.write("<html lang=\"pt-br\"<head>\n")
fileType.write("<meta charset=\"UTF-8\">\n")
fileType.write("<title>"+projectName+"</title>\n")
fileType.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n")
fileType.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
fileType.write("</head>\n")
fileType.write("<body>\n")
fileType.write("\n")
fileType.write("<script type=\"text/javascript\"></script>\n")
fileType.write("</body>\n")
fileType.write("</html>\n")

fileType.flush()

fileType.close()

print("Projeto "+params[2]+" criado!")

