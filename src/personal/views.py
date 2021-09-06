from django.shortcuts import render

# Create your views here.

def home_screan_view(request):
    # ex) 1
    # content = {}
    # content["my_number"] = "sisad hezaro bist o char"

    # ex) 2
    # content = {
    # "my_number": "charsad bist o char yea yea212",
    # "khersi": "khersi is here \n his name is coli"
    # }

    # ex) 3
    content = {}
    listOfBooks = ["work harder","clean code","best program","khajebe"]
    listOfBooks.append("TAMARKOZ")

    content["listOfBooks"] = listOfBooks
    return render(request,"personal/home.html",content)
