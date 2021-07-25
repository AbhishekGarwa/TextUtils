# I have created this file - Abhishek Garwa
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    charractercounter = request.POST.get('charractercounter', 'off')


    # initializing punctuations string
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Removing punctuations in string
    # Using loop + punctuation string
    analyzed = ''
    if removepunc == 'on':
        analyzed = ''
        purpose = 'Remove Puncations'
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
    djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        purpose = 'Uppercase'
        for char in djtext:
            analyzed = analyzed + char.upper()
    djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        purpose = 'New Line Character'
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
    djtext = analyzed

    if removeextraspace == 'on':
        analyzed = ''
        purpose = 'Remove Extra Space'
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
    djtext = analyzed
    if charractercounter == 'on':
        analyzed = ''
        purpose = 'Number of Characters'
        i = 0
        for char in djtext:
            i += 1
        analyzed = 'Number of Characters you Entered are '+str(i)+' Characters'

    if analyzed == '':
        return HttpResponse('Please select any operation try again')

    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

