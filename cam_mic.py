import time
import threading

from rec import MakeWavFile
from simple_cap import capture

thread_1 = threading.Thread(target=MakeWavFile)
thread_2 = threading.Thread(target=capture)


thread_1.start()
thread_2.start()

thread_1.join()
