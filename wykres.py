
import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(50)
b = np.random.rand(50)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(0, 10, 100)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sin")
axs[0, 0].grid(True)
axs[0, 0].annotate("opis", xy=(2, 1), xytext=(3, 1), arrowprops={"facecolor":"black", "shrink": 0.05})

axs[0, 1].scatter(a, b)
axs[0, 1].set_title("Random")

axs[1, 0].bar(["a", "b", "c"], [10, 20, 5])
axs[1, 0].set_title("...")

dane = np.random.randn(1000)
axs[1, 1].hist(dane, bins=30)
axs[1, 1].set_title("histogram")
plt.show()