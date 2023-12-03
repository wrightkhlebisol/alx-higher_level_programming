#!/bin/bash
# Post JSON
curl -s -X POST "$1" --data-binary "@$2"
