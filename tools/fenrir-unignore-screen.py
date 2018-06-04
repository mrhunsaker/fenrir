#!/usr/bin/env python3
import os, argparse

def removeScreenFromIgnoreList(ignoreFileName = '/tmp/fenrirSuspend', screen = '1', useCurrentScreen = True):
    if useCurrentScreen:
        tty = open('/sys/devices/virtual/tty/tty0/active','r')
        screen = str(tty.read()[3:-1])
    if not screen:
        print('No screen given.')        
    ignoreScreens = []
    ignoreScreensStr = ''
    if ignoreFileName != '':
        if os.access(ignoreFileName, os.R_OK):
            with open(ignoreFileName, 'r') as fp:
                try:
                    ignoreScreens = fp.read().split(',')#.replace('\n','').split(',')
                except Exception as e:
                   print(e)

        if screen in ignoreScreens:
            ignoreScreens.remove(screen)
        ignoreScreensStr = ','.join(ignoreScreens)
           
        with open(ignoreFileName, 'w') as fp:
            fp.write(ignoreScreensStr)
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Unignore screens in fenrir to make it active again. If no screen is given use current screen.')
    parser.add_argument('-s', '--screen', metavar='SCREEN', default=None, help='Ignore a given screen. Use current screen as default.')
    parser.add_argument('-f', '--file', metavar='File', default='/tmp/fenrirSuspend', help='Specify the suspendingScreenFile')            
    try:
        args = parser.parse_args()
        ignoreFileName = args.file
        useCurrentScreen = False
        screen = None
        print(args.file)
        if args.screen:
            screen = args.screen
        else:
            useCurrentScreen = True     
        removeScreenFromIgnoreList(ignoreFileName, screen, useCurrentScreen)        
    except Exception as e:
        parser.print_help()      