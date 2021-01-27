from werkzeug.wrappers import Request, Response

def render_template(template_name='HomePage.html',context =
{}):
	html_str = ""
	with open(template_name,'r') as f:
		html_str = f.read()
		html_str = html_str.format(**context)
	return html_str

def home(environ):
	return render_template('HomePage.html',context={})
def application(environ, start_response):
	path = environ.get('PATH_INFO')
	#environ.path = 'E_cart'
	if path == '/':
		data = home(environ)
	else:
		data = render_template('404.html',context={"path":path})
	data = data.encode('utf-8')
	response = Response(data,mimetype='text/html')
	return response(environ, start_response)
