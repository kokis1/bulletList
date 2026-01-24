import os

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
      print("No valid file found yet")
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
         break
      active_file = response
   return active_file

def main():
   metadata_path = "./metadata.txt"
   if not valid_path(metadata_path):
      print("No metada found, can't run!")
      exit()
   active_file = open_file(metadata_path)
   update_metadata(metadata_path, active_file)
   print("Exiting. Thank you for using bulletList!")
   exit()
if __name__ == "__main__":
   main()