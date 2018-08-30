# -*- coding: utf-8 -*-

import multiprocessing, time, os

def whoami(name):
  print(' %s, 行程 %s' % (name, os.getpid()))

def loopy(name):
  whoami(name)
  start = 1
  stop = 880000
  for num in range(start, stop):
    print('\tNumber %s of %s. 執行!' % (num, stop))
    time.sleep(1)

if __name__ == '__main__':
  whoami('main')
  p = multiprocessing.Process(target=loopy, args=('loopy',))
  p.start()
  time.sleep(5)
  p.terminate()