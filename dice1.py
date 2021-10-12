import random
import plotly.figure_factory as ff

counter  = []
dice_results = []

for x in range(0,100):
    dicei = random.randint(1,6)
    diceii = random.randint(1,6)
    dice_results.append(dicei + diceii)
    counter.append(x)

print(counter,dice_results)

curve = ff.create_distplot([dice_results],["Results"])
curve.show()