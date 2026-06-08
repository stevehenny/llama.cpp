import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spec_benchmark.csv")

# average over runs
g = df.groupby("ctx").mean(numeric_only=True)

plt.figure()
plt.plot(g.index, g["tokens_per_sec"], marker="o")
plt.xscale("log", base=2)
plt.xlabel("Context length")
plt.ylabel("Tokens/sec (decode)")
plt.title("Speculative decoding scaling vs context length")
plt.show()

plt.figure()
plt.plot(g.index, g["accept_rate"], marker="o")
plt.xscale("log", base=2)
plt.xlabel("Context length")
plt.ylabel("Acceptance rate (%)")
plt.title("Speculative acceptance vs context length")
plt.show()
