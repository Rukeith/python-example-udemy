# -*- coding: utf-8 -*-
import thread

a_lock = thread.allocate_lock()

with a_lock:
  print('a_lock is locked while this executes')