def get_recent_files():
   with open("./metadata.txt") as file:
      ...
def main():
   response = input("Open a new file? [y/n] ")
   if response == "y":
      response = input("File Location? [y/n] ")
   elif response == "n":
      print("recently opened files:")
if __name__ == "__main__":
   main()