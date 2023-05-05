
# Scapy Port Scanner

A simple TCP stealth port scanner using Scapy.


## Setup

Follow these steps to set up and run the Scapy port scanner:


1. Install Python 3.10.6.
2. Create a directory name ‘Scapy’ and go to that directory.

3. Run the below commands.
      - `python3.10.6 -m venv env		      # creates a python virtual environment name ‘env’.`
      - `source env/bin/activate		      # activates the virtual environment.`
      - `pip install -r requirements.txt		# install the required Python modules.`

4. Copy the code into the file ‘scapy_portScanner.py’.
5. Run the below command to do the port scanning for a desired host. Here '--start_port' and '--end_port' are optional arguments. The default values for '--start_port' is 1 and '--end_port' is 1024 and can be changed in the code.
      - `python scapy_portScanner.py 192.168.1.1 --start_port 0 --end_port 1024`
      
      

**Note**: Scanning ports without permission is illegal and unethical. Always obtain permission before scanning a network or host.

