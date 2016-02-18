import os, sys, zipfile
from xml.dom.minidom import parse
import xml.dom.minidom


def main():
	print('Provide file name with directory location eg:- "C://dirname//file.zip" with double quotes ')
    	name=input('Name:-') 
    	if zipfile.is_zipfile(name):
    		destination=input('Extract location & folder name in format "C://dirname//extractfoldername":-\n')
    		if os.path.isdir(destination):
    			print("destination already exists")
    		else:
    			des=unzipfile(name,destination)
    			print("d:-"+des)
    			listfiles(des)
    			parsemeXML(des)
    	else:
    		print("Invalid zip file")
    		



def unzipfile(name,destination):
	if zipfile.is_zipfile(name):
		zfile=zipfile.ZipFile(name,'r')
		zfile.extractall(destination)
		print("extraction completed to location:-"+destination)
		return destination
	else:
		print("Invalid zip")



def listfiles(des):
	for dirName, subdir, fileList in os.walk(des):
		print('Directory: %s' % dirName)
		for filename in fileList:
			print('\t%s' % filename)
		if len(subdir) > 0:
			del subdir[0]

        

def parsemeXML(des):
	domtree = xml.dom.minidom.parse(des+"//"+"parseme.xml")
	print("**********************************************************\n")
	print("parseme.xml Id, name, version, publicKeyToken\n")
	supportedOS = domtree.getElementsByTagName('supportedOS')
	for id in supportedOS:
		if id.hasAttribute("Id"):
			print "Id:-"+id.getAttribute("Id")
	assemblyIdentity = domtree.getElementsByTagName('assemblyIdentity')
	for assId in assemblyIdentity:
		if assId.hasAttribute("name"):
			print "name:-"+assId.getAttribute("name")
		if assId.hasAttribute("version"):
			print "version:-"+assId.getAttribute("version")
		if assId.hasAttribute("publicKeyToken"):
			print "publicKeyToken:-"+assId.getAttribute("publicKeyToken")




if __name__ == "__main__":
	main()
	
    	
    	
    	