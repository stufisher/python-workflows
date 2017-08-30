from __future__ import absolute_import, division

import workflows.transport

def test_known_transports_is_a_dictionary():
  '''Check transport register build in CommonTransport.'''
  assert isinstance(workflows.transport.get_known_transports(), dict)

def test_load_any_transport():
  '''Look up fallback transport mechanism.'''
  assert workflows.transport.lookup(None)