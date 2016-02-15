#!/bin/bash

# Make a data directory in ephemeral stoage
sudo mkdir -p /mnt/tmp
sudo chown ubuntu /mnt/tmp

# Grab the 2013 ACS 1 year
cd /mnt/tmp
mkdir -p acs2013_1yr
cd acs2013_1yr
sudo apt-get -y install unzip
aria2c --dir=/mnt/tmp/acs2013_1yr --max-connection-per-server=5 --force-sequential=true \
    "http://www2.census.gov/acs2013_1yr/summaryfile/2013_ACSSF_All_In_1_Giant_File(Experienced-Users-Only)/All_Geographies.zip" \
    "http://www2.census.gov/acs2013_1yr/summaryfile/Sequence_Number_and_Table_Number_Lookup.xls"
unzip -q All_Geographies.zip
