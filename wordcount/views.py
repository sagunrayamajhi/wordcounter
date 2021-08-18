import operator
import re

from django.http import HttpResponse
from django.shortcuts import render
import operator


def homePage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordDict ={}
    for wordz in words:
        word = re.sub("[^0-9a-zA-Z]+","",wordz)
        if word in wordDict:
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1),reverse=True)
    print(sortedWords)

    return render(request,'count.html',{'fullText':fulltext,'count':len(words),'sortedWords':sortedWords})

def about(request):
    return render(request,'about.html')
