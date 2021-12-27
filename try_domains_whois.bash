#!/bin/bash
for line in $(head -n $2 $1)
do
    whois "$line".com  | grep "No match for domain"
done