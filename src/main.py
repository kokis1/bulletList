from blessings import Terminal

class task:
   def __init__(self, description: str, duedate: str, tag: str) -> None:
      self.description = description
      self.duedate = duedate
      self.tag = tag


def main(term: Terminal) -> None:
   # sets the terminal to full screen
   with term.fullscreen():
   # sets the cursor at the top left of the screen
      term.location(0, 0)
   # prints the menu
   print(term.move_x(8) + "Menu")
   print("Tasks" + term.move_right + "DueDate" + term.move_right + "Tag")
   # asks if the user wants to load or create a new set of tasks
   # loads the tasks if so

if __name__ == "__main__":
   term = Terminal()
   main(term)