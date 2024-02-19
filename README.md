# WiiUBOSSDumper

Easily dump the BOSS databases from your Wii U console.

Heavily based off of [autodance-convert](https://github.com/oscie57/autodance-convert)

## Pre-requisites

- A Wii U with [Aroma custom firmware](<https://aroma.foryour.cafe/>)
- [Python 3.9](<https://www.python.org/downloads/release/python-390/>) or above
- The FTPiiU Aroma plugin

## Instructions

1. Make sure you have a system with Aroma custom firmware with the FTPiiU plugin enabled.
2. In the Wii U Plugin System Config Menu, make sure that in FTPiiU - Settings, that "Allow access to system files" is enabled"
3. Write down your console IP address.
4. Run `pip install ftputils`
5. Run `python3 dump.py` and input the console's IP address.
6. Wait until the script is complete, open the `output` folder and send `output.zip` here.
