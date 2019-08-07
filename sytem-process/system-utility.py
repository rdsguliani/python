// pip install psutil

import psutil;

print(psutil.cpu_times(percpu=False));


for x in range(3):
    print(psutil.cpu_percent(interval=1));

virtual_memory = psutil.virtual_memory();

print(virtual_memory);

converter_to_Gb = 1024 *  1024 * 1024;

print ('total : {} {}'.format((virtual_memory.total)/(converter_to_Gb), 'Gb'));
print ('available : {} {}'.format((virtual_memory.available)/(converter_to_Gb), 'Gb'));

print ('used : {} {}'.format((virtual_memory.used)/(converter_to_Gb), 'Gb'));
print ('free : {} {}'.format((virtual_memory.free)/(converter_to_Gb), 'Gb'));

print(psutil.virtual_memory())

# print(' DISK DETAILS ::')
#
# print(psutil.disk_partitions(all=False));

# print(psutil.pids());
print('SYTEM PROCESSES ::')
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
    except psutil.NoSuchProcess:
        pass
    else:
     print(pinfo)
