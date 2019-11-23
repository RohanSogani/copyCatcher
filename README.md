# copyCatcher
1. listner.py - Program that runs infinitely to catch URL's that you've copied
  This program must be run in a separate tab so that it keeps on catching the URL's.
  Sleep Time can be changed, current time is 10.
  Before running, make sure you have installed pyperclip.

  If not, use
  ```console
  foo@bar:~$ pip3 install pyperclip
  ```

  To execute
  ```console
  foo@bar:~$python3 listner.py
  ```
  Keeps on catching URL and stores in catcher.txt
2. convertTxtToCsv.py - To convert txt file created by listner to csv for further analysis
