## NMEA GPS Server, written in Python

## Purpose
Receive real-time GPS NMEA messages over a network to a server.  Project the coordinates to local from WGS84 into a local coordinate system.  Store results in a database.  Scope - NMEA GPGGA NMEA messages only.  


## Building

1) Install Python 2.7.11 or newer

2) Install git

3) CD to repo directory

4) Run cmd git clone https://github.com/ryanbaumann/NMEA_GPS_Server.git

5) Run cmd "pip install -r requirements.txt"

If you have any errors installing the python files (especially on Windows), try installing the files from Wheels (pre-built distribution packages).  The python pre-built packages are included in the repo at /python_wheels.  To install a package, run command "pip install <path_to_wheels_file>"


## Configuring

1) Open nmea_gps_server.py to alter database settings on lines 22-28

2) Set server listening port on line 35.  Default is port 10110.  

## Running

CD to the rep directiory and run "python nmea_gps_server.py".  

--The server will listen for and store GPGGA NMEA messages sent to the configured port (default 10110).  The data will be stored in the database and table configured in lines 22-28 of nmea_gps_server.py

## Credits

* [Ryan Baumann] (https://ryanbaumann.com) 

## License
The MIT License (MIT)

Copyright (c) 2016, Ryan Baumann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
