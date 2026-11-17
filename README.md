
# First AI Cost Tracker Project

## FileName main.py

### Key Value Pair (Dictionary)


prices = {"input": 0.10, "output": 0.40}
 

 ### Function definition that return tokens  calucaltion  for input and output
 def cost(tokens, price_per_million):
    return tokens * price_per_million / 1_000_000

### Calculate total cost
total = cost(2000, prices["input"]) + cost(500, prices["output"])

### display on screen
print(f"Cost per call: ${total:.6f}")

