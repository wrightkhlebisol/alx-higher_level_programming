#!/bin/bash
# Display HTTP methods accepted by the server
curl -sI "$1" | grep Allow | awk -F ': ' '{print $2}'
