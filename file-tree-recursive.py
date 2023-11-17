import os

i = chr(9474)
t = chr(9500) + chr(9472)
l = chr(9492)+ chr(9472) 


def print_directory(path, indentation_level = 0):

    up = indentation_level + 1
    end = l * indentation_level
    tab = ""
    
    for counter in range(0,indentation_level):
        tab = tab + i + " " * (indentation_level+1)

    directory = os.scandir(path)
    directory_sorted = sorted(directory,key=lambda f: f.name.lower())
    
    try:
        *_, last=directory_sorted

        for each in directory_sorted:

            #intendation=0: 
            if each != last and each.is_file() and indentation_level == 0:
                print(t, each.name)

            elif each == last and each.is_file() and indentation_level == 0:
                 print(l,  each.name)
                
            elif each != last and each.is_dir() and indentation_level == 0:
                print(t, each.name)
                print_directory(each.path, up)
            
            elif each == last and each.is_dir()and indentation_level == 0:
                print(l, each.name)
                print_directory(each.path, up)


                
            #intendation>0:
            elif each != last and each.is_file() and indentation_level > 0:
                print(tab, t, each.name)
                
            elif each == last and each.is_file() and indentation_level > 0:
                 print(tab,  l, each.name)
                
            elif each != last and each.is_dir() and indentation_level > 0:
                print(tab,  t, each.name)
                print_directory(each.path, up)
            
            elif each == last and each.is_dir()and indentation_level > 0:
                print(tab,l, each.name)
                print_directory(each.path, up)
               
            else:
                print("Unknown type.")
                           
    except:
        pass

if __name__ == "__main__":

    print_directory(".")





           
  
