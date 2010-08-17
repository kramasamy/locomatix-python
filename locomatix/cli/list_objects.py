#!/usr/bin/env python

import sys
import httplib
import locomatix

def list_objects():
  """docstring for list_objects"""
  parser = locomatix.ArgsParser()
  parser.add_description("Gets the details of all objects")
  parser.add_arg('feed', 'Name of the feed')
  args = parser.parse_args(sys.argv)
  
  lxsvc = locomatix.Service(args['custid'], \
                           args['key'], \
                           args['secret-key'], \
                           args['host'], \
                           args['port'], \
                           args['use-ssl'])
  
  for batch in lxsvc.list_objects_iterator(args['feed']):
    for obj in batch.objects:
      print obj


if __name__ == '__main__':
  list_objects()