# Software Details

This file aims to provide more details on how to get the software working. 
Most of it shouldn't apply to you.
Its mainly to cut down on any questions.

## Necessary Stuff 

- Start Powershell as administrator
- type: New-NetFirewallRule -LocalPort 12000 -Action Allow - Profile Any
- type: New-NetFirewallRule -LocalPort 12010 -Action Allow - Profile Any
- type: New-NetFirewallRule -LocalPort 12100 -Action Allow - Profile Any
- type: New-NetFirewallRule -LocalPort 12110 -Action Allow - Profile Any
- type: New-NetFirewallRule -LocalPort 12200 -Action Allow - Profile Any
- type: New-NetFirewallRule -LocalPort 12210 -Action Allow - Profile Any

These commands allow for the software to send and recieve the data.
If you cannot get administrator to unblock those ports, then the software cannot receive any information.

## Downloads and installation:

If you have not done so already, you will need to download various software:
- Python - Any version after 3.6 - I coded it all on python 3.11
- Node.js - Any version afer 12.X - I coded it all on v12.11.0
- Electron - Any version after 11.X - I coded it all on v34.0.0

I will not provide any requirement download/installation websites.
I do not want to have responsability about any accidently injected malware.
