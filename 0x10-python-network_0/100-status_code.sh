#!/bin/bash
# Status code
curl -sI -w '%{http_code}' "$1"
