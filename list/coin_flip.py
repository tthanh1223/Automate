"""
If you flip a coin 100 times and write down an "H" for
each heads and "T" for tails.
"""
import random

def coin_flip_streaks(num_experiments=10000, num_flips=100, streak_length=10):
    streak_count = 0

    for _ in range(num_experiments):
        # Generate a list of random coin flips (0 for Tails, 1 for Heads)
        flips = [random.randint(0, 1) for _ in range(num_flips)]

        # Check for streaks
        current_streak = 1
        for i in range(1, len(flips)):
            if flips[i] == flips[i - 1]:
                current_streak += 1
                if current_streak == streak_length:
                    streak_count += 1
                    break
            else:
                current_streak = 1

    # Calculate the percentage of experiments containing a streak
    percentage = (streak_count / num_experiments) * 100
    print(f"Percentage of experiments with a streak of {streak_length}: {percentage:.2f}%")

# Run the experiment
coin_flip_streaks()
