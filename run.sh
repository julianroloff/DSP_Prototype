#!/bin/bash
# Start the Fuseki server
cd /apache-jena-fuseki-5.2.0
./fuseki-server &
# Give the server a few seconds to start
sleep 5
# Navigate to your project directory and run the script
cd "/Users/julian/Desktop/Master UvA/Semester 1/Data Systems Project/DSP Prototype"
source venv/bin/activate
python main.py
