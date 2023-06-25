#!/usr/bin/env bash

# to display messages with different formating and styles
message_newline(){
  echo
}

#  @ is the arguments passed to the function
message_debug(){
  echo -e "DEBUG: ${@}"
}

# msg passed in as arguments will ne displayed in bold
message_welcome(){
  echo -e "\e[1m${@}\e[0m"
}

# for es===========
message_warning(){
  echo -e "\e[33mWARNING\e[0m: ${@}" 
}

# changing color to red and reerse the change as well
message_error(){
  echo -e "\e[31mERROR\e[0m: ${@}"
}

# msg in light grey
message_info(){
  echo -e "\e[37mINFO\e[0m: ${@}"
}

# msg in yellow
message_suggestion(){
  echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

# msg in green





message_success(){
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}