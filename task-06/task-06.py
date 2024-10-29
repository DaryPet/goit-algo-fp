items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # sort by going down - calories and price
    sorted_items = sorted(items.items(), key= lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost +  details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]

    # inicialization
    dp = [[0 for _ in range(budget + 1)] for _ in range (n + 1)]

    # fill dp
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w =  budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]
    total_calories = dp[n][budget]
    return selected_items, total_calories

# implementing
if __name__ == "__main__":
    budget = 100
    print("Greedy Algorithm:")
    greedy_selection, greedy_calories = greedy_algorithm(items, budget)
    print(f"Selected items: {greedy_selection}")
    print(f"Total calories: {greedy_calories}\n")

    print("Dynamic Programming Algorithm:")
    dp_selection, dp_calories = dynamic_programming(items, budget)
    print(f"Selected items: {dp_selection}")
    print(f"Total calories: {dp_calories}")