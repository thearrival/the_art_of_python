import platform

print("~"*30, "System Information", "~"*40)
uname = platform.uname()

print(f"System:  {uname.system}")
print(f"Release: {uname.release}")
print(f"Node: {uname.node}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
