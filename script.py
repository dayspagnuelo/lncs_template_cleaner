import os
import cleaner

path = "iswc/txt/"

for file in os.listdir(path):
    if "iswc" in file:
        print("Cleaning file: ", file)
        proceedings = open(path+file, "r+")
        content = proceedings.read()
        proceedings.close()

        content = cleaner.cleanPreface(content)
        content = cleaner.cleanHeaders(content)
        content = cleaner.cleanTableContents(content)

        # For proceedings with two parts
        if "-" in file:
            content = cleaner.cleanTableContentsParts(content)

        # For proceedings until 2014
        if int(file[4:8]) < 2015:
            content = cleaner.cleanCopyrightOld(content)
        else:
            content = cleaner.cleanCopyrightNew(content)

        content = cleaner.cleanReferences(content)
        content = cleaner.cleanAuthorIndex(content)
        content = cleaner.cleanTables(content)
        content = cleaner.cleanStrangeSpaces(content)
        content = cleaner.cleanExtraLines(content)

        if content:
            cleanProceedings = open(path+file, "w+")
            cleanProceedings.write(content)
            cleanProceedings.close()
