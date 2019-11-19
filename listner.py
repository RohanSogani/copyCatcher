import time
import threading

import pyperclip

def isUrl(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    return False

def printOut(clipboard_content):
    print("Found a url", str(clipboard_content))
    print("Opening File")
    file = open("listner.txt", "a+")
    file.write(str(clipboard_content) + "\n")
    file.close()

class copyUrlListner(threading.Thread):
    def __init__(self, predicate, callback, pause=5.):
        super(copyUrlListner, self).__init__()
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
    listner = copyUrlListner(isUrl, printOut, 5.)
    listner.start()
    while True:
        try:
            print("Waiting to be changed...")
            time.sleep(10)
        except KeyboardInterrupt:
            listner.stop()
            break


if __name__ == "__main__":
    main()
