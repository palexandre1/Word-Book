from django.shortcuts import render
from django.http import HttpResponse

from lookup.models import Entry
from django.template.loader import render_to_string
from django.http import JsonResponse



	# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")

	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		words = Entry.objects.filter(word__icontains=url_parameter) #SQL comes before icontains...SQL__icontains
	else:
		words = Entry.objects.all()


	ctx["words"] = words
	if request.is_ajax():
		html = render_to_string(
	    	template_name="word-results-partial.html", 
	    	context={"words": words}
		)
		data_dict = {"html_from_view": html}
		return JsonResponse(data=data_dict, safe=False)

	return render(request, "home.html", context = ctx)


def contact_view(request, *args, **kwargs):

	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):

	my_context = {
	"my_text": "This is about me",
	"my_number": 123,
	"my_list": [123,4242, 12313]

	}
	return render(request, "about.html", my_context)