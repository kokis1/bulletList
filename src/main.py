import os

class task:
   def __init__(self, description, duedate, tag) -> None:
      self.description = description
      self.duedate = duedate
      self.tag = tag



def get_recent_files(path):
   '''return a list of the recently opened bulletList save files, using the metadata file'''
   with open(path, mode="r") as file:
      recent_files = []
      file_line = False # toggles on and then off when the files are there or not
      for line in file.readlines():
         line = line.strip("\n")
         if line == "end of files":
            file_line = False
         if file_line:
            recent_files.append(line)
         if line == "files":
            file_line = True
   return recent_files

def write_new_file(path: str) -> None:
   '''opens a new file at the given path and writes a header'''
   with open(path, mode="w") as file:
      file.write("bulletList File")

def valid_path(path: str) -> bool:
   '''return whether a path is valid or not and that it is a file and not a directory'''
   return os.path.exists(path) and os.path.isfile(path)

def update_metadata(path: str, active_file: str) -> None:
   recent_files = get_recent_files(path)
   if active_file in recent_files:
      return
   recent_files.insert(0, active_file)
   if len(recent_files) > 4:
      recent_files = recent_files[:4] # makes sure there are at most 4 recent files
   
   # makes sure each line has a newline character
   lines_to_write = ["files"] + recent_files + ["end of files"]
   lines_to_write = [line + "\n" for line in lines_to_write]
   with open(path, mode="w") as file:
      file.writelines(lines_to_write)
   
   

def open_file(metadata_path: str) -> str:
   active_file = ""
   while not valid_path(active_file):
      print("Valid file not selected yet:")
      response = input("Open a new file? [y/n/q] ")
      if response == "y":
         print("File location:")
         response = input("> ")
         write_new_file(response)
      elif response == "n":
         print("recently opened files:")
         recent_files = get_recent_files(metadata_path)
         for file in recent_files:
            print(file)
         response = input("File location: ")
      elif response == "q":
         exit()
      active_file = response
   print(" ")
   print("     Valid: Opening file")
   print(46 * ".")
   print(46 * ".")
   print(" ")
   print(" ")
   return active_file

def pad_string(string: str, length: int) -> str:
   '''ensures a string is the right length, pads to the right if too short
   truncates from the right if too long'''
   if len(string) >= length:
      return string[:length]
   pad_length = length - len(string)
   return string + pad_length*" "

def print_tasks(tasks: list[task], flag: list[str] = []) -> None:
   '''prints a list of all the tags, padded to keep everything in line
      flags:
         urgent: lists in descending order of soonest due date
         tag: lists all the tasks by tag'''
   print(20*" ", "Tasks")
   print(46*".")
   print("Index   |  Description   |  Due Date |  Tag")
   for i in range(len(tasks)):
      index = pad_string(str(i+1), 5)
      description = pad_string(tasks[i].description, 11)
      duedate = pad_string(tasks[i].duedate, 8)
      print(index, "   |   ", description, "  |  ", duedate, " |  ", tasks[i].tag, sep="")

def parse_input() -> list[str]:
   response = input("> ").split(" ")
   return response

def get_new_tasks(tasks: list[task], response: list[str]) -> list[task]:
   # inserts the new task into the front of the task queue 
   
   # checks that the keyword is indeed new, removes from the front of the list
   if response.pop(0) != "new":
      return tasks
   new_response = " ".join(response).split("|")
   if len(new_response) > 3:
      print("Unable to parse input: too many arguments. 3 needed")
   elif len(new_response) < 3:
      print("Unable to parse input: not enough arguments. 3 needed")
   new_task = task(new_response[0], new_response[1], new_response[2])
   tasks.insert(0, new_task)
   return tasks
   

def command_line_loop(tasks: list[task]) -> list[task]:
   current_tasks = tasks
   print_tasks(current_tasks)
   while True:
      response = parse_input()
      match response[0]:
         case "q":
            break
         case "h":
            ...
         case "list":
            print_tasks(current_tasks, response)
         case "new":
            current_tasks = get_new_tasks(tasks, response)
            print_tasks(current_tasks)
         case "complete":
            ...
         case "save":
            ...
   
   return current_tasks

def parse_tasks(lines: list[str]) -> list[task]:
   tasks = []
   for line in lines:
      # splits each line into words and removes spaces after the end
      line = line.split("|")
      line = [word.strip() for word in line]
      if line[0] != "task":
         continue
      descr = line[1]
      duedate = line[2]
      tag = line[3]
      tasks.append(task(descr, duedate, tag))
   return tasks

def read_tasks(active_file: str) -> list[task]:
   with open(active_file, mode="r") as file:
      lines = file.readlines()
      lines = [line.strip("\n") for line in lines]
   if lines[0] != "bulletList File":
      print("File is corrupted, unreadable")
      exit()
   tasks = parse_tasks(lines[0:])
   return tasks

def main():
   metadata_path = "./metadata.txt"
   if not valid_path(metadata_path):
      print("No metadata found, can't run!")
      exit()
   active_file = open_file(metadata_path)
   tasks = read_tasks(active_file)
   tasks = command_line_loop(tasks)
   update_metadata(metadata_path, active_file)
   print("Exiting. Thank you for using bulletList!")
   exit()
if __name__ == "__main__":
   main()