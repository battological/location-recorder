#!/usr/bin/python


from BaseHTTPServer import HTTPServer
from datetime import datetime
from pprint import pprint
from sys import argv
from SimpleHTTPServer import SimpleHTTPRequestHandler
from urlparse import parse_qs


class HTTPHandler(SimpleHTTPRequestHandler):

	def do_POST(self):
		# Get location
		length = int(self.headers.getheader('content-length'))
		raw_params = self.rfile.read(length)
		params = parse_qs(raw_params)

		# Log location
		pprint(params)

		# Record location properly
		with open('locations.csv', 'a') as out:
			out.write(','.join([params['lat'][0], params['lon'][0], str(datetime.now())])+'\n')
		
		# HTTP response
		self.send_response(201)
		self.send_header('Refresh', '0;done.html')
		self.end_headers()


if __name__ == '__main__':
	try:
		port = int(argv[1])
		print('Starting server on port {}'.format(str(port)))
		server = HTTPServer(('', port), HTTPHandler)
		server.serve_forever()
	except IndexError:
		print('Forgot port!')
	except KeyboardInterrupt:
		print('Shutting down')
		server.socket.close()
