# AI & Technology Intern Assignment: Technical Tasks

This project contains the completed technical tasks for the AI & Technology Intern (EdTech) screening assignment. The project includes a simple chatbot and a To-Do Manager web application, both of which demonstrate a core functional workflow and an AI-powered feature.

---

### Task 1: Chatbot

#### Tech Stack

* **Language:** Python
* **Environment:** VS Code (or any other Python environment)

#### How to Run the Code

To run this chatbot, follow these simple steps:

1.  Ensure you have **Python 3** installed on your system.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you have saved the `chatbot.py` file.
4.  Execute the script using the following command:
    ```bash
    python chatbot.py
    ```
5.  The chatbot will start, and you can begin typing your questions.

#### Features Implemented

The chatbot is designed to handle the following FAQs about the Iron Lady programs:

* **Programs Offered:** Provides details on the types of programs available.
* **Program Duration:** Informs the user about the typical length of a program.
* **Online/Offline Mode:** Clarifies that the programs are conducted online.
* **Certificate Provision:** Confirms that certificates are provided upon completion.
* **Mentor Information:** Offers general information about the mentors.

A fallback AI response is provided for any questions that are not recognized.

---

### Task 2: To-Do Manager

#### Tech Stack

* **Language:** HTML, CSS, JavaScript
* **Environment:** Any modern web browser (e.g., Chrome, Firefox, Safari)

#### How to Run the Code

This is a single-file application, so running it is very simple.

1.  Ensure you have a modern web browser installed.
2.  Open the `index.html` file directly in your browser by double-clicking it.
3.  The application will load, and you can begin adding and managing your tasks.

#### Features Implemented

The To-Do Manager is designed with a full **CRUD** (Create, Read, Update, Delete) workflow and a bonus AI feature:

* **Create (Add):** Users can add new tasks by typing into the input field and clicking the "Add Task" button.
* **Read (View):** All tasks are displayed in a list format on the page.
* **Update (Edit):**
    * Clicking the pencil icon allows users to edit a task's text.
    * Clicking on the task text itself toggles its completion status, visually marking it as done with a strikethrough.
* **Delete (Remove):** The trash can icon allows users to delete a task from the list.
* **Bonus AI Feature:** Clicking the "Generate a new task" button uses an AI-powered function to automatically suggest and add a new, random task to the list. This demonstrates a simple integration of AI to enhance the application's functionality.
