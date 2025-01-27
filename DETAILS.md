# Software Details

This file aims to provide more details on how to get the software working.
Most of it shouldn't apply to you.
Its mainly to cut down on any questions.

## Ports

In order for the software to be able to communicate from one computer to another, you need to open the following ports.
I have listed the various ports below with the port number and the reason for its use.

12010 - pc_info.py sender port
12000 - pc_info.py receiver port
12110 - msg.py sender port
12100 - msg.py receiver port
12210 - file_transfer.py sender port
12200 - file_transfer.py receiver port

I have provided a dedicated folder for the opening of those ports. You can find it in the following (relative) path:
/setup. You #NEED# to be in administrator mode to open the ports.
Be aware that those files only work on Windows. I have no plans on trying to get them to work on Linux or macOS.

## Downloads and installation

If you have not done so already, you will need to download various software:

- Python - Any version after 3.6 - I coded it all on python 3.11
- Node.js - Any version afer 12.X - I coded it all on v12.11.0
- Electron - Any version after 11.X - I coded it all on v34.0.0

I will not provide any requirement download/installation websites.
I do not want to have responsability about any accidently injected malware.
