
import pandas as pd
import matplotlib.pyplot as plt
from analysis import media_saida_mensal_por_centro as md 
from database import connect_db
data = md
df = pd.DataFrame(
    data,
    columns=[
        'centro',
        'mes',
        'media_saida'
    ]
)

for centro in df['centro'].unique():
    subset = df[df['centro'] == centro]
    plt.plot(subset['mes'], subset['media_saida'], label=centro)

plt.title('Média Mensal de Saída por Centro')
plt.xlabel('Mês')
plt.ylabel('Média de Saída')
plt.legend()
plt.tight_layout()
plt.show()


