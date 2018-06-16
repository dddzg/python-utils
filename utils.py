from contextlib import contextmanager
import time
@contextmanager
def timer(name):
  """
  Taken from Konstantin Lopuhin https://www.kaggle.com/lopuhin
  in script named : Mercari Golf: 0.3875 CV in 75 LOC, 1900 s
  https://www.kaggle.com/lopuhin/mercari-golf-0-3875-cv-in-75-loc-1900-s
  """
  t0 = time.time()
  yield
  print(f'[{name}] done in {time.time() - t0:.0f} s')

from functools import reduce
def compose(*funcs):
    """Compose arbitrarily many functions, evaluated left to right.

    Reference: https://mathieularose.com/function-composition-in-python/
    """
    # return lambda x: reduce(lambda v, f: f(v), funcs, x)
    if funcs:
        return reduce(lambda f, g: lambda *a, **kw: g(f(*a, **kw)), funcs)
    else:
        raise ValueError('Composition of empty sequence not supported.')
