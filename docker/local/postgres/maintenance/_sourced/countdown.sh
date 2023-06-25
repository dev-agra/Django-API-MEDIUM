#!/usr/bin/env bash

# takes a int mumber as arg and displays the same in the terminal
# timer runs updates itslef in real time until the specified numbe rof seconds have elapsed
countdown(){

  declare desc="A simple countdown."

  local seconds="${1}"

  local d=$(($(date +%s) + "${seconds}"))
# while loop runs as until the critical date "d" matches the current date got using date +%s
  while [ "$d" -ge `date +%s` ]; do
#   hours min seconds
# calculates the remaining time by subtracting the current time and the target time and converting the same to a human readable format of H M S
    # remianing time displayed on the same line so as to render effect of a countdown timer and the -ne flag allows us to use the \r flag ie.e. new line character
    echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r";

    sleep 0.1
  done

}