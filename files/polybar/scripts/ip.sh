#!/bin/bash

ip addr show enp0s3 | grep "inet " | awk  '{print $2}' | cut -d/ -f1