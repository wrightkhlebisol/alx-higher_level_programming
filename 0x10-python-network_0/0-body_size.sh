#!/bin/bash
# Curl body size
curl -s -w '\n%{size_download}\n' "$1" | tail -n 1
