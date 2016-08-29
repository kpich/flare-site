#!/usr/bin/env python

from jinja2 import Template
import json
import os
import csv

def to_utf8(lst):
    return [x.decode('utf-8') for x in lst]

BASE_TEMPLATE_FILE = "base.jinja"

DATA_DIR = "DATA/"
RESOURCES_FNAME = os.path.join(DATA_DIR, 'resources.json')
PAPERS_CSV =  os.path.join(DATA_DIR, "papers.csv")

# load up the papers into a format

previous_papers = []
with open(PAPERS_CSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = csvreader.next()
    for row in csvreader:
        paper = dict(zip(header, to_utf8(row)))
        if not paper['dateread']:
            paper['dateread'] = '-'
        previous_papers.append(paper)

def main():
  with open(BASE_TEMPLATE_FILE, 'r') as inf:
    base_template = inf.read()
  template = Template(base_template)
  with open(RESOURCES_FNAME, 'r') as inf:
    resources = json.load(inf)['resources']
  print(template.render(resources=resources, previous_papers=previous_papers))

if __name__ == '__main__':
  print('Content-type: text/html; charset=utf-8\n')
  main()
