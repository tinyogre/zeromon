Zeromon
=======

About
-----

I was looking for simple, lightweight, server monitoring tools.  I had some goals:
* It shouldn't take more than 5 minutes to install and configure
* It should show me my server's overall memory utilization with a granularity of 5 seconds or better
* If I see a spike, I should be able to easily figure out what process(es) caused it

I basically gave up after failing to build, install, or configure
several different packages.  I'm still certain the package I wanted
exists.  But I'm a programmer, dammit, I'll just write my own thing.
So here it is.  If you try to use it, it will probably fail the first
requirement, it relies on things I already have lying around:

* luajit
* buzz (another project of mine)
* zeromq, plus python AND lua bindings for same

Plus it only monitors one thing and has no configuration to speak
of. It does what I needed it to, that's all.

Running it
----------
* On your server to be monitored, run python server.py

* On any machine that can talk to the server, modify buzzclient/webmon.lua to point to your server.
* Run webmon.lua with luajit
* Point a browser at http://<machine-with-webmon>:9901/index.html
* Behold your memory usage!
* Watch the output from webmon.lua too to see the top 5 processes by memory usage at each tick.  Not in the web interface (yet?)

