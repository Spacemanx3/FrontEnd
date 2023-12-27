#!/bin/bash

# Check if port 8000 is open on localhost (127.0.0.1)
if nc -zv 0.0.0.0 8000; then
    echo "Port 8000 is open. Displaying 'Hello, World2!' on the web page."
    echo -e "HTTP/1.1 200 OK\r\nContent-Length: $(echo -n 'Hello, World2!' | wc -c)\r\n\r\nHello, World2!"
else
    echo "Port 8000 is not open. Please make sure your web server is running on localhost:8000."
fi
