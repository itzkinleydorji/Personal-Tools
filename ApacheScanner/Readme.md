#### ApacheScan
apacheScan is a simple Python script that scans a given Apache version against a local database of known CVEs to check for potential vulnerabilities.

#### Features
- Scans Apache version strings against a CVE database (apache_CVE.txt)

- Highlights found vulnerabilities in the terminal

- Uses color-coded output for better readability

#### Requirements
- Python 3.x

#### Usage 
```JSON
git clone https://github.com/itzkinleydorji/Personal-Tools/ApacheScanner.git
```
```JSON
cd ApacheScanner
```
```JSON
sudo chmod +x scan.py
```
```JSON
sudo python scan.py apache version 
sudo python scan.py 2.2.8
```
#### Notes
- Make sure the apache_CVE.txt file exists in the same directory as the script and is readable.

- This tool does not perform live scanning. It only checks the version string against a local static database.

#### License
[MIT License](https://github.com/itzkinleydorji/License) 