import matplotlib.pyplot as plt

def get_summary(data):
    total = sum(exp["amount"] for exp in data)
    return total

def category_breakdown(data):
    category_total = {}

    for exp in data:
        cat = exp["category"]
        category_total[cat] = category_total.get(cat, 0) + exp["amount"]

    return category_total

def show_chart(data):
    category_total = category_breakdown(data)

    labels = list(category_total.keys())
    values = list(category_total.values())

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Breakdown")
    plt.show()

def highest_category(data):
    category_total = category_breakdown(data)
    return max(category_total, key=category_total.get)


def suggest_reduction(data):
    category_total = category_breakdown(data)
    total = get_summary(data)

    suggestions = []

    for cat, amt in category_total.items():
        percent = (amt / total) * 100

        if percent > 40:
            if cat == "Food":
                suggestions.append("Reduce eating outside ")
            elif cat == "Travel":
                suggestions.append("Use public transport ")
            elif cat == "Bills":
                suggestions.append("Save electricity ")
            else:
                suggestions.append(f"Reduce spending on {cat}")

    return suggestions