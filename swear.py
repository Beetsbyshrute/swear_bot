BAD_WORD_LIST = open('list.txt', 'r').read().split('\n')

def bad_word_count(sentence):
  count = 0
  user_input = sentence.lower().split()

  for word in user_input:
    if word in BAD_WORD_LIST:
      count = count + 1

  return count
