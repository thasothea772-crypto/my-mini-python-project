import matplotlib.pyplot as plt
import seaborn as sns

day = [1, 2, 3, 4, 5, 6, 7]
hours = [1, 2, 3, 8, 10, 12, 14]

sns.set_theme(style="darkgrid")
plt.title("Hour per day", fontsize=14)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Hours", fontsize=12)

plt.plot(day, hours, marker='o', color='blue',
         linestyle='-', linewidth=2)
plt.show()