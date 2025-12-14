# EduManage - Class Management Website

EduManage is a comprehensive web-based platform designed to streamline educational institution management. It serves students, teachers, and administrators with a modern, responsive interface and robust features for academic tracking, scheduling, and communication.

## Features

### 🎓 **For Students**
*   **Dashboard:** View course progress, upcoming assignments, and announcements.
*   **Course Enrollment:** Browse available courses and request enrollment.
*   **Attendance Tracking:** Check attendance status and scan QR codes for instant check-in.
*   **Gradebook:** View scores for mini-tests, midterms, and final exams.
*   **Assignment Submission:** Submit homework and assignments directly through the portal.
*   **Feedback:** Provide feedback on courses and instructors.

### 👩‍🏫 **For Teachers**
*   **Class Management:** Create and manage classes, upload materials, and post announcements.
*   **Grading:** Enter and update student grades efficiently.
*   **Attendance:** Generate QR codes for sessions or manually mark attendance.
*   **Assignments:** Create assignments, set due dates, and grade submissions.
*   **Statistics:** View class performance analytics and identify students at risk.

### 🛠 **For Administrators (Staff)**
*   **User Management:** Manage student, teacher, and staff accounts.
*   **Course Management:** Oversee class types, schedules, and enrollments.
*   **System Oversight:** Monitor platform statistics and handle enrollment requests.

## Tech Stack

*   **Backend:** Django 5.0+ (Python)
*   **Database:** Microsoft SQL Server (MSSQL)
*   **Frontend:** HTML5, Tailwind CSS, JavaScript
*   **Styling:** Custom CSS with modern animations and responsive design

## Prerequisites

Before running the project, ensure you have the following installed:

1.  **Python 3.10+**: [Download Python](https://www.python.org/downloads/)
2.  **Microsoft SQL Server**: [Download SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
3.  **ODBC Driver 17 for SQL Server**: Required for Django to connect to MSSQL. [Download Driver](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

## Installation & Setup

1.  **Clone the Repository** (if applicable) or navigate to the project folder.

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure the Database**
    Open `ClassManagementWebsite/settings.py` and locate the `DATABASES` section. Update the `NAME`, `USER`, `PASSWORD`, and `HOST` to match your SQL Server configuration.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'YourDatabaseName',
            'USER': 'YourUsername',
            'PASSWORD': 'YourPassword',
            'HOST': 'localhost',
            'PORT': '1433',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
    ```

6.  **Apply Migrations**
    Create the necessary database tables:
    ```bash
    python manage.py migrate
    ```

7.  **Seed Initial Data (Optional)**
    Populate the database with sample data for testing:
    ```bash
    python manage.py seed_data
    ```

8.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

9.  **Access the Application**
    Open your browser and navigate to: `http://127.0.0.1:8000/`

## Project Structure

*   `accounts/`: Authentication (Login, Signup) logic.
*   `core/`: Core models (Student, Teacher, Class) and main views.
*   `dashboard/`: The main functional area for all user roles (Student, Teacher, Admin).
*   `templates/`: HTML templates (now unified with `base.html` inheritance).
*   `static/`: CSS, JavaScript, and images.
*   `media/`: User-uploaded content (assignments, materials, class images).

## License

This project is for educational purposes.
