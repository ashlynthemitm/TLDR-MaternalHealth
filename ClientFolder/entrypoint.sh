#!/bin/bash

# Execute the Python script
python client-side.py

#Execute the SQL commands using psql
#psql -h 104.211.45.109 -p 8888 -U azureuser -d fetaldevelopment -f /app/input-fd-data.sql

psql -U azureuser -d database -f input-tldr-data.sql