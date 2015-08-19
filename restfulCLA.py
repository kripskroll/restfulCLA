import requests
import sys,os
#To manipulate XML files if necessary
import xml.etree.ElementTree as ET

#To encode Password for no cleartext password
import base64

# To import all commands available
from command import *

def cleanXML (resp):
    #Need to suppress all blank lines beginning of Response
    resp = os.linesep.join([s for s in resp.splitlines() if s])

    # Still need to suppress "non" XML tag (body and HTML) in order to properly manage it with ElementTree module.
    # See : https://wordpress.org/support/topic/xml-parsing-error-xml-or-text-declaration-not-at-start-of-entity-2
    # I'm a stupid dev : http://www.gossamer-threads.com/lists/python/python/1081659
    # So suppress them at beginning of output and end of output
    xmlResp = '\n'.join(resp.split('\n')[2:-2])
    return xmlResp

def readlAllMEG ():
    command = "<clacommand><act>siteconfig</act><get_site>getsites.txt</get_site></clacommand></clacommands>"
    return command

#api_url = 'http://10.10.10.3:8080/accessor/nG1CLA.jsp'
api_url = 'http://192.168.41.10:8080/accessor/nG1CLA.jsp'
login = 'froments'
passwd = 'netscout1'
startData = "<clacommands><ur>"+login+"</ur><pw>"+passwd+"</pw>"
endData = "</clacommands>"
cmdData = READ_ALL_MEG
data = startData+ cmdData + endData
headers = {'Content-Type': 'application/xml'}
print("Lecture Requete")
data = startData+ cmdData
r = requests.post(api_url, data=data, headers=headers)
resp = r.text
xmlResp = cleanXML(resp)
respRoot = ET.fromstring(xmlResp)

#for child in respRoot:
#    print (child.tag, child.attrib, child.text)
#    for child2 in child:
#        print (child2.tag, child2.attrib, child2.text)

# See ElementTree doc at https://docs.python.org/2/library/xml.etree.elementtree.html
# findall ONLY for direct children !!

for output in respRoot.findall('./claoutput/outputContent'):
    content = output.text
    print (content)

