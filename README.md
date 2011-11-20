Zeromon
=======

About
-----

I was looking for simple, lightweight, server monitoring tools.  My
hosting provider has been sending me emails telling my server has been
rebooted due to going over its memory quota (Though it never actually
does get rebooted, every time I get one of those emails, the uptime is
still measured in days), but the monitoring they provide never shows
me over half my quota, and usually under 1/3rd.  So, I've probably got
some very brief spikes going on that are below the granularity of the
tools they give me, but still triggering alerts from their automated
systems.

I had some goals:

* It shouldn't take more than 5 minutes to install and configure
* It should graph, in a browser, my server's overall memory utilization with a granularity of 5 seconds or better
* If I see a spike, I should be able to easily figure out what process(es) caused it

I basically gave up after failing to build, install, or configure
several different packages.  I'm still certain the package I wanted
exists.  But I'm a programmer, dammit, I'll just write my own thing.
So here it is.  If you try to use it, it will probably fail the first
requirement, it relies on things I already have lying around:

* luajit
* buzz (another project of mine, a lua web framework)
* zeromq, plus python AND lua bindings for same

Plus it only monitors one thing and has no configuration to speak
of. It does what I needed it to, that's all.

Running it
----------
* On your server to be monitored, run python server.py

* On any machine that can talk to the server, modify buzzclient/webmon.lua to point to your server. You can run it on the same machine as the server if you want, but if you're concerned with memory usage, why run even more stuff on that server?
* Run webmon.lua with luajit
* Point a browser at http://(machine-with-webmon):9901/index.html
* Behold your memory usage!
* Watch the output from webmon.lua too to see the top 5 processes by memory usage at each tick.  Not in the web interface (yet?)

You can also run client.py if you JUST want to watch the raw sample data.

For the curious
---------------

The big spikes I've identified using this so far are from php
processes, not the django apps I was kind of expecting to be the
problem spots.  Which narrows it down to one of four wordpress blogs
on the server (None of them are high traffix, and two of them are
practically invisible to the world).  Loading the main pages myself
causes spikes too, but not as big as some of the others I've seen.
There must be something that causes larger memory usage that users are
doing, perhaps spam comments getting blocked automatically, for
example.  I haven't tried to correlate it with the rest of my logs
yet.
