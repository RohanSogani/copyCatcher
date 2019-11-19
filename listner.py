import time
import threading
import sys
import pyperclip
from datetime import datetime

def isUrl(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    return False

def printOut(clipboard_content):
    print("Found a url", str(clipboard_content))
    print("Opening File")
    file = open("catcher.txt", "a+")
    todayDateAndTime = datetime.now();
    file.write(str(clipboard_content) + " |%$$%| " + str(todayDateAndTime) + "\n")
    file.close()

class copyURLCatcher(threading.Thread):
    def __init__(self, predicate, callback, pause=5.):
        super(copyURLCatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):
        currentCopyVal = ""
        while not self._stopping:
            temporaryCopyVal = pyperclip.paste()
            if temporaryCopyVal != currentCopyVal:
                currentCopyVal = temporaryCopyVal
                if self._predicate(currentCopyVal):
                    self._callback(currentCopyVal)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True

def main():
    catcher = copyURLCatcher(isUrl, printOut, 5.)
    catcher.start()
    while True:
        try:
            print("Waiting for clipboard to be changed...")
            time.sleep(10)
        except KeyboardInterrupt:
            catcher.stop()
            break


if __name__ == "__main__":
    main()
