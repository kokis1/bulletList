import os

def get_recent_files(path):
   with open(path, mode="r") as file:
      recent_files = []
      file_line = False # toggles on and then off when the files are there or not
      for line in file.readlines():
         line = line.strip("\n")
         if file_line:
            recent_files.append(line)
         if line == "files":
            file_line = True
         if line == "end of files":
            file_line = False
   return recent_files

def valid_path(path: str) -> bool:
   return os.path.exists(path) and os.path.isfile(path)


def open_file(metadata_path: str) -> str:
   active_file = ""
   while not valid_path(active_file):
      response = input("Open a new file? [y/n] ")
      if response == "y":
         print("File location:")
         response = input("> ")
      elif response == "n":
         print("recently opened files:")
         recent_files = get_recent_files(metadata_path)
         for file in recent_files:
            print(file)
         response = input("File location: ")
      active_file = response
   return active_file

def main():
   open_file("./metadata.txt")
if __name__ == "__main__":
   main()