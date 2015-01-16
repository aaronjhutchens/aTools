#!/usr/bin/python
import sys

def aaronBrackets ( aString ):
        counter = 0
        fileCount = 0
        file = open('output_'+str(fileCount)+'.JSON', 'w')
        for char in aString:
                if char == '{':
                        file.write(char)
                        counter += 1
                elif char == '}':
                        if counter == 1:
                                file.write(char + ']')
                                file.close()
                                file = open('output_' + str(fileCount) + '.JSON', 'w')
                                fileCount += 1
                                counter -= 1
                        else:
                                file.write(char)
                                counter -= 1

                else:
                        file.write(char)


print(aaronBrackets(unicode(open(sys.argv[1]).read(), errors='ignore')))

