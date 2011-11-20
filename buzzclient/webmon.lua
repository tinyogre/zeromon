
require('buzz')
require('zmq')
require('poller')

local zctx = zmq.init(1)
local sub = zctx:socket(zmq.SUB)
sub:connect('tcp://rumsey.org:9900')
sub:setopt(zmq.SUBSCRIBE, '')

function static(request, args)
  print('static '..args[1])
  if string.find(args[1], '[.]/') then
	buzz.error(request, 404, 'Invalid path')
	return
  end
  local file
  if args[1]:find('[.]js$') then
    print('open js/'..args[1])
    file = io.open('js/'..args[1])
  else
    file = io.open('static/'..args[1])
  end
  buzz.response(request, file:read('*a'))
end
buzz.get('^/(index.html)$', static)
buzz.get('^/js/(.*)$', static)

function sample(request)
  buzz.response(request, last_sample)
end
buzz.get('/sample', sample)

buzz.init(9901)

function get_sample()
  print('get_sample')
  last_sample = sub:recv()
  print(last_sample)
end

-- Block until one message has been received
local message = sub:recv()
last_sample = message
print(last_sample)

local poller = poller(2)
poller:add(sub, zmq.POLLIN, get_sample)

while true do
  poller:poll(0)
  buzz.poll(1000)
end


