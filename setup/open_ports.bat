@echo off
s
netsh advfirewall firewall add rule name="Allow Port 12000" dir=in action=allow protocol=TCP localport=12000 profile=any
netsh advfirewall firewall add rule name="Allow Port 12010" dir=in action=allow protocol=TCP localport=12010 profile=any
netsh advfirewall firewall add rule name="Allow Port 12100" dir=in action=allow protocol=TCP localport=12100 profile=any
netsh advfirewall firewall add rule name="Allow Port 12110" dir=in action=allow protocol=TCP localport=12110 profile=any
netsh advfirewall firewall add rule name="Allow Port 12200" dir=in action=allow protocol=TCP localport=12200 profile=any
netsh advfirewall firewall add rule name="Allow Port 12210" dir=in action=allow protocol=TCP localport=12210 profile=any

echo All ports have been opened.
