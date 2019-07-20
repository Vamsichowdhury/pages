from django.shortcuts import render


def home(request):
	return render(request,"message_board_app/home.html")

def blogs(request):
	return render(request,"message_board_app/blogs.html")
