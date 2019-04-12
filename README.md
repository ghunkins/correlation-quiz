# Correlation One | D.S. Challenge

This project is a basic Django web-app proof-of-concept for serving a Data Science quiz.

Programmer: `Gregory D. Hunkins`

### Installation & Run

Clone the repository locally.

```
git clone https://github.com/ghunkins/correlation-quiz.git
```

Enter the web-app folder.

```
cd correlation-quiz/interview
```
Create an environment suitable for running the web-app using `conda` and activate it.

```
conda env create -f environment.yml
conda activate correlation
```

Make the necessary migrations and create the tables.

```
python manage.py makemigrations; python manage.py migrate --run-syncdb
```

Run the server and navigate to `http://127.0.0.1:8000`.

```
python manage.py runserver
```

You should be able to navigate between the following screens:

![alt text](https://raw.githubusercontent.com/ghunkins/correlation-quiz/master/readme_imgs/signup.png)

![alt text](https://raw.githubusercontent.com/ghunkins/correlation-quiz/master/readme_imgs/question.png)


### Progress Report & TODO

This is not a full implementation of the requested project. Below are a basic set of `#TODO`s.

- Integrate with [`django-rest-framework`](https://www.django-rest-framework.org/) to enable a REST API
- Integrate [`django-multiselectfield`](https://pypi.org/project/django-multiselectfield/) with the question model and forms
- Install [`fluentcms-countdown`](https://github.com/django-fluent/fluentcms-countdown) to showcase and provide triggers for quizzes over the time threshold.
- Create a question review & thank you page after the final question is submitted


