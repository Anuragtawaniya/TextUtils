from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def removepunch(request):
    # get the text
    text = request.POST.get('text', 'default')
    # check checkbox value
    removepunch = request.POST.get('removepunch', "off")
    uppercase = request.POST.get('fullcaps', "off")
    extraspaceremover = request.POST.get('extraspaceremover', "off")
    newlineremover = request.POST.get('newlineremover', "off")
    charcount = request.POST.get('charcount', "off")
    params = {}
    # checkbox on or off
    if (removepunch == "on"):
        punchuation = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        analyze = ""

        # check the char in punchuation string
        for ch in text:
            if ch not in punchuation:
                analyze += ch
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyze}
        text = analyze
        # return render(request, 'removepunch.html', params)

    elif (uppercase == "on"):
        analyze = ""
        for ch in text:
            analyze += ch.upper()

        params = {"purpose": "Uppercase", "analyzed_text": analyze}
        text = analyze
        # return render(request, 'removepunch.html', params)

    elif (newlineremover == "on"):
        analyze = ""
        for ch in text:
            if not ch != "\n" and ch != "\r":
                analyze += ch

        params = {"purpose": "newlineremover", "analyzed_text": analyze}
        text = analyze
        # return render(request, 'removepunch.html', params)

    elif (extraspaceremover == "on"):
        analyze = ""
        for index, ch in enumerate(text):
            if not (text[index] == " " and text[index+1] == " "):
                analyze += ch
        params = {"purpose": "extraspaceremover", "analyzed_text": analyze}
        text = analyze

        # return render(request, 'removepunch.html', params)
    elif (charcount == "on"):
        analyze = len(text)

        params = {'purpose': "counting the character",
                  "analyzed_text": analyze}

    elif(charcount == "off" and extraspaceremover == "off" and newlineremover == "off" and uppercase == "off" and removepunch == "off"):
        return HttpResponse("Please select any operation and Try again):")

    return render(request, "removepunch.html", params)
