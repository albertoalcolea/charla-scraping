from django.shortcuts import render
from django.http import JsonResponse, Http404

from main.forms import PageForm

from django.views.decorators.csrf import ensure_csrf_cookie



# Create your views here.


PARRAFO = 10 *'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu nisi hendrerit, imperdiet ipsum in, tristique justo. Cras vel sem at nibh iaculis sagittis. Vivamus elementum odio non porta dapibus. Pellentesque sit amet lorem neque. Quisque id lacus interdum, porta est vitae, cursus turpis. Praesent vitae nisl fringilla nibh tincidunt varius nec efficitur purus. Suspendisse massa magna, placerat pharetra orci rutrum, tempus suscipit felis. Vestibulum vehicula ex quis justo pretium gravida. Vivamus sed risus eget lacus molestie euismod non non lectus. Morbi vestibulum tristique tincidunt. Nunc vitae mi congue, ullamcorper ipsum eu, hendrerit massa. Aenean molestie tellus consectetur condimentum tempus. Cras tempus vel leo viverra hendrerit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque pharetra massa arcu. Phasellus rutrum porta erat non maximus.'

def _gen_parrafo(page):
	return 'Pagina {0}  -  {1}'.format(page, PARRAFO)

@ensure_csrf_cookie
def index(request):
	context = {
		'parrafo': _gen_parrafo(1),
	}
	return render(request, 'index.html', context)

@ensure_csrf_cookie
def more(request):
	# if not request.is_ajax(): raise Http404
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			page = int(form.cleaned_data['page'])
			response = {
				'status': 'ok',
				'parrafo': _gen_parrafo(page)
			}
			return JsonResponse(response)
		else:
			print 'Form invalid'
	else:
		print 'Method invalid'
