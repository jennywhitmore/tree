import os

i = chr(9474)
t = chr(9500) + chr(9472)
l = chr(9492)+ chr(9472)
nfiles = 0
ndirectories = 0

def print_directory(path, indentation_level = 0):

    up = indentation_level +1
    end = l * indentation_level
    tab = ""
    nfiles = 0
    ndirectories = 0
    
    
    for i_level in range(0,indentation_level):
        tab = tab + i + " " * (indentation_level+1)

    directory = os.scandir(path)
    directory_sorted = sorted(directory,key=lambda f: f.name.lower())

    try:
        *_, last=directory_sorted

        for each in directory_sorted:

            #intendation=0: 
            if each != last and each.is_file() and indentation_level == 0:
                print(t, each.name)
                nfiles += 1
                
            elif each == last and each.is_file() and indentation_level == 0:
                 print(l,  each.name)
                 nfiles += 1
            
            elif each != last and each.is_dir() and indentation_level == 0:
                print(t, each.name)
                f, d = print_directory(each.path, up, )
                nfiles += f
                ndirectories += 1
            
            elif each == last and each.is_dir()and indentation_level == 0:
                print(l, each.name)
                f, d = print_directory(each.path, up, )
                nfiles += f
                ndirectories += 1
                
            #intendation>0:
            elif each != last and each.is_file() and indentation_level > 0:
                print(tab, t, each.name)
                nfiles += 1
     
            elif each == last and each.is_file() and indentation_level > 0:
                 print(tab,  l, each.name)
                 nfiles += 1
            
            elif each != last and each.is_dir() and indentation_level > 0:
                print(tab,  t, each.name)
                f,d = print_directory(each.path, up,)
                nfiles += f
                ndirectories += 1
            
            elif each == last and each.is_dir() and indentation_level > 0:
                print(tab,l, each.name)
                f, d = print_directory(each.path, up, )
                nfiles += f
                ndirectories += 1
               
            else:
                print("Unknown type.")
                           
    except:
        pass

    return nfiles,ndirectories

if __name__ == "__main__":
    nfiles,ndirectories = print_directory(".")
    print ("Files:", nfiles, "Directories:", ndirectories)




           
  
