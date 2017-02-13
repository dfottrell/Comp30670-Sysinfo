'''
Created on 6 Feb 2017

@author: David Fottrell
'''
import platform

def main():
    print(platform.platform())
    print("The name of this machine is: ", platform.machine())
    print("The processor is: ", platform.processor())
    print("The operating system is: ", platform.system())
    print("The version of this system is: ", platform.release())
    print("The version of this operating system is: ", platform.version())
    print("The user name of this system is: ", platform.uname())
    return


if __name__ == '__main__':
    main()