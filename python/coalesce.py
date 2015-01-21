#!/usr/bin/python
# TODO:
#       Encapsulate functions into classes
#       Make RFC specific allowances into proper polymorphism rather than hard coded regular expressions
#       Implement more intelligent directory creation
#       Fault tolerance.  Any would be nice, especially when working with the file system
#       Etc.


from os import listdir
import sys, os, json, csv, re

def json2csv(input, fileName):
        data = json.loads(input)
        output = csv.writer(open(fileName+'.csv', 'w'))

        output.writerow(data[0].keys())

        for row in data:
                output.writerow(row.values())



def aaronBrackets ( aString ):
        counter = 0
        fileCount = 0
        subString = ""
        fileName = 'output_'+str(fileCount)
        for char in aString:
                if char == '{':
                        subString += char
                        counter += 1
                elif char == '}':
                        if counter == 1:
                                subString += char + ']'
                                subString = re.sub('^,', '[', str(subString))
                                subString = re.sub(r'"workflow":{("workflowID":[0-9]*),"(name":".*?")},', r'\1,"RFC\2,', str(subString))
                                #subString = re.sub(r'{"name":(".*?"),"value":"(.*?)"},', r'{\1:"\2"},', str(subString))
                                #print subString + "\n\n"
                                json2csv(subString, fileName)
                                subString = ""
                                fileCount += 1
                                fileName = 'output_' + str(fileCount)
                                counter -= 1
                        else:
                                subString += char
                                counter -= 1

                else:
                        subString += char

'''

Classes.  Because this how I do.


'''

class oldFile:

        '''
        Takes an old file and parses the file name, CSV header, and content into attributes.
        '''

        def __init__(self, fileName):
                self.content = ''
                with open(fileName, 'r') as file:
                        self.title = file.name
                        self.header = file.readline()
                        for line in file:
                                self.content += line
                        file.close()

        def getHeader(self):
                return self.header

        def getTitle(self):
                return self.title

        def getContent(self):
                return self.content

        def showContent(self):
                print "title: " + self.getTitle()
                print "Header: " + self.getHeader()
                print "content: " + self.getContent()

class outFile:

        '''
        Object class for new files; getter functions are only useful for debugging and testing, but
        addContent() and writeContent() are your workhorses here, populating the body attribute and then
        the outfile.
        '''
        def __init__(self, fileName, initHeader):
                self.title = fileName
                self.header = initHeader
                self.body = ''

        def getHeader(self):
                return self.header

        def getTitle(self):
                return self.title

        def getBody(self):
                return self.body

        def addContent(self, oldFile):
                if (oldFile.getHeader() == self.header):
                        self.body += re.sub(r'{u\'name\': u(\'.*?\'), u\'value\': u\'(.*?)\'}', r'\1:\2',oldFile.getContent())

        def writeContent(self):
                with (open(self.title, 'w')) as outFile:
                        outFile.write(self.header)
                        outFile.write(self.body)
'''

declarations, son

'''

fileCounter = 0
uniqueList = []
fileList = []
newFileList = []


'''

Now some logic.  Maybe implement some things. For reals yo.

'''
inFile = open(sys.argv[1]).read()

if os.access('temp_json', os.W_OK): # Needs some work here, probably a try-except. Also we need to generate a new directory other than 'temp_json'
        os.chdir('temp_json')
        aaronBrackets(str(unicode(inFile, errors='ignore')))
else:
        os.mkdir('temp_json')
        os.chdir('temp_json')
        aaronBrackets(str(unicode(inFile, errors='ignore')))



for file in listdir("."): # Take the cwd listing and turn that shit into a list of objects, homeskillet
        fileList.append(oldFile(file))
        os.remove(file)

for each in fileList: # Watch out, this guy knows how to use lists
        uniqueList.append(each.getHeader())


for header in (set(uniqueList)): # Maybe I'm using too many lists? Maybe you were adopted.
        newFileList.append(outFile('outfile_' + str(fileCounter) + '.csv', header))
        fileCounter += 1


for newFile in newFileList: # NOW LET'S DO THE THING!
        for oldFile in fileList:
                newFile.addContent(oldFile)
        newFile.writeContent()

