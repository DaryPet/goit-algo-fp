Висновки щодо правильності розрахунків (Метод Монте-Карло vs Аналітичні Розрахунки)

Огляд

Метою цього завдання було перевірити правильність розрахунків ймовірностей сум при киданні двох кубиків, використовуючи метод Монте-Карло та аналітичні розрахунки. Метод Монте-Карло полягав у імітації великої кількості кидків кубиків (100 000) і визначенні ймовірностей кожної можливої суми (від 2 до 12). Після цього результати симуляцій були порівняні з аналітично обчисленими ймовірностями.

Порівняння результатів

Аналітичні ймовірності були обчислені на основі всіх можливих комбінацій результатів для двох шестигранних кубиків. Найвища ймовірність спостерігалася для суми 7, яка може бути отримана з найбільшою кількістю комбінацій (наприклад, (1, 6), (2, 5), і т.д.). Інші суми мали меншу кількість комбінацій і, відповідно, меншу ймовірність.

Метод Монте-Карло продемонстрував, що для дуже великої кількості симуляцій ймовірності кожної суми наближаються до аналітичних значень. Це підтверджується з графіків та порівняння результатів.

Висновки з порівняння

Точність Методу Монте-Карло:

Для великої кількості симуляцій (100 000) ймовірності, отримані за допомогою методу Монте-Карло, дуже близькі до аналітичних значень, що свідчить про правильність використання цього методу для статистичних оцінок.

Метод Монте-Карло підтверджує закон великих чисел: чим більша кількість симуляцій, тим точніше результати наближаються до теоретичних ймовірностей.

Відхилення:

Для менших кількостей кидків відхилення можуть бути значними, оскільки результат кожного кидка є випадковим, і може зайняти певний час, щоб середнє значення стабілізувалося.

Проте, для 100 000 кидків відхилення були мінімальні і становили менше ніж 0.1% для кожної можливої суми.

Практичне Застосування:

Метод Монте-Карло підходить для моделювання подій, де аналітичний розрахунок ймовірностей може бути складним або недоступним. Ця техніка є корисною для випадків, коли є велика кількість випадкових факторів або комбінацій.

Висновок

Метод Монте-Карло продемонстрував хорошу точність для оцінки ймовірностей сум при киданні двох кубиків. Для великої кількості симуляцій (100 000) ймовірності кожної суми дуже близькі до аналітичних значень, що підтверджує правильність як теоретичних розрахунків, так і надійність методу Монте-Карло для моделювання випадкових подій. Точність цього методу робить його ефективним інструментом для оцінки ймовірностей у складних системах, де традиційні аналітичні методи можуть бути недостатньо ефективними або складними для застосування.

<!--  English-->

# Conclusions on the Accuracy of Calculations (Monte Carlo Method vs Analytical Calculations)

## Overview

The goal of this task was to verify the accuracy of probability calculations for the sums obtained by rolling two dice using both the Monte Carlo method and analytical calculations. The Monte Carlo method involved simulating a large number of dice rolls (100,000) and determining the probabilities of each possible sum (from 2 to 12). The results of the simulations were then compared with analytically computed probabilities.

## Comparison of Results

- Analytical probabilities were calculated based on all possible combinations of results for two six-sided dice. The highest probability was observed for the sum of **7**, which can be obtained with the largest number of combinations (e.g., (1, 6), (2, 5), etc.). Other sums had fewer combinations and therefore lower probabilities.
- The Monte Carlo method demonstrated that for a very large number of simulations, the probabilities for each sum approach the analytical values. This is confirmed by the graphs and comparison of results.

### Key Findings

1. **Accuracy of the Monte Carlo Method**:

   - For a large number of simulations (100,000), the probabilities obtained using the Monte Carlo method are very close to the analytical values, indicating the reliability of this method for statistical estimation.
   - The Monte Carlo method supports the law of large numbers: the greater the number of simulations, the closer the results get to the theoretical probabilities.

2. **Deviations**:

   - For smaller numbers of rolls, the deviations can be significant, as each roll is random, and it may take some time for the average to stabilize.
   - However, for 100,000 rolls, the deviations were minimal and amounted to less than 0.1% for each possible sum.

3. **Practical Applications**:
   - The Monte Carlo method is suitable for modeling events where analytical calculation of probabilities may be complex or unavailable. This technique is useful for scenarios involving a large number of random factors or combinations.

## Conclusion

The Monte Carlo method demonstrated high accuracy for estimating the probabilities of sums when rolling two dice. For a large number of simulations (100,000), the probabilities of each sum were very close to the analytical values, confirming the correctness of both the theoretical calculations and the reliability of the Monte Carlo method for modeling random events. The accuracy of this method makes it an effective tool for estimating probabilities in complex systems where traditional analytical methods may be insufficient or difficult to apply.
