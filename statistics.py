import pandas
import random
import matplotlib
import numpy
import matplotlib.pyplot as plt
from scipy import stats
rgen = random.Random()

experiments = []
for e in range(2000):
    v = 0.0
    for r in range(25):
        t = rgen.randint(1,10)
        if t < 6:
            v += 0.5
        elif t < 8:
            v += 1
        
    experiments.append(v)

plt.plot(list(range(2000)), experiments)
plt.title('Experimantal data')
plt.show()


df = pandas.DataFrame(data={
    'experiments': experiments
})
df.to_csv("experiments.csv")


df1 = pandas.read_csv("experiments.csv")
df = pandas.DataFrame(data={
	'df1': df1['experiments'],
	}
)

df.plot.kde()

print(stats.kstest(df['df1'], 'norm', (df['df1'].mean(), df['df1'].std())))

