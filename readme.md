# 📝 Flask TODO

Welcome to Flask TODO! 🚀 A simple, yet powerful TODO list application using Flask and HTMX that features user authentication, TODO creation and management, and a host of other interactive interface features.

## 🛠️ Features

### 🔒 User Authentication
- **Register**: Create a new account with just your full name. You will receive a **unique 16-character key** to use for logging in. 🔑
- **Login**: Access your TODO list effortlessly with your unique key—no email or password needed! ✨
### ✅ TODO Management
- **Add TODOs**: Quickly add new tasks to your list. 🆕
- **Toggle Completion**: Mark TODOs as completed or incomplete with a single click. ✔️❌
- **Delete TODOs**: Remove tasks from your list easily. 🗑️

### 🌟 Dynamic Updates
- **Real-Time Updates**: Thanks to HTMX, the TODO list updates dynamically without refreshing the page. 🖥️🔄

> [!NOTE]
> There is a small issue and because of that, we need to refresh the page everytime you make a new task. We will be happy to see someone who can fix it! (Read [contributing](#-contributing).)
## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Python-dotenv (for environment variables)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sudo-arash/flask-todo.git
    cd flask-todo
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the environment variables:**
    - Copy `.env.example` to `.env`:
      ```bash
      cp .env.example .env
      ```
    - Update `.env` with your own values.

6. **Initialize the database:**
    ```bash
    python
    >>> from app import db
    >>> db.create_all()
    ```

7. **Run the application:**
    ```bash
    python app.py
    ```
    All that remains now is to open `http://127.0.0.1:5000/` in the web browser of your choice, and voilà! You now have your shiny, new todo application up and running.

## 🤝 Contributing

Issues and PRs welcome! Also, feel free to open issues or submit pull requests. 🎉

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.