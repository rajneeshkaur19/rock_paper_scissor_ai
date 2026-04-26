# ✊📄✌️ AI Rock Paper Scissors

> A command-line game with an adaptive AI opponent that predicts your moves using frequency analysis.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Play Rock Paper Scissors against an AI that learns from you. The opponent tracks your move history using `collections.Counter` and counters your most-played choice — so the longer you play, the smarter it gets.

---

## Features

- **AI move prediction** — counters your most frequently played move
- **Two game modes** — Best of 3 or Best of 5
- **Score tracking** — live score displayed each round
- **Play again loop** — replay without restarting the script
- **Input validation** — handles invalid entries gracefully

---

## Getting Started

No external dependencies. Requires Python 3.x.

```bash
# Clone the repo
git clone https://github.com/your-username/ai-rock-paper-scissors.git

# Run the game
python rps.py
```

---

## How the AI Works

The AI maintains a full history of your moves each session. After each round, it uses `collections.Counter` to find the move you've played most often and selects the move that beats it. On the very first turn — before any history exists — it falls back to a random choice.

| Your most common move | AI plays |
|-----------------------|----------|
| Rock                  | Paper    |
| Paper                 | Scissors |
| Scissors              | Rock     |

---

## Project Structure
```
rps.py
├── main()               # Entry point and outer game loop
├── select_mode()        # Choose Best of 3 or Best of 5
├── play_game()          # Round logic and score tracking
├── get_user_move()      # Validated user input
├── get_ai_move()        # Frequency-based AI prediction
├── decide_winner()      # Determine round outcome
└── show_final_result()  # Display end-of-game result
```


## Author

**Rajneesh Kaur (Cherry)**

---

## License

This project is licensed under the [MIT License](LICENSE).
