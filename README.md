# University Evaluation System

## 1. Project Title

**University Evaluation System**

A Python-based university portal application for managing student authentication, academic evaluations, grades, GPA, and class performance analytics.

---

## 2. Project Overview

The **University Evaluation System** is a menu-driven Python application designed to manage and display academic information for students, teachers, and administrators.

The system provides different functionality based on the user's role:

* **Students** can view their grades, schedule, evaluation records, performance, and class statistics.
* **Teachers** can record and manage student evaluation scores and view class analytics.
* **Administrators** can create new users and check the system status.

The project is divided into separate Python modules for authentication, evaluation management, analytics, and the main application menu.

---

## 3. Features

### 3.1 Authentication

* User login using User ID/Registration Number and password.
* Role-based access for:

  * Student
  * Teacher
  * Administrator
* Separate dashboards for different user roles.
* User creation functionality for administrators.

### 3.2 Student Features

Students can:

* Log in to the university portal.
* View grades and academic schedule.
* View performance information.
* View attendance and examination performance.
* View assessment/evaluation details.
* View overall course score.
* View letter grade and GPA.
* Compare their performance with class statistics.

### 3.3 Teacher Features

Teachers can:

* Upload/record student marks.
* Create evaluation records.
* View class marksheets.
* View class performance analytics.
* Update existing evaluation records.
* Delete evaluation records.
* Calculate weighted student scores.

### 3.4 Evaluation System

The evaluation module provides:

* Creation of evaluation records.
* Retrieval of student evaluations.
* Updating evaluation records.
* Deletion of evaluation records.
* Score validation.
* Weighted score calculation.
* Letter grade calculation.
* GPA calculation.
* Class average and highest score calculation.

### 3.5 Analytics

The analytics module provides:

* Class average.
* Highest score.
* Lowest score.
* Number of passing students.
* Number of failing students.
* Grade distribution.
* Student progress visualization using text-based charts.

---

## 4. Technologies and Tools Used

### Programming Language

* **Python 3**

### Development Environment

* **Python IDLE**

### Version Control

* **Git**

### Repository Hosting

* **GitHub**

### Python Libraries/Modules

The project primarily uses Python's built-in functionality, including:

* `typing`
* `uuid`

The project is organized into the following Python modules:

```text
analytics.py
authentication.py
evaluation.py
main.py
```

---

## 5. Project Structure

```text
University-Evaluation/
│
├── analytics.py
├── authentication.py
├── evaluation.py
├── main.py
├── README.md
└── .gitignore
```

### `main.py`

Acts as the main entry point of the application. It initializes sample database information and displays the main menu.

### `authentication.py`

Contains:

* User authentication
* Student dashboard
* Teacher dashboard
* Administrator dashboard
* User management

### `evaluation.py`

Contains:

* Evaluation creation
* Evaluation retrieval
* Evaluation updating
* Evaluation deletion
* Grade calculation
* GPA calculation
* Class analytics

### `analytics.py`

Contains:

* Class performance calculations
* Grade distribution
* Student progress display
* Text-based performance reports

---

## 6. Installation and Setup

### Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/

During installation on Windows, make sure to select:

```text
Add Python to PATH
```

### Step 2: Download or Clone the Project

Clone the GitHub repository using:

```bash
git clone https://github.com/a-2305nanya/university-evaluation.git
```

Then move into the project directory:

```bash
cd university-evaluation
```

### Step 3: Check Python Installation

Run:

```bash
python --version
```

The command should display the installed Python version.

### Step 4: Run the Application

The main application can be run using:

```bash
python main.py
```

Alternatively, the project can be opened and executed using **Python IDLE**.

Open `main.py` in IDLE and select:

```text
Run → Run Module
```

---

## 7. How to Use the Application

After starting the application, the main menu is displayed:

```text
--- MAIN MENU ---

1. Authentication
2. Evaluation and display
3. Analytics
4. Exit
```

Enter the number corresponding to the required operation.

### Authentication

Select:

```text
1. Authentication
```

Enter the User ID and password.

The application identifies the user's role and opens the corresponding dashboard.

### Evaluation

Select:

```text
2. Evaluation and display
```

Teachers can manage evaluation records, including creating, viewing, updating, and deleting scores.

### Analytics

Select:

```text
3. Analytics
```

The system displays class performance information such as:

* Average score
* Highest score
* Lowest score
* Pass/fail information
* Grade distribution

### Exit

Select:

```text
4. Exit
```

to close the application.

---

## 8. Testing Instructions

Testing can be performed by running the application through Python IDLE or the terminal.

### Test 1: Application Startup

Run:

```bash
python main.py
```

Verify that the main menu appears correctly.

Expected result:

```text
--- MAIN MENU ---

1. Authentication
2. Evaluation and display
3. Analytics
4. Exit
```

### Test 2: Authentication

Select the authentication option and enter a valid user ID and password.

Verify that:

* The login succeeds.
* The correct user role is identified.
* The appropriate dashboard is displayed.

### Test 3: Invalid Login

Enter an incorrect user ID or password.

Expected behavior:

```text
[ERROR] Invalid ID or Password! Access Denied.
```

### Test 4: Evaluation Creation

From the teacher evaluation menu:

1. Select **Record New Score**.
2. Enter a student ID.
3. Enter a course ID.
4. Enter an assessment name.
5. Enter the score.
6. Enter the maximum score.
7. Enter the weight.

Verify that an evaluation ID is generated and the record is saved.

### Test 5: Evaluation Update

Select the update option and provide an existing evaluation ID.

Enter a new score and verify that the evaluation record is updated.

### Test 6: Evaluation Deletion

Select the delete option and provide an evaluation ID.

Verify that the evaluation record is removed.

### Test 7: Analytics

Select the analytics option and verify that the system displays:

* Class average
* Highest score
* Lowest score
* Pass/fail count
* Grade distribution

---

## 9. Sample Data

The project includes sample users and student academic data for testing.

Example roles include:

```text
Administrator
Teacher
Student
```

The application also initializes sample student information such as:

* Student IDs
* Student names
* Study hours
* Attendance
* Examination scores

This sample data is initialized when the main application starts.

---

## 10. Screenshots

Screenshots can be added to this section to demonstrate the application interface.

Recommended screenshots include:

1. Main Menu
2. Login Screen
3. Student Dashboard
4. Teacher Dashboard
5. Evaluation Management Menu
6. Class Analytics Report
7. Grade Distribution
8. GitHub Repository

Example:

```markdown
## Screenshots

### Main Menu

![Main Menu](screenshots/main-menu.png)

### Student Dashboard

![Student Dashboard](screenshots/student-dashboard.png)

### Class Analytics

![Class Analytics](screenshots/class-analytics.png)
```

Create a folder named:

```text
screenshots/
```

and place your screenshots inside it.

---

## 11. Git and GitHub

The project uses Git for version control and GitHub for remote repository hosting.

To save changes:

```bash
git add .
git commit -m "Update project"
git push
```

To get the latest version of the project:

```bash
git pull
```

---

## 12. Conclusion

The University Evaluation System demonstrates a modular Python application for managing university-related authentication, student evaluations, grades, GPA, and academic performance analytics.

The project separates major functionality into different modules, making the application easier to organize, maintain, test, and extend.
