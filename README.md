# Simple image service

This repo provides a simple Python-Flask Server for image processing capabilities using Python, for POC of imagekit replacement 


## Pending Items
* Resize API Storage to s3
* Caching 
   * Local caching BYTES/resized extension
   * Global -> CDN Caching 


## simpleimageserver 0.1 API endpoints 

### /env [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "env": # dump of available environmental variables,
             "version": $VERSION
         }


### /health [0.1]

        HTTP/1.1 200 OK
        $HEADER_FIELDS
         {
             "delay in seconds": $HEALTH_DELAY,
             "version": $VERSION,
             "healthy": true
         }


### /info [0.1]

        HTTP/1.1 200 OK
        $HTTP_HEADERZ
         {
             "from": "$REMOTE_IP",
             "host": ""$HOST:$PORT"",
             "version": "$VERSION"
         }




By setting the following environment variables, you can change the runtime behaviour of simpleservice:

    - PORT0 - the port simpleservice is serving on
    - VERSION - the value of version returned in the JSON response of the /endpoint0 endpoint
    - HEALTH_DELAY - delay in milliseconds that the /health endpoint responds

## How to Run this Code

0. Ensure Python 3.6+ has been installed, then use `pip` to install Flask.

        python3 -m pip install flask

0. Run the code with Python 3.6+

        python3 simpleimageservice.py
        
0. Set the environmental variable `VERSION` to "24601" and `PORT0` to "8887", then launch the server.

        VERSION=24601 PORT0=8887 python3 simpleflaskservice.py
