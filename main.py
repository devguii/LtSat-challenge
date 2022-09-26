import matplotlib.pyplot as plt
import pandas as pd

# make data
data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

primeira_coluna = df["AlturaSatelite"]
segunda_coluna = df["AlturaContainer"]

# plot graph
fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

axs[0].plot(primeira_coluna)
axs[1].plot(segunda_coluna)
axs[2].plot(primeira_coluna)
axs[2].plot(segunda_coluna)

axs[0].title.set_text('Altura Satélite')
axs[1].title.set_text('Altura Container')
axs[2].title.set_text('Altura Satélite X Container')

fig.suptitle('Gráficos Altura Satélite e Container', y=1.0)

plt.show()