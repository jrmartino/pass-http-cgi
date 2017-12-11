#!/usr/bin/env python

# A simple HTTP server that responds to POSTs by running a shell command
# Usage: python cgi_server.py &

import BaseHTTPServer
from subprocess import call

# Edit these values to control the server behavior
PORT    = 7000
COMMAND = "java"
ARGS    = ["-jar",
           "nihms-cli-1.0.0-SNAPSHOT-shaded.jar",
           "/usr/local/src/huims-submission/nihms-cli/src/main/resources/FilesystemModelBuilderTest.properties",
           "local"
          ]


# Define a request handler class that runs a command when it receives a POST
class RequestHandler (BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(s):

        # Execute the command and prepare the POST response code.
        # Prints an error message to the console on failure.
        # This is a blocking function.  Use subprocess.Popen for non-blocking.
        try:
            status = call([COMMAND]+list(ARGS))
            if status != 0:
                args = " ".join(str(x) for x in ARGS)
                print "Command '{} {}' failed with code {}".format(COMMAND, args, status)
                code = 500
            else:
                code = 200
        except:
            args = " ".join(str(x) for x in ARGS)
            print "Command '{} {}' failed with an exception".format(COMMAND, args)
            code = 500

        # Prepare and send the response header
        s.send_response(code)
        s.send_header("Content-type", "text/html")
        s.send_header("Access-Control-Allow-Origin", "*")
        s.end_headers()

# Create and run the server
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(("", PORT), RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
