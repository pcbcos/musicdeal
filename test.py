import subprocess
import time
p = subprocess.Popen("netease-dl -a playlist -i 4885484129",stdin = subprocess.PIPE,shell =True)
p.stdin.write(b"18658255803\n")
time.sleep(2)
p.stdin.write(b"3210266696\n")

