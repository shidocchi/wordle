class Wordle:

  LENGTH = 5 
  HIT = 'H'
  BLOW = 'B'
  UNUSED = '-'

  def __init__(self):
    self.clear()

  def clear(self):
    self.hbs = []

  def pop(self):
    self.hbs.pop()

  def ishitblow(self, hitblow):
    return not hitblow.strip(self.HIT + self.BLOW + self.UNUSED)

  def _hitblow(self, word, guess):
    start = {}
    for i,ch in enumerate(guess):
      x = word.find(ch, start.get(ch,-1)+1)
      start[ch] = x
      if x == -1:
        yield self.UNUSED
      elif x == i:
        yield self.HIT
      else:
        yield self.BLOW

  def hitblow(self, word, guess):
    return ''.join(self._hitblow(word, guess))

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
