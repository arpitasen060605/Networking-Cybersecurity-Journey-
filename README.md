# Networking-Cybersecurity-Journey
This is my learning journey from beginner to Cybersecurity Professional.

## Project 1: Port Scanner
A simple TCP port scanner built in Python.
Scans ports 1–1024 and displays open ports with service names.

## How to run
python port_scanner.py

## Concepts learned
- TCP connections & handshake
- Python socket module
- Port scanning basics

## Project 2: Network Ping Sweeper
A multithreaded ping sweeper built in Python.
Scans an entire subnet (e.g. 192.168.1.0/24) and shows which 
devices are currently active on the network.

## How to run
python ping_sweeper.py

## Concepts learned
- ICMP and the ping protocol
- Network reconnaissance (host discovery)
- Python subprocess module
- Multithreading with locks
  
## Project 3: Password Strength Analyzer
A password strength checker built in Python that scores 
passwords, flags commonly leaked ones, and estimates brute-force 
crack time using entropy calculations.

## How to run
python password_analyzer.py

## Concepts learned
- Password entropy and brute-force math
- Dictionary attacks vs brute-force attacks
- Character pool size and exponential growth
- Python sets for fast lookups

## Project 4: Network Monitoring Dashboard
A full-stack network monitoring tool, built in two phases: a Python 
CLI engine that pulls live system and network data, then wrapped in 
a Flask web app with an interactive dashboard UI.

## How to run
python app.py
Then open http://127.0.0.1:5000

## Concepts learned
- Regex for parsing system command output
- psutil for CPU/RAM monitoring
- Flask routing, templates, and Jinja2 (loops, conditionals, filters)
- GET vs POST and HTML forms
- Reusing and combining code from earlier projects
