import ctypes
import sys
if sys.platform.startswith('linux'):
    try:
        print('Starting')
        x11 = ctypes.cdll.LoadLibrary('libX11.so')
        print('Library loaded!')
        x11.XInitThreads()
    except:
        print("Warning: failed to XInitThreads()")
        print ("Unexpected error:", sys.exc_info ())
        
