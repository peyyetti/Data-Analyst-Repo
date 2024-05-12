CREATE TABLE system_info(
	time_col TIMESTAMP,
	cpu_usage NUMERIC(5,2),
	memory_usage NUMERIC(5,2),
	cpu_interrupts NUMERIC(18, 0),
	cpu_calls NUMERIC(18, 0),
	memory_used NUMERIC(18, 0),
	memory_free NUMERIC(18, 0),
	bytes_sent NUMERIC(18, 0),
	bytes_recieved NUMERIC(18, 0),
	disk_usage NUMERIC(5, 2)
);

select * FROM system_info;