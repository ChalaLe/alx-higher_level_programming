#!/bin/bash
# sends a request to a URL passed as an argument and displays only the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"

101-post_json.sh

#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
