#!/bin/bash
sleep 20s;
echo "Writing data into DB"
for filename in *.py; do
    python $filename || true
done
echo "Done writing data, shutting down."
exit 0