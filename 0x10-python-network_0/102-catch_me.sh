#!/bin/bash
# Take in filename and URL, post contents of file; Usage: ./102-catch_me.sh ; echo ""
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
