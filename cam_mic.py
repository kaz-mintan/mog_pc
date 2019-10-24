import time
import threading

from rec import MakeWavFile
from simple_cap import capture
from call_ard import get_hearts

thread_1 = threading.Thread(target=MakeWavFile)
thread_2 = threading.Thread(target=capture)
thread_3 = threading.Thread(target=get_hearts)

thread_2.start()
thread_1.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
