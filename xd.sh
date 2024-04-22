#!/bin/bash

# To use, add this to your .bashrc:
# alias xd=". /path/to/xd.sh"

# Run python script in current directory & capture its output in a variable
RESULT=`python "$(dirname ${BASH_SOURCE[0]})/xd.py" $@`
COUNT=`echo "$RESULT" | grep -v "^$" | grep -c '^'`

if [ -z "$1" ]; then
  echo "xd <directory name or pattern>"
elif [ "$COUNT" -eq 0 ]; then
  echo "No directories match this pattern"
elif [ "$COUNT" -eq 1 ]; then
  if [ -n "$RESULT" ]; then
    cd "$RESULT" || exit
  fi
else
  echo "$RESULT"
  echo
  echo "$COUNT directories match this pattern"
fi
