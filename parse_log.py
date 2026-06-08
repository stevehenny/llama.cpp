import re
import sys

log = open(sys.argv[1]).read()

def find(pattern):
    m = re.search(pattern, log)
    return m.group(1) if m else "NA"

# tokens/sec (from "speed: X t/s")
tps = find(r"speed:\s*([0-9.]+)")

# n_predict / n_accept / n_drafted
n_predict = find(r"n_predict\s*=\s*([0-9]+)")
n_accept  = find(r"n_accept\s*=\s*([0-9]+)")
n_drafted = find(r"n_drafted\s*=\s*([0-9]+)")

# accept rate (fallback compute if missing)
accept_rate = find(r"accept\s*=\s*([0-9.]+)%")

# total time
total_time = find(r"total time\s*=\s*([0-9.]+)")

print(tps, accept_rate, n_predict, n_accept, n_drafted, total_time)
