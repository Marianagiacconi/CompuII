from celery import Celery
import numpy as np

appCele = Celery('task', broker='redis://localhost', backend='redis://localhost:6379')

@appCele.task
def log(N):
    print('log')
    res = np.log(N) 
    return str(res)

