import re

# Cleans everything until the preface (all opening pages)
def cleanPreface(proceeding):
    matches = re.finditer("\f *Preface\n", proceeding)
    clean = ""
    for m in matches:
        position = m.end()
        clean = proceeding[position:]
        break
    return clean


# Cleans all running headers (with title and authors names)
def cleanHeaders(proceeding):
    clean = re.sub("\f.*[0-9]+.*\n", "", proceeding)
    return clean


# Cleans conference organization, sponsors, list of poster presentations, and table fo contents (for proceedings with
# one part)
def cleanTableContents(proceeding):
    beginning = re.search("\f *.*Organi(z|s)(ing|ation) ?(Committee)?\n", proceeding)
    end = re.search("Author Index.*\n", proceeding)
    clean = proceeding[:beginning.start()] + proceeding[end.end():]
    return clean


# Cleans conference organization, sponsors, list of poster presentations, and table fo contents (for proceedings with
# two parts)
def cleanTableContentsParts(proceeding):
    beginning = re.search("\f +(Table of )?Contents ?– ?Part I(I)?", proceeding)
    end = re.search("Author Index.*\n", proceeding)
    clean = proceeding[:beginning.start()] + proceeding[end.end():]
    return clean


# Cleans copyright footnote (until and including 2014)
def cleanCopyrightOld(proceeding):
    clean = re.sub(".*ISWC(/ASWC)? [0-9]+, (Part .+, )?LNCS [0-9]+.*\n(.+\n)*(.*Springer.*)", "", proceeding)
    return clean


# Cleans copyright footnote (from 2014)
def cleanCopyrightNew(proceeding):
    clean = re.sub(".*Springer.*\n.*ISWC(/ASWC)? [0-9]+, (Part .+, )?LNCS [0-9]+.*\n.*doi.*\n", "", proceeding)
    return clean


# Cleans reference lists
def cleanReferences(proceeding):
    clean = re.sub("References\n(.*\n)*?\f", "", proceeding)
    return clean


# Cleans list of authors from the last pages
def cleanAuthorIndex(proceeding):
    clean = re.sub(" +Author Index\n(.*\n)*", "", proceeding)
    return clean


# Cleans some tables
def cleanTables(proceeding):
    clean = re.sub("Table [0-9]+[.].+\n^\n+(.+\n)+?^\n^\n", "", proceeding, flags=re.MULTILINE)
    return clean


# Cleans figure captions
def cleanFigures(proceeding):
    clean = re.sub("Fig\. [0-9]+[.].+(.+\n)+?^\n^\n", "", proceeding, flags=re.MULTILINE)
    return clean


# Cleans any line with more than 5 consecutive spaces
def cleanStrangeSpaces(proceeding):
    clean = re.sub("^       *.*\n", "", proceeding, flags=re.MULTILINE)
    return clean


# Cleans extra lines (any sequence of two empty lines)
def cleanExtraLines(proceeding):
    clean = re.sub("\n\n", " ", proceeding, flags=re.MULTILINE)
    return clean