Location Recorder
=================

Dumb little app to record your location.

# Setup

Requires a `private.js` file that looks like:

```
var apiKey = yourApiKey;
var homeLat = yourHomeLat;
var homeLon = yourHomeLon;
```

`apiKey` is your Google API key.
`homeLat` and `homeLon` are the spot to initialize your map before locating yourself.

# Run

The server was written for Python 2.7.6. It uses only the standard library. To run the server:

```
python server.py [port]
```

where `[port]` is the port on which you want to run the server.

Then navigate to <http://localhost:[port]> (substituting your chosen port).
