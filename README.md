TVBot
=====

TVBot resolves bookmark rotation, through Selenium, 
for presentation on television. (For example, for Raspberry Pi TV or other similar solutions)

The advantage of this is that TVBot communicates via WebSocket, 
so it is possible to add or delete addresses to the stations without using the keyboard of station.

Installation
-----------

### Git

```bash
git clone git@github.com:geekmoss/tv-bot.git
cd tv-bot
pip install .
```

Usings
------

### TV (Station)

```bash
# With default host & port from ENV

TVBOT_HOST="http://websocket-server"
# TVBOT_PORT=9600  # Default is 9600

# Get list of URLs
tvbot-cli ls
# Add url to list
tvbot-cli put http://google.com/
# Remove url from list
tvbot-cli rm http://google.com/

# Or with switches
tvbot-cli ls --host http://localhost --port 9700 
```

### Server

```bash
tvbot-socket-server  # Default is 0.0.0.0:9600
```

### CLI Client

```bash
tvbot-tv --delay 10 --host http://websocket-server
# delay is speed of rotation, default is 30 sec
# host for specific host, default is from TVBOT_HOST or http://localhost  
```