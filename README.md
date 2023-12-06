# MyFitness

MyFitness is a Django project designed for university purposes, allowing users to track their meal nutrition, set goals
for specific calorie, protein, carbs, and fats intake, and monitor their macros. The project utilizes the FoodData
Central (FDC) database for nutritional information.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Running the Project Locally](#running-the-project-locally)
- [Usage](#usage)

## Getting Started

These instructions will help you set up and run the MyFitness project on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.10)
- Pip (package installer for Python)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/varlamzhordania/myfitness.git
```

2. Navigate to the project directory:

   ```bash
   cd myfitness
   cd backend
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On Unix or MacOS:

      ```bash
      source venv/bin/activate
      ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project Locally

1. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser (for Django admin access):

   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at [http://localhost:8000](http://localhost:8000).

4. Access the Django admin interface at [http://localhost:8000/admin](http://localhost:8000/admin) and log in with the
   superuser credentials created earlier.

## Configuration

Rename the example.env file to .env:

```bash
mv example.env .env
```

Open the .env file and fill in the FDC_TOKEN variable with your FoodData Central (FDC) API token.

## Usage

MyFitness allows users to:

- Track meal nutrition
- Set goals for calorie, protein, carbs, and fats intake
- Monitor their macros

Note: MyFitness uses the FoodData Central (FDC) database for nutritional information.
