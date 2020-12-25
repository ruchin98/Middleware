from .tasks import longtime_add
import time
import os
from os.path import dirname,abspath
import numpy as np
import time
from timeit import default_timer as timer
#if __name__ == '__main__':
file_path = dirname(dirname(abspath(__file__)))
# print(file_path)
upload_folder = file_path+"/celery_test/Uploads"
output_folder = file_path+"/celery_test/Outputs"
f = os.listdir(upload_folder)[0]
fh = open(file_path+"/celery_test/Uploads/"+f)
num_lines = sum(1 for line in fh)
res_out = np.zeros((num_lines,),dtype=bool)
os.unlink(output_folder+"/"+os.listdir(output_folder)[0])
start = time.clock()
start1 = time.time()
start2 = timer()
for f in os.listdir(upload_folder):
    c = 0
    fh = open(upload_folder+"/"+f)
    f_out = open(output_folder+"/"+"out.txt","a+")
    reesult = []
    for line in fh:
        a,b = line.split(" ")
        result = longtime_add.delay(int(a),int(b))
        # print(result.task_id)
        # # at this time, our task is not finished, so it will return False
        # print('Task finished? ', result.ready())
        # print('Task result: ', result.result)   
        # # sleep 10 seconds to ensure the task has been finished
        # time.sleep(10)
        # # now the task should be finished and ready method will return True
        # print('Task finished? ', result.ready())
        # print('Task result: ', result.result)
        ressult.append(result)
        outt = [t.get() for t in result]

        
        f_out.write(str(result.result)+"\n")
        if result.ready()==True:
            res_out[c] = True
        c = c+1
            
    fh.close()
    f_out.close()
res_out = np.zeros((num_lines,),dtype=bool)
print(len(outt))
print(outt)
elapsed = (time.clock() - start)
elapsed1 = (time.time()- start1)
elapsed2 = timer()- start2
print(elapsed)
print(elapsed1)
print(elapsed2)