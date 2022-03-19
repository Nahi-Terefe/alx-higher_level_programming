#!/bin/bash
# Script to curl catch_me file and display
curl -s -H --data @catch_me 0.0.0.0:5000/catch_me
