The “tree”1 tool is a simplified project of the tree command such as shown on Wikipedia
https://en.wikipedia.org/wiki/Tree_(command)

It displays the contents of the current directory in a tree-like structure (or root-structure) with various indentation levels.
If tree encounters a subdirectory, the indentation level of the filenames in that directory move. This continues recursively for sub-subdirectories etc.
The print_directory(path) function is implemented and uses
os.scandir to iterate over the files in the passed directory and outputs the file names in a tree-structure.
It sorts the file and directory names by using the lambda f function f.name.lower().
It also counts files and directories and gives out that number.

This is a project done as final coding exam for Wilhelm Buechner University of applied science.
