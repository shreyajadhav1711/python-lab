transactions = []

# Accept 5 transaction values
for i in range(5):
    amount = float(input("Enter transaction amount: "))
    transactions.append(amount)

# Find largest transaction
largest = max(transactions)

# Find average
average = sum(transactions) / len(transactions)

# Display results
print("\nTransaction List:", transactions)
print("Largest Transaction:", largest)
print("Average Spend:", average)