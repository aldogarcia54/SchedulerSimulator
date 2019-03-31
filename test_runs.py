import subprocess

turn = open("turnarounds.txt", "w")
thr = open("throughputs.txt", "w")
util = open("cpu_utilization.txt", "w")
readQueue = open("ready_que_avg.txt", "w")
python_version = '3'
path_to_run = './main'
py_name = '.py'

for j in range(1,5):
    for i in range(1,31):
        # args = [f"python{python_version}", f"{path_to_run}{py_name}"]  # Avaible in python3
        args = ["python{}".format(python_version), "{}{}".format(path_to_run, py_name), "-s", str(j), "-a",str(i), "-t", ".06"]

        res = subprocess.Popen(args, stdout=subprocess.PIPE)
        output, error_ = res.communicate()
        data = output.decode("utf-8").split("\n")

        if not error_:
            turn.write(data[0]+"\n")
            thr.write(data[1]+"\n")
            util.write(data[2]+"\n")
            readQueue.write(data[3]+"\n")
        else:
            print(error_)

turn.close()
thr.close()
util.close()
readQueue.close()