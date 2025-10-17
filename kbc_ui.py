import tkinter as tk
from tkinter import messagebox
import lifelines
import prizes
from confetti import show_confetti


# ---- Sample Questions (keep your existing list) ----
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": 3
    },
    {
        "question": "Who wrote the National Anthem of India?",
        "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Sarojini Naidu", "Bankim Chandra Chatterjee"],
        "answer": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"],
        "answer": 2
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": 2
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Gd", "Go", "Au", "Ag"],
        "answer": 3
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["Germany", "France", "England", "Spain"],
        "answer": 2
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["1", "2", "3", "5"],
        "answer": 2
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Bhagat Singh"],
        "answer": 2
    },
    {
        "question": "Which language has the most native speakers?",
        "options": ["English", "Mandarin", "Hindi", "Spanish"],
        "answer": 2
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": 2
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["1945", "1946", "1947", "1950"],
        "answer": 3
    },
    {
        "question": "Which element is needed for the production of nuclear energy?",
        "options": ["Uranium", "Coal", "Iron", "Silver"],
        "answer": 1
    },
    {
        "question": "Who is known as the Missile Man of India?",
        "options": ["APJ Abdul Kalam", "Vikram Sarabhai", "Rakesh Sharma", "Homi Bhabha"],
        "answer": 1
    },
    {
        "question": "Which animal is known as the Ship of the Desert?",
        "options": ["Horse", "Camel", "Elephant", "Donkey"],
        "answer": 2
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["China", "Brazil", "UK", "Russia"],
        "answer": 2
    },
    {
        "question": "Which instrument measures earthquakes?",
        "options": ["Barometer", "Seismograph", "Thermometer", "Anemometer"],
        "answer": 2
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Michelangelo", "Van Gogh", "Leonardo da Vinci", "Picasso"],
        "answer": 3
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Yen", "Won", "Dollar"],
        "answer": 2
    },
    {
        "question": "Who discovered gravity?",
        "options": ["Newton", "Einstein", "Galileo", "Kepler"],
        "answer": 1
    },
    {
        "question": "Which blood group is known as universal donor?",
        "options": ["O+", "O-", "AB+", "AB-"],
        "answer": 2
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "Thailand", "Korea"],
        "answer": 2
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["Oxygen", "Water", "Hydrogen", "Salt"],
        "answer": 2
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["Tiger", "Leopard", "Cheetah", "Lion"],
        "answer": 3
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": 3
    },
    {
        "question": "Which vitamin is produced when skin is exposed to sunlight?",
        "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin B12"],
        "answer": 3
    },
    {
        "question": "Who was the first man to step on the moon?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
        "answer": 1
    },
    {
        "question": "Which is the smallest continent?",
        "options": ["Europe", "Australia", "Antarctica", "South America"],
        "answer": 2
    },
    {
        "question": "Which organ purifies our blood?",
        "options": ["Heart", "Kidney", "Liver", "Lungs"],
        "answer": 2
    },
    {
        "question": "What is the national flower of India?",
        "options": ["Rose", "Lotus", "Sunflower", "Jasmine"],
        "answer": 2
    }
]

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0b0340")  # KBC dark blue

        self.current_q = 0
        self.score = 0

        # Lifeline usage flags
        self.used_5050 = False
        self.used_audience = False
        self.used_phone = False

        self.timer_seconds = 30
        self.timer_running = False

        self.create_ui()
        self.load_question()

    def create_ui(self):
        # Left Frame for prize ladder
        left_frame = tk.Frame(self.root, bg="#0b0340")
        left_frame.pack(side="left", fill="y", padx=20, pady=20)

        self.prize_labels = []
        for i, amount in enumerate(reversed(prizes.get_prizes()), start=1):
            lbl = tk.Label(left_frame, text=f"{len(prizes.get_prizes())-i+1}. {amount}",
                           font=("Helvetica", 12, "bold"), bg="#0b0340", fg="white", anchor="w")
            lbl.pack(fill="x", pady=2)
            self.prize_labels.append(lbl)

        # Center frame for question and options
        center_frame = tk.Frame(self.root, bg="#0b0340")
        center_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)

        self.question_label = tk.Label(center_frame, text="", font=("Helvetica", 18, "bold"),
                                       bg="#0b0340", fg="white", wraplength=600, justify="center")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(center_frame, text="", font=("Helvetica", 14),
                            width=40, bg="#1c0465", fg="white",
                            activebackground="#f5d142", activeforeground="black",
                            command=lambda idx=i: self.check_answer(idx+1))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Timer label
        self.timer_label = tk.Label(center_frame, text="Time: 30", font=("Helvetica", 14, "bold"),
                                    bg="#0b0340", fg="gold")
        self.timer_label.pack(pady=10)

        # Lifeline Buttons
        lifeline_frame = tk.Frame(center_frame, bg="#0b0340")
        lifeline_frame.pack(pady=20)

        self.btn_5050 = tk.Button(lifeline_frame, text="50-50", font=("Helvetica", 12), bg="gold",
                                  command=self.use_5050)
        self.btn_5050.grid(row=0, column=0, padx=5)

        self.btn_audience = tk.Button(lifeline_frame, text="Audience Poll", font=("Helvetica", 12), bg="gold",
                                      command=self.use_audience)
        self.btn_audience.grid(row=0, column=1, padx=5)

        self.btn_phone = tk.Button(lifeline_frame, text="Phone a Friend", font=("Helvetica", 12), bg="gold",
                                   command=self.use_phone)
        self.btn_phone.grid(row=0, column=2, padx=5)

    def highlight_prize(self):
        for lbl in self.prize_labels:
            lbl.config(bg="#0b0340")
        prize_index = len(prizes.get_prizes()) - 1 - self.current_q
        if 0 <= prize_index < len(self.prize_labels):
            self.prize_labels[prize_index].config(bg="#f5d142", fg="black")

    def load_question(self):
        if self.current_q >= len(questions):
            messagebox.showinfo("Winner!", f"You've won {prizes.get_prizes()[-1]}!")
            self.root.quit()
            return

        q_data = questions[self.current_q]
        self.question_label.config(text=q_data["question"])

        for i, opt in enumerate(q_data["options"]):
            self.option_buttons[i].config(text=opt, state="normal", bg="#1c0465", fg="white")

        self.highlight_prize()
        self.timer_seconds = 30
        self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_seconds > 0 and self.timer_running:
            self.timer_label.config(text=f"Time: {self.timer_seconds}")
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        elif self.timer_seconds == 0:
            self.time_up()

    def time_up(self):
        self.timer_running = False
        messagebox.showerror("Time's up!", "You ran out of time!")
        self.root.quit()

    def check_answer(self, choice):
        self.timer_running = False
        q_data = questions[self.current_q]
        if choice == q_data["answer"]:
            # Show confetti animation
            show_confetti(self.root, duration=1500)

            # Show the correct message after confetti finishes
            self.root.after(1500, lambda: self.show_correct_message())

        else:
            messagebox.showerror("Wrong!", "Sorry, that's not correct.")
            self.root.quit()
    def show_correct_message(self):
        messagebox.showinfo(
            "Correct!",
            f"That's right! You won {prizes.get_prizes()[self.current_q]}"
        )
        self.current_q += 1
        self.load_question()

    def use_5050(self):
        if self.used_5050:
            return
        self.used_5050 = True
        q_data = questions[self.current_q]
        reduced = lifelines.lifeline_5050(q_data["answer"], q_data["options"])
        keep_indexes = [i-1 for i, _ in reduced]
        for i in range(4):
            if i not in keep_indexes:
                self.option_buttons[i].config(text="", state="disabled")
        self.btn_5050.config(state="disabled")

    def use_audience(self):
        if self.used_audience:
            return
        self.used_audience = True
        q_data = questions[self.current_q]
        poll_result = lifelines.lifeline_audience_poll(q_data["answer"])
        result_text = "\n".join([f"{chr(65+i)}: {poll_result[i]}%" for i in range(4)])
        messagebox.showinfo("Audience Poll", result_text)
        self.btn_audience.config(state="disabled")

    def use_phone(self):
        if self.used_phone:
            return
        self.used_phone = True
        q_data = questions[self.current_q]
        suggestion = lifelines.lifeline_phone_friend('answer')(q_data["answer"], q_data["options"])
        messagebox.showinfo("Phone a Friend", f"Your friend thinks the answer is: {suggestion}")
        self.btn_phone.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()
