# -*- coding: utf-8 -*-
import logging, threading, time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s',)

def producer(cond):
  logging.debug('Starting producer thread')
  with cond:
    logging.debug('Making resource avaiable')
    cond.notifyAll()

def consumer(cond):
  logging.debug('Starting consumer thread')
  t = threading.current_thread()
  with cond:
    cond.wait()
    logging.debug('Resource is avaiable to consumer')

condition = threading.Condition()
cu1 = threading.Thread(name='consumer_1', target=consumer, args=(condition,))
cu2 = threading.Thread(name='consumer_1', target=consumer, args=(condition,))
pro = threading.Thread(name='Producer', target=producer, args=(condition,))
cu1.start()
time.sleep(2)
cu2.start()
time.sleep(2)
pro.start()