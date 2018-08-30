#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing as mp

def washer(dishes, output):
  for dish in dishes:
    print('洗', dish)
    output.put(dish)

def dryer(input):
  while True:
    dish = input.get()
    print('擦乾', dish)
    input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dishes = ['大碗', '小碗', '鍋子', '筷子', '湯匙']
washer(dishes, dish_queue)
dryer_proc.start()
dish_queue.join()