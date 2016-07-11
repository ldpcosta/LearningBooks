

File = open('C:\\Users\\Luis\\hello.txt', "w")
def madLibs(File,adjective,noun1,verb,noun2):
    string = "The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events." %(adjective, noun1, verb, noun2)
    File.write(string)
    File.close()

    
