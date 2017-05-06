import os

import win32file
import win32event
import win32con
import tempcreate as tc

path_to_watch = os.path.abspath (".")


change_handle = win32file.FindFirstChangeNotification (
  path_to_watch,
  0,
  win32con.FILE_NOTIFY_CHANGE_FILE_NAME
)


noscan=["t.csv","tb.csv","dump.txt"]
try:

  old_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch)])
  while 1:
    result = win32event.WaitForSingleObject (change_handle, 500)

  
    if result == win32con.WAIT_OBJECT_0:
      
      new_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch)])
      added = [f for f in new_path_contents if not f in old_path_contents]
      #deleted = [f for f in old_path_contents if not f in new_path_contents]
      if added[0] not in noscan:
          print ("Added",added)
          tc.tempcreate()
 #         join (added)
      '''if deleted:
          print ("Deleted: ")
  #        join (deleted)'''

      old_path_contents = new_path_contents
      win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)
