import os, sys, re

import configparser

if __name__ == "__main__":

  config_fname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "xd.ini")
  config = configparser.ConfigParser()
  config.read(config_fname)

  recurse = config.getboolean('General', 'recurse')
  dirs = [dir.strip() 
            for dir in config.get('General', 'paths').split("\n") 
              if dir!='']
  
  # No args
  if len(sys.argv)==1:
    #print("<directory name or pattern>", file=sys.stderr)
    sys.exit(1)

  # Print any matching path
  pattern = re.compile(" ".join(sys.argv[1:]).lower())
  for root in dirs:
    if recurse:
      for root, dirs, files in os.walk(root):
        for dir in dirs:
          path = os.path.join(root, dir)
          if pattern.search(path.lower()):
            print(path)
    else:
      # Don't recurse:
      for dir in os.listdir(root):
        path = os.path.join(root, dir)
        if os.path.isdir(path):
          if pattern.search(path.lower()):
            print(path)
