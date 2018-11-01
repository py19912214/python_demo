import psutil
# 2说明是双核超线程, 4则是4核非超线程
# CPU逻辑数量
print(psutil.cpu_count())
# CPU物理核心
print(psutil.cpu_count(logical=False))
# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 磁盘分区信息
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage('/'))
 # 磁盘IO
print(psutil.disk_io_counters())
print()
