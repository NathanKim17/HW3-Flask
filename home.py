from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

#different URL the app  will implement
@myapp_obj.route("/")
def home():
    user = {'username': 'Nathan'}
    city_names = ['Paris','London','Rome', 'Tahiti']
    name = "Lisa"

    return '''
	<html>
	<head>
		<title>Home Page - my blog</title>
	</head>
	<body>
		<h1>Welcome ''' + name + '''!</h1>
        <a href="https://www.google.com"> not google</a>
        <ul>
            <li>''' + city_names[0] + '''</li>
            <li>''' + city_names[1] + '''</li>
            <li>''' + city_names[2] + '''</li>
            <li>''' + city_names[3] + '''</li>
        </ul>
	</body>
	</html>'''


myapp_obj.run()