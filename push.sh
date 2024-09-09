#!/bin/bash
# aws s3 command that will push the currect directory files in the cloud storage bucket in aws 
aws s3 sync local-directory-path s3://bucket-name/path/ --recursive
