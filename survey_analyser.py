
import csv
from collections import Counter
from pathlib import Path


def load_responses(filename):
    """Load anonymised questionnaire responses from a CSV file."""
    try:
        with open(filename, "r", newline="", encoding="utf-8-sig") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return []


def analyse_responses(responses):
    """Summarise response patterns across questionnaire columns."""
    if not responses:
        return {}

    results = {}

    for question in responses[0]:
        answers = [
            row[question].strip()
            for row in responses
            if row.get(question, "").strip()
        ]

        results[question] = Counter(answers)

    return results


def save_report(results, filename="analysis_report.txt"):
    """Save analysis results to a text report."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("ReConnectSphere Survey Analysis Report\n")
        file.write("=" * 42 + "\n\n")

        for question, counts in results.items():
            file.write(f"Question: {question}\n")
            file.write("-" * 30 + "\n")

            for answer, count in counts.most_common():
                percentage = count / sum(counts.values()) * 100
                file.write(
                    f"{answer}: {count} responses ({percentage:.1f}%)\n"
                )

            file.write("\n")

    print(f"Report saved as {filename}")


def main():
    filename = input("Enter the CSV filename: ").strip()

    responses = load_responses(filename)

    if not responses:
        print("No responses available to analyse.")
        return

    results = analyse_responses(responses)

    print(f"\nSuccessfully loaded {len(responses)} responses.")

    save_report(results)

    print("Analysis complete!")


if __name__ == "__main__":
    main()
