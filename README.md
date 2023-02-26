# Library System Project

This is a library system project built with Django 3.2 that allows users to manage the borrowing and returning of books, search for books, add categories, and add new books (if an admin). Users can also sign up and log in to the system.

## Demo

Click [here](https://www.youtube.com/watch?v=0-GT9c9_h8Y) to view a demo of the Library System Project.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

```bash
$ git clone https://github.com/usamashehab/library.git
```


2. Change into the project directory:
```bash
$ cd library
```


3. Install the required dependencies:
```bash
$ pip install -r requirements.txt
```


4. Create the database tables:
```bash
$ python manage.py migrate
```



5. Start the development server:
```bash
$ python manage.py runserver
```

6. Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

Once the application is running, users can perform the following actions:

- Sign up or log in
- Search for books by title, author, or category
- Borrow and return books
- Add, update and delete books (if an admin)
- Add, update and delete categories (if an admin)


## Acknowledgements

- The Django documentation: https://docs.djangoproject.com/en/3.2/
- Bootstrap: https://getbootstrap.com/




