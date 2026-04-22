import pandas as pd
import matplotlib.pyplot as plt

# Данные
data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "consumption": [120, 130, 125, 140, 150, 170, 160]
}

df = pd.DataFrame(data)

# График
plt.plot(df["day"], df["consumption"], marker='o')
plt.title("Electricity Consumption by Day")
plt.xlabel("Day")
plt.ylabel("Consumption")

for i, value in enumerate(df["consumption"]):
    plt.text(i, value, str(value))

plt.show()

print("Max consumption:", df["consumption"].max())
print("Min consumption:", df["consumption"].min())
print("Average consumption:", df["consumption"].mean())