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

def main():
   response = input("Open a new file? [y/n] ")
   if response == "y":
      response = input("File Location? [y/n] ")
   elif response == "n":
      print("recently opened files:")
      recent_files = get_recent_files("./metadata.txt")
      for file in recent_files:
         print(file)
if __name__ == "__main__":
   main()