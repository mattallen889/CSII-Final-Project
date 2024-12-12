import csv
import os

class Calculator:
    """
    Handles the CSV file called 'CSProject.' It writes headers for the file, inputs the scores, and
    calculates the averages of the scores.
    """

    def __init__(self, file_name) -> None:
        """
        Starts the calculator and checks if the file even exists.

        :param file_name: Name of the CSV file that stores the data
        """
        self.file_name = file_name
        file_exists = os.path.exists(self.file_name)
        if not file_exists:
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                headers = ["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Average"]
                writer.writerow(headers)

    def process(self, name, scores) -> None:
        """
        Processes the scores, calculates the average, and adds the data to the file
        :param name: Name of the student
        :param scores: The integers that the students input that represent their grades/scores. 0's will be
        used to fill in any extra spaces for scores.
        :return:
        """
        while len(scores) < 4:
            scores.append(0)
        num_score = [score for score in scores if score > 0]
        average = sum(num_score) / len(num_score) if num_score else 0
        row = [name] + scores + [f"{average:.2f}"]
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

class Logic:
    """
    Handles the logic for interacting within the GUI. It validates the inputs, edits the GUI's score inputs,
    and sends data to the calculator class.
    """
    def __init__(self, ui):
        """
        Starts the logic instance and connects all the GUI elements to the correct action.
        :param ui: The GUI object containing all user elements
        """
        self.ui = ui
        self.calculator = Calculator("CSProject.csv")
        self.ui.LineEditAttempts.textChanged.connect(self.attempts_change)
        self.ui.pushButton.clicked.connect(self.submit_action)

    def attempts_change(self) -> None:
        """
        Updates the visibility of the score input text boxes. This is based on the number
        of attempts entered at the top of the GUI.
        """
        attempts = self.ui.LineEditAttempts.text()
        try:
            attempts = int(attempts)
        except ValueError:
            attempts = 0
        self.ui.score1.setVisible(attempts >= 1)
        self.ui.Score1Label.setVisible(attempts >= 1)
        self.ui.score2.setVisible(attempts >= 2)
        self.ui.Score2Label.setVisible(attempts >= 2)
        self.ui.score3.setVisible(attempts >= 3)
        self.ui.Score3Label.setVisible(attempts >= 3)
        self.ui.score4.setVisible(attempts >= 4)
        self.ui.Score4Label.setVisible(attempts >= 4)

    def submit_action(self):
        """
        Updates the feedback given in the GUI, helps save data to the file, and validates the inputs. It
        validates the input by checking the number of attempts, scores being between 1 and 100, and that
        the number of scores match the number of attempts.

         Displays different feedback depending on the error type or success.
        """
        name = self.ui.LineEditName.text().strip()
        attempt = self.ui.LineEditAttempts.text()
        scores = [self.ui.score1.text().strip(), self.ui.score2.text().strip(), self.ui.score3.text().strip(), self.ui.score4.text().strip(),]

        try:
            attempts = int(attempt)
            if attempts > 5:
                self.ui.SubmitLabel.setText("1-4 Attempts!")
                self.ui.SubmitLabel.show()
                return

            scores = [int(score) for score in scores if score]

            if not all(1 <= score <= 100 for score in scores):
                self.ui.SubmitLabel.setText("Between 1 and 100")
                self.ui.SubmitLabel.show()
                return

            if len(scores) != attempts:
                self.ui.SubmitLabel.setText(f"Enter {attempts} scores!")
                self.ui.SubmitLabel.show()
                return


            self.calculator.process(name, scores)
            self.ui.SubmitLabel.setText("SUBMITTED")
            self.ui.SubmitLabel.setStyleSheet("color: green;")
            self.ui.SubmitLabel.show()

        except ValueError:
            self.ui.SubmitLabel.setText("Invalid input!")
            self.ui.SubmitLabel.show()

