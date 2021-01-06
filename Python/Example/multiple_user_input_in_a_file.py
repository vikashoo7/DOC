######## This will work in Python 3.x ########

def serverList():
        print ("\033[1;33;40mEnter the list of the Server \033[00m")
        print ('-----------------------------')
        f=open('/location/to/the/file', "w")
        while True:
                l=input()
                f.write(l)
                f.flush()
                if l == "":
                        break
                f.write("\n")
        f.close()
        
serverList()
