The cgi_server.py script implements a simple server for use during the PASS project demonstration.
The server can be called from the Ember-based web site to invoke back-end FTP functionality.
The server returns code 200 on success and 500 on failure of the command.
It prints a message to the console when the command fails.

Preparing the script:
    Save cgi_server.py in the desired location and use chmod to make it executable by necessary users/groups.
    Edit the script's constants to specify the listening port and the command to invoke and its arguments.
    
Preparing the computer:
    Make sure the Linux system firewall allows inbound traffic on the specified port.
    If the system is a cloud instance, it's security protocal must also allow inbound traffic on that port.
    Make sure python 2.7 is installed on the system.

Usage:
    cd to directory containing cgi_server.py
    python cgi_server.py &