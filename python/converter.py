#!/usr/bin/python
import sys

def aaronBrackets ( aString ):
        counter = 0
        for char in aString:
                if char == '{':
                        sys.stdout.write(char)
                        counter += 1
                elif char == '}':
                        if counter % 2 == 0:
                                sys.stdout.write(char)
                                counter -= 1
                        elif counter % 2 == 1:
                                sys.stdout.write(char)
                                sys.stdout.write("\n\n")
                                counter -= 1
                else:
                        sys.stdout.write(char)
print(aaronBrackets(open(sys.argv[1]).read().decode("utf8").encode("ascii")

