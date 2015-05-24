# -*- coding: utf-8 -*-

import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# In the handler we decide what code the execute based on the type of http request that is sent to the server
class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self): # simple pattern matching plan
		try: 
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "Hello!"
				output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return
			
			if self.path.endswith("/hola"):
 				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
 				output += "<html><body>"
				output += "&#161Hola  <a href='/hello'>Back to Hello</a>"
 				output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
				output += "</body></html>"
				self.wfile.write(output)
 				print output
 				return
		except:
			self.send_error(404, "File Not Found %s" % self.path)
	def do_POST(self):
		try: 
			self.send_response(301)
			self.end_headers()
			
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')
			output = ""
			output += "<html><body>"
			output += "<h2> Okay, how about this: </h2>"
			output += "<h1> %s </h1>" % messagecontent[0]
			
			output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
			output += "</body></html>"
			self.wfile.write(output)
			print output
			return						
		except:
			pass


# In main we instantiate our server and specify what port the web server will listen on
def main(): 
	try:
		# creating the HTTPServer class
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Web server running on port %s" % port
		# to keep the server constantly listening
		server.serve_forever()		

	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()

if __name__ == '__main__':
	main() 
