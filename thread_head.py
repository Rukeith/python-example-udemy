# -*- coding: utf-8 -*-
import threading

def do_this(what):
  whoami(what)

def whoami(what):
  print('執行緒%s跑%s' % (threading.Thread(), what))

if __name__ == '__main__':
  whoami('主程式:')
  for n in range(3):
    p = threading.Thread(target=do_this, args=('函數%s' % n,))
    p.start()
    p.join()