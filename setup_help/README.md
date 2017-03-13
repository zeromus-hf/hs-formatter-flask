I used the two PDFs in this directory to help get uWSGI setup with nginx. The root folder
is all the files that would have been made to configure the app.


The links for the two PDFs are [here](http://vladikk.com/2013/09/12/serving-flask-with-nginx-on-ubuntu/)
and [here](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms).

Also I modified `target_source/main.py` to load the script from an absolute path, may want
to make that configurable sometime.
