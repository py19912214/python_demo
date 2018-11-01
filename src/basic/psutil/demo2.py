import psutil

psutil.pids()
# 所有进程ID
#[3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
p =psutil.Process(8965)
# 获取指定进程ID=3776，其实就是当前Python交互环境
print(p.name())
# 进程名称
#'python3.6'
print(p.exe()) # 进程exe路径
#'/Users/michael/anaconda3/bin/python3.6'
print(p.cwd()) # 进程工作目录
#'/Users/michael'
print(p.cmdline()) # 进程启动的命令行
#['python3']
print(p.ppid()) # 父进程ID
#3765
print(p.parent()) # 父进程
#<psutil.Process(pid=3765, name='bash') at 4503144040>
print(p.children()) # 子进程列表
#[]
print(p.status()) # 进程状态
#'running'
print(p.username()) # 进程用户名
#'michael'
print(p.create_time()) # 进程创建时间
#1511052731.120333
print(p.terminal()) # 进程终端
#'/dev/ttys002'
print(p.cpu_times()) # 进程使用的CPU时间
#pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
print(p.memory_info()) # 进程使用的内存
#pmem(rss=8310784, vms=2481725440,pfaults=3207,pageins=18)
print(p.open_files()) # 进程打开的文件
#[]
print(p.connections()) # 进程相关网络连接
#[]
print(p.num_threads()) # 进程的线程数量
#1
print(p.threads()) # 所有线程信息
#[pthread(id=1, user_time=0.090318, system_time=0.062736)]
print(p.environ()) # 进程环境变量
#{'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
print(p.terminate()) # 结束进程
#Terminated: 15 <-- 自己把自己结束了