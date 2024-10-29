import random
import matplotlib.pyplot as plt
import pandas as pd

# simulation for dice rolls using the Monte Carlo method
def monte_calro_simulation(num_rolls):
    sums_frequency = {i:0 for i in range(2,13)}

    # # Dice roll simulation
    for _ in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total_sum = die1 + die2
        sums_frequency[total_sum] += 1

   # Probability calculation
    probabilities = {key: (value / num_rolls) * 100 for key, value in sums_frequency.items()}
    return probabilities, sums_frequency

# number of simulations
num_rolls = 10000
probabilities, sum_frequency =  monte_calro_simulation(num_rolls)

# Convert results to a DataFrame for easy presentation
results_df = pd.DataFrame(list(probabilities.items()), columns=["Sum", "Probability (%)"])
print(results_df)

# # Probability graph
plt.figure(figsize=(10,6))
plt.bar(results_df["Sum"], results_df["Probability (%)"], color="skyblue")
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability (%)")
plt.title(f"Probability of Sums (Monte Carlo Simulation, {num_rolls} Rolls)")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Analytical probabilities to compare
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Comparison of results
comparison_df = pd.DataFrame({
    "Sum": list(analytical_probabilities.keys()),
    "Analytical Probability (%)": list(analytical_probabilities.values()),
    "Monte Carlo Probability (%)": [probabilities[sum_val] for sum_val in analytical_probabilities.keys()]
})


print(comparison_df)

# Graph comparing analytical and Monte Carlo probabilities
plt.figure(figsize=(10, 6))
plt.plot(comparison_df["Sum"], comparison_df["Analytical Probability (%)"], marker='o', label="Analytical Probability", color='blue')
plt.plot(comparison_df["Sum"], comparison_df["Monte Carlo Probability (%)"], marker='x', label="Monte Carlo Probability", color='red')
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability (%)")
plt.title("Comparison of Analytical and Monte Carlo Probabilities")
plt.xticks(range(2, 13))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()