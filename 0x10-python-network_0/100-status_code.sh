#!/bin/bash
# Status code
curl -s -o /dev/null -w '%{http_code}' "$1"
