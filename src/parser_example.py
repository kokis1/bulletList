KEYWORDS = ["return",
            "if",
            "else",
            "for",
            "while",
            "let",
            "int",
            "str",
            "float"]


class tok:
   def __init__(self, type, value) -> None:
      self.type = type
      self.value = value
   def __repr__(self) -> str:
      return f"TOK({self.type}, {self.value})"

class node:
   def __init__(self, parent, value: tok, children) -> None:
      self.parent = parent
      self.value = value
      self.children = children
   def __repr__(self) -> str:
      return f"{self.value}"
   
   def print_tree(self, indendation = 0):
      representation = indendation * " " + str(self.value)
      indendation += 1
      for child in self.children:
         child.print_tree(indendation+1)
      print(representation)
   
   def add_child(self, child: tok):
      self.children.append(child)

def join(buffer: list) -> str:
   value = ""
   for char in buffer:
      value += char
   return value

def get_number(text: list[str], index: int) -> tuple[float, int]:
   number = []
   while index < len(text) and text[index].isdigit():
      number.append(text[index])
      index += 1
   index -= 1
   return int(join(number)), index

def get_word(text: list[str], index: int) -> tuple[str, int]:
   word = []
   while index < len(text) and text[index].isalnum():
      word.append(text[index])
      index += 1
   index -= 1
   return join(word), index

def tokeniser(text: list[str], keywords: list[str]) -> list[tok]:
   '''separates the stream of text into a stream of tokens'''
   toks = []
   i = 0
   while i < len(text):
      char = text[i]
      if char.isspace():
         i += 1
         continue
      if char.isdigit():
         number, i = get_number(text, i)
         toks.append(tok("NUM", value=number))
      elif char.isalpha():
         word, i = get_word(text, i)
         if word in keywords:
            toks.append(tok(word, 0))
         else:
            toks.append(tok("WORD", word))
      elif char == "(":
         toks.append(tok("LPAREN", 0))
      elif char == ")":
         toks.append(tok("RPAREN", 0))
      elif char == ";":
         toks.append(tok("SCOLON", 0))
      elif char == ".":
         toks.append(tok("DOT", 0))
      elif char == "+":
         toks.append(tok("ADD", 0))
      elif char == "-":
         toks.append(tok("MINUS", 0))
      elif char == "/":
         toks.append(tok("DIV", 0))
      elif char == "*":
         toks.append(tok("TIMES", 0))
      i += 1
   return toks

'''GRAMMAR:
            program: expr*
            expr: expr | ( expr ) | times | add
            times: expr | times | int * times
            add: expr | times | int + add'''

def parse(tokens: list[tok]) -> node:
   root = node(None, tok("ROOT", 0), [])
   return root


def main():
   text = list("1 + 45*50")
   toks = tokeniser(text, KEYWORDS)
   print(toks)

if __name__ == "__main__":
   main()