
"""
ReConnectSphere Survey Analyser
A beginner Python project developed alongside the CREST Gold project.

Analyses anonymised questionnaire responses using Python's
built-in CSV and collections modules.
"""

import csv
import os
from collections import Counter


def load_survey(filename):
    """Load survey responses from a CSV file."""

    if not os.path.exists(filename):
        print(f"\nFile not found: {filename}")
        return []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        responses = list(reader)

    print(f"\nLoaded {len(responses)} responses from {filename}.")
    return responses


def analyse_survey(responses, survey_name):
    """Analyse questionnaire responses."""

    print("\n" + "=" * 55)
    print(f"ANALYSIS: {survey_name}")
    print("=" * 55)

    if not responses:
        print("No responses available to analyse.")
        return

    print(f"\nTotal responses: {len(responses)}")

    for question in responses[0].keys():

        answers = [
            row[question].strip()
            for row in responses
            if row.get(question) and row[question].strip()
        ]

        if not answers:
            continue

        print("\n" + "-" * 45)
        print(f"Question: {question}")
        print(f"Valid responses: {len(answers)}")

        # Count answers to categorical questions
        counts = Counter(answers)

        if len(counts) <= 20:
            print("\nResponse breakdown:")

            for answer, count in counts.most_common():
                percentage = (count / len(answers)) * 100

                print(
                    f"  {answer}: {count} "
                    f"({percentage:.1f}%)"
                )

        else:
            # Summarise longer written responses
            print("\nWritten response examples:")

            for answer in answers[:5]:
                print(f"  - {answer}")

            print(
                f"\nTotal written responses: {len(answers)}"
            )


def save_report(filename, content):
    """Save analysis results to a text report."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"\nReport saved as {filename}")


def main():

    print("=" * 55)
    print("       RECONNECTSPHERE SURVEY ANALYSER")
    print("=" * 55)

    print("\nThis programme analyses anonymised survey data.")
    print("It does not identify participants or provide conclusions")
    print("about individuals.")

    survey_files = [
        ("survey1.csv", "Questionnaire 1"),
        ("survey2.csv", "Questionnaire 2")
    ]

    for filename, survey_name in survey_files:
        responses = load_survey(filename)
        analyse_survey(responses, survey_name)

    print("\n" + "=" * 55)
    print("Analysis complete.")
    print("=" * 55)


if __name__ == "__main__":
    main()
