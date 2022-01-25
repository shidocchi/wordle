import re

__version__ = '0.1.1'

class Wordle:

  LENGTH = 5 
  HIT = 'H'
  BLOW = 'B'
  UNUSED = '-'

  chars = re.escape(f'{HIT}{BLOW}{UNUSED}')
  rx_chars = re.compile(f'[{chars}]+')

  def __init__(self):
    self.clear()

  def clear(self):
    self.hbs = []

  def pop(self):
    self.hbs.pop()

  def ishitblow(self, hitblow):
    return self.rx_chars.fullmatch(hitblow)

  def hitblow(self, word, guess):
    w = list(word)
    g = list(guess)
    for i,ch in enumerate(g):
      if w[i] == ch:
        g[i] = self.HIT
        w[i] = None
    for i,ch in enumerate(g):
      if ch != self.HIT:
        if ch in w:
          g[i] = self.BLOW
          w[w.index(ch)] = None
        else:
          g[i] = self.UNUSED
    return ''.join(g)

  def __len__(self):
    return len(self.hbs)

  def __setitem__(self, guess, hitblow):
    self.hbs.append((guess, hitblow))

  def items(self):
    return self.hbs

  def solve(self, words):
    for word in words:
      if all(self.hitblow(word, guess) == hitblow
             for guess,hitblow in self.items()):
        yield word.rstrip()

if __name__ == '__main__':
  w = Wordle()
  words = open('wordles.txt', 'r')

  while True:

    i = len(w) + 1
    guess = input(f'\n  guess({i}): ').strip()
    if not guess or len(guess) != w.LENGTH:
      ans = input('[p]op / [c]lear / e[x]it? ').strip()
      if ans == 'x':
        break
      elif ans == 'c':
        w.clear()
      elif i > 1 and ans == 'p':
        w.pop()
      continue

    hitblow = input(f'hitblow({i}): ').strip()
    if not hitblow or len(hitblow) != w.LENGTH or not w.ishitblow(hitblow):
      continue

    w[guess] = hitblow
    words.seek(0)
    possib = list(w.solve(words))
    if len(possib) == 0:
      print('no possib')
      w.pop()
      continue
    print(f' possib({i}):', ' '.join(possib))
