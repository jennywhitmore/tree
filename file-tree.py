import os

t = chr(9500) + chr(9472)
l = chr(9492)+ chr(9472)

def print_directory(path):
    
    directory = os.scandir(path)
    directory_sorted = sorted(directory,key=lambda f: f.name.lower())
    *_, last=directory_sorted

    for each in directory_sorted:
        if each != last:
            print (t, each.name)
        else:
            print(l, each.name)
    
if __name__ == "__main__":
    print_directory(".")

    




           
  
