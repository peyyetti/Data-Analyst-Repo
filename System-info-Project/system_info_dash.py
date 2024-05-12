import psutil
import time
import psycopg2

hostname = 'localhost'
database = 'System_Information'
username = 'postgres'
pwd = 'password123'
port_id = '5432'

conn = psycopg2.connect(host = hostname,
                        dbname = database,
                        user = username,
                        password = pwd,
                        port = port_id)

cur = conn.cursor()

while 1:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_recieved = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]
    
    cur.execute('INSERT INTO system_info VALUES (NOW()::TIMESTAMP,'+ str(cpu_usage) + ','
                + str(memory_usage) + ','
                + str(cpu_interrupts) + ','
                + str(cpu_calls) + ','
                + str(memory_used) + ','
                + str(memory_free) + ','
                + str(bytes_sent) + ','
                + str(bytes_recieved) + ','
                + str(disk_usage) + ')'
                )
    
    conn.commit()
    print(memory_usage)
    time.sleep(1)

