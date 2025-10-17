# main.py

import options
import rules
import questions
import lifelines
import prizes
import timer

def main():
    # Display the game title and subtitle
    print("=" * 60)
    print("🎯  KAUN BANEGA CROREPATI  🎯".center(60))
    print("💰  Let's see if you can become a Crorepati!  💰".center(60))
    print("=" * 60)

    while True:
        choice = options.show_options()

        if choice == 1:
            rules.show_rules()

        elif choice == 2:
            print("\nStarting the game... Get ready!")
            play_game()

        elif choice == 3:
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

def play_game():
    # Get all questions
    q_list = questions.get_question()
    prize_list = prizes.get_prizes()
    used_lifelines = []

    for i, q_data in enumerate(q_list):
        question = q_data["question"]
        options_list = q_data["options"]
        correct_answer = q_data["answer"]

        print("\n" + "=" * 50)
        print(f"Question {i+1} for ₹{prize_list[i]}")
        print(question)
        for idx, opt in enumerate(options_list, start=1):
            print(f"{idx}. {opt}")
        print("=" * 50)

        # Timer before input
        timer.countdown(5)

        # Lifeline option
        available_lifelines = ["50-50", "Audience Poll", "Phone a Friend"]

        use_life = input("Do you want to use a lifeline? (yes/no): ").strip().lower()
        if use_life == "yes":
            if available_lifelines:
                print("Available Lifelines:")
                for idx, lf in enumerate(available_lifelines, start=1):
                    print(f"{idx}. {lf}")
                try:
                    lf_choice = int(input("Choose lifeline number: "))
                    chosen_lifeline = available_lifelines[lf_choice - 1]

                    if chosen_lifeline == "50-50":
                        reduced_options = lifelines.lifeline_5050(q_data["answer"], q_data["options"])
                        print("Reduced options:")
                        for idx, text in reduced_options:
                            print(f"{idx}. {text}")

                    elif chosen_lifeline == "Audience Poll":
                        poll = lifelines.lifeline_audience_poll(q_data["answer"], q_data["options"])
                        print("Audience Poll Results:", poll)

                    elif chosen_lifeline == "Phone a Friend":
                        advice = lifelines.lifeline_phone_friend(q_data["answer"])
                        print(advice)

                    used_lifelines.append(chosen_lifeline)
                    available_lifelines.remove(chosen_lifeline)

                except (ValueError, IndexError):
                    print("Invalid lifeline choice. Continuing without lifeline.")
            else:
                print("No lifelines left!")

        # Take answer
        try:
            ans = int(input("Enter your answer (1-4): "))
        except ValueError:
            print("Invalid input! You lost the game.")
            break

        if ans == correct_answer:
            print("✅ Correct Answer!")
        else:
            print(f"❌ Wrong Answer! The correct answer was option {correct_answer}.")
            print(f"You won ₹{prize_list[i-1] if i > 0 else 0}")
            break
    else:
        print("🎉 Congratulations! You completed all the questions!")
        print(f"You are the Crorepati and won ₹{prize_list[-1]}!")

if __name__ == "__main__":
    main()
