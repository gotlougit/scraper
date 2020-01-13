"""
Scraper:
    A simple web scraper built purely in Python
"""

def getPage(url):
    """Gets the entire webpage as a list of strings"""

    from urllib.request import urlopen
    rawpage = urlopen("https://"+url+"/").read()
    a = ""
    webpage = []
    for i in rawpage:
        i = chr(i)
        if i != '\n':
            a+=i
        elif i == '\n':
            webpage.append(a)
            a = ""
    return webpage

def getTags(lst):
    """Gets a list of tags in the webpage"""

    tagList = []
    string = ""
    for line in lst:
        for i in line:
            if i != "<":
                string+=i
            if i == ">":
                tagList.append(string)
                string = ""
    return tagList

def searchTag(tagList, tagname):
    """Searches for specific tags inside the given list of tags"""

    results = []
    x = len(tagname)
    for tag in tagList:
        if str(tag[:x]) == tagname and tag not in results:
            results += [tag]
    return results

def searchAttr(taglist, attr):
    """Searches for tags with a particular attribute in the list of tags"""

    results = []
    for tag in taglist:
        if attr in tag and tag not in results:
            results += [tag]
    return results

def getTagAttributes(tagList, tagname, attribute):
    """Searches for a specific tag with a particular attribute in the list of tags"""
    
    x = len(tagname)
    attrs = []
    for tag in tagList:
        if str(tag[:x]) == tagname and attribute + "=" in tag:
            j = tag.partition(attribute + "=")[2].split('"')
            if len(j) == 1:
                j = tag.partition(attribute + "=")[2].split("'")
            for i in j:
                if len(i) != 0 and (i[0] == " " and i[-1] == "="):
                    z = j.index(i)
                    j = j[:z]
                    break
            a= ""
            for i in j:
                a+=i
            a = a.replace(">","")
            a = a.replace("\x80\x98","")
            if a not in attrs:
                attrs.append(a)
        else:
            continue
    return attrs

def removeSpecialChars(l):
    """It cleans up the output to remove any HTML-specific characters"""
    
    from html import unescape
    for i in range(len(l)):
        l[i] = unescape(l[i])
        l[i] = l[i].replace('â',"'")
    return l
