def months(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        next(file)
        month_counts = {}
        all_total = 0

        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 5 and parts[4]:
                date_parts = parts[4].split('/')
                if date_parts and len(date_parts[0]) > 0:
                    month = int(date_parts[0])
                else:
                    month = 0
                if month > 0:
                    month_counts[month] = month_counts.get(month, 0) + 1
                    all_total += 1

    return month_counts, all_total


def main():
    filepath = "astronauts.csv"
    month_counts, total = months(filepath)

    top_three = []
    for _ in range(min(3, len(month_counts))):
        max_month = max(month_counts, key=month_counts.get)
        top_three.append((max_month, round(month_counts.pop(max_month) / total * 100, 1)))

    for month, percentage in top_three:
        print(f"{month}. hónap: {percentage}%")


main()
