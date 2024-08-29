
# Quiz Game

## Project Description

This Python-based quiz game is designed to test users' knowledge on various Islamic topics through a graphical user interface (GUI) built with Tkinter. The game features three distinct levels, each with a different type of quiz:

1. **General Religious Questions** - Test your knowledge with a set of general Islamic questions.
2. **"Who Said This in the Verse?"** - Identify the speaker of specific Quranic verses.
3. **"Who is Mentioned in the Verse?"** - Determine who is referred to in different Quranic verses.

### Features

- **Countdown Timer**: A countdown timer is included for each question, adding a time challenge element.
- **Score Tracking**: Scores are tracked throughout the game, and the best scores are saved and displayed.
- **Sound Effects**: The game includes sound effects for correct answers, incorrect answers, and button clicks.
- **Customizable Settings**: Users can toggle sound effects on or off.
- **High Score Management**: The game maintains and displays the highest scores achieved in different quiz levels.
- **Retry Option**: Players can retry the game if the time runs out or if they make mistakes.

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Make sure you have Python installed. Then, install the necessary packages:

   ```bash
   pip install pygame
   ```

   Tkinter is included with Python, so no additional installation is required for Tkinter.

3. **Run the Game**

   Execute the Python script to start the game:

   ```bash
   python <script-name>.py
   ```

## Usage Instructions

1. **Start the Game**

   Upon running the script, you will be presented with a menu. Click on "بدأ اللعب" (Start Playing) to begin.

2. **Select a Game Mode**

   Choose from the following game modes:
   
   - **أسئلة دينية عامة** (General Religious Questions)
   - **لعبة من القائل في الآية** (Who Said This in the Verse?)
   - **لعبة من المقصود في الآية** (Who is Mentioned in the Verse?)

   Click the corresponding button to start the selected game mode.

3. **Answering Questions**

   - Read the question displayed at the top.
   - You have only 20 seconds to answer.
   - Click on one of the four buttons below to select your answer.
   - If the answer is correct, you will earn points and move on to the next question.
   - If the answer is incorrect, your score will decrease.
   - If you selecte two incorrect choices or the time runs out, the game will end, and you will see your final score.

4. **Using Settings**

   Access the settings by clicking "ضبط الإعدادات" (Settings). You can toggle sound effects on or off.

5. **View High Scores**

   To view high scores, click "أعلى نقاط" (Best Scores) from the menu. The highest scores for each game mode will be displayed.

6. **Developer Information**

   For information about the developer, click "معلومات عن المطور" (Developer Info) from the menu.

7. **Retry Game**

   If the time runs out or you wish to try again, you can click "حاول مجددا" (Try Again) to restart the game.

## Notes

- Ensure that the sound files for correct answers and button clicks are available at the specified paths in the script. You may need to adjust the paths if they differ on your system.
- The high scores are saved in text files (`best_score_1.txt`, `best_score_2.txt`, `best_score_3.txt`) and can be reset using the "تصفير النقاط" (Reset Scores) button.

## Contact

For any issues or suggestions, you can reach out to the developer at [rayanereda90@gmail.com](mailto:rayanereda90@gmail.com).
