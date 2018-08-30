from multiprocessing import Pool

def f(x):
  return x*x

if __name__ == '__main__':
  p = Pool(5) # 平行運算物件
  print(p.map(f, [1, 2, 3]))