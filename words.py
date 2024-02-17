def print_upper_words(words):
  """print out each word on a separate line, uppercased.
  
  ex) print_upper_case(["step", "two", "starting", "on", "your", "own"])
      STEP
      TWO
      STARTING
      ON
      YOUR
      OWN
  """
  for word in words:
    print(word.upper())


def print_upper_words_start_with_e(words):
  """print out words that start with letter 'e' or 'E', uppercased, on a separate line.

  ex) print_upper_words_start_with_e(["etep", "two", "Etarting", "on", "eour", "own"])
      ETEP
      TARTING
      EOUR
  """
  for word in words:
    if word.startswith("e") or word.startswith("E"):
      print(word.upper())


def print_upper_words2(words, must_start_with):
  """print out words that start with letter which is given, uppercased, on a separate line.

  ex) print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
      HELLO
      HEY
      YO
      YES
  """
  for word in words:
    for letter in must_start_with:
      if word.startswith(letter):
        print(word.upper())
        break