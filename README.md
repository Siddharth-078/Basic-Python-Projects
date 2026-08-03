# Basic Python Projects

A collection of beginner-friendly Python projects covering variables, data types, strings, conditionals, and lists/tuples — built while learning Python fundamentals.

## Projects

### 1. Contact Card Generator
Takes basic user details (name, age, phone, email, hobbies) and generates a formatted contact card, with input validation for each field.

**How to run:**
```bash
python contactcard.py
```

Follow the prompts to enter your details — the program validates your inputs and prints a formatted card at the end.

---

### 2. Restaurant Bill Splitter
Calculates a restaurant bill for a group of 3 friends, including tax and tip, and splits the total either **equally** or **individually** (based on what each person ordered).

**How it works:**
- Takes each person's name and order price (3 people, name validated to be letters only)
- Takes a tip amount
- Automatically calculates a 5% tax on the subtotal
- Lets you choose:
  - **Equal split (E)** — total divided evenly across all 3 people
  - **Individual split (I)** — each person pays their own order amount, plus an equal share of tax + tip
- Prints a clean, formatted bill summary

**How to run:**
```bash
python bill.py
```

Follow the prompts: enter each person's name and order price, enter a tip amount, then type `E` for equal split or `I` for individual split.
