# week6_lab.py
# Author: Daniela Pena

records = [
    {
        "id": 1,
        "name": "Abby",
        "category": "Travel",
        "amount": 1200,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jojo",
        "category": "Equipment",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "May",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Sarah", "category": "Travel", "amount": 89, "status": "Pending"},
    {
        "id": 5,
        "name": "Gretchen",
        "category": "Equipment",
        "amount": 2200,
        "status": "Pending",
    },
]

LIMIT = 1000
HIGH = 2000
total = 0

flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]
        if rec["amount"] > LIMIT:
            flagged.append(rec)
        if rec["amount"] > HIGH:
            high_value.append(rec)


lines = [
    f"Pending total: ${total:,.2f}",
    f"Needs review: {len(flagged)}",
    f"High-value: {len(high_value)}",
]

for line in lines:
    print(line)

import os

os.makedirs("data_dir", exist_ok=True)

with open("data_dir/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for r in flagged:
    print(f"  ID {r['id']}: {r['name']} - ${r['amount']:,.2f}")
