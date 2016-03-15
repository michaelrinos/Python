#!/usr/bin/python3
import sys
import sh

def main():
    if len(sys.argv) == 2:
        sh.cd(sys.argv[1])
        print(sh.git("status"))
        print("(Y/n): Are you sure you want to reset this directory?")
        temp = str(input("Local changes will be deleted: "))
        if temp=="y" or temp =="Y":
            print(sh.git.reset("--hard", "HEAD"))
            print(sh.git.clean("-f"))
            print(sh.git.pull)
            print(sh.git("status"))
        else:
            sys.exit(0)

    else:
        print(sh.git("status"))
        print("(Y/n): Are you sure you want to reset this directory?")
        temp = str(input("Local changes will be deleted: "))
        if temp=="y" or temp =="Y":
            print(sh.git.reset("--hard", "HEAD"))
            print(sh.git.clean("-f"))
            print(sh.git.pull)
            print(sh.git("status"))
        else:
            sys.exit(0)

if __name__ == '__main__':
    main()