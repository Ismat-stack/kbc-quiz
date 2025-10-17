# lifelines.py

import random


def lifeline_5050(answer, options):
    """
    Removes two wrong options and returns a reduced list of (index, option_text).

    answer: int (1-based index) or str (correct answer text)
    options: List of answer strings
    """
    # If answer is text, find its index
    if isinstance(answer, str):
        correct_index = options.index(answer)  # 0-based
    else:
        correct_index = answer - 1  # Convert 1-based to 0-based

    # Create list of wrong option indexes
    wrong_indexes = [i for i in range(len(options)) if i != correct_index]

    # Select one wrong option to keep
    keep_wrong_index = random.choice(wrong_indexes)

    # Always keep correct + one wrong
    reduced = [
        (correct_index + 1, options[correct_index]),
        (keep_wrong_index + 1, options[keep_wrong_index])
    ]

    # Shuffle so correct answer isn't always first
    random.shuffle(reduced)
    return reduced


def lifeline_audience_poll(answer, options):
    """Simulates audience poll percentages."""
    poll = {}
    correct_percentage = random.randint(50, 80)
    remaining_percentage = 100 - correct_percentage

    wrong_distribution = random.sample(range(0, remaining_percentage), len(options) - 1)
    wrong_distribution.append(remaining_percentage)
    wrong_distribution.sort()
    wrong_percentages = [
        wrong_distribution[i+1] - wrong_distribution[i]
        for i in range(len(wrong_distribution) - 1)
    ]

    for opt in options:
        if opt == answer:
            poll[opt] = correct_percentage
        else:
            poll[opt] = wrong_percentages.pop()

    return poll


def lifeline_phone_friend(answer):
    """Simulates phone a friend (friend may be unsure)."""
    if random.random() < 0.8:  # 80% chance friend knows answer
        return f"I think the correct answer is '{answer}'."
    else:
        guess = random.choice(['A', 'B', 'C', 'D'])
        return f"I'm not entirely sure"