#!/usr/bin/env bash

yes_no(){
    # description variable
  declare desc="Prompt for confirmation. \$\"\{1\}\": confirmation message"

  local arg1="${1}"

  local response= read -r -p "${arg1} (y/[n])? " response
    
    # if user response matches the y or Y regex
  if [[ "${response}" =~ ^[Yy]$ ]]
    # if matches
  then
    exit 0
    # if doen't matches
  else
    exit 1
  fi
}
