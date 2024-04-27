import os, sys, re

import yaml

if __name__ == "__main__":

  config_fname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "xd.yml")
  config = yaml.safe_load(open(config_fname))

  # No args
  if len(sys.argv)==1:
    #print("<directory name or pattern>", file=sys.stderr)
    sys.exit(1)

  # Print any matching path
  pattern = re.compile(" ".join(sys.argv[1:]).lower())
  for root in config['paths']:
    if config['recurse']:
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
