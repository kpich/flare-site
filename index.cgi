#!/usr/bin/env python

from jinja2 import Template
import json
import os

BASE_TEMPLATE_FILE = "base.jinja"

DATA_DIR = "DATA/"
RESOURCES_FNAME = os.path.join(DATA_DIR, 'resources.json')

def main():
  with open(BASE_TEMPLATE_FILE, 'r') as inf:
    base_template = inf.read()
  template = Template(base_template)
  with open(RESOURCES_FNAME, 'r') as inf:
    resources = json.load(inf)['resources']
  #print(resources)
  print(template.render(resources=resources))

if __name__ == '__main__':
  print('Content-type: text/html; charset=utf-8\n')
  main()
