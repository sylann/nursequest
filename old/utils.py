from random import randint

import datetime
import requests
from bs4 import BeautifulSoup
from faker import Faker

from app.models.models_old.users import User

WEBSITE_URL = 'https://www.medicinenet.com'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
fake = Faker('fr_FR')


def make_url(letter):
    return WEBSITE_URL + '/diseases_and_conditions/alpha_' + letter + '.htm'


def get_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print (response.status_code)
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    html = list(soup.children)[2]
    __, head, __, body, __ = list(html.children)
    return body


def get_disease_html_elements(body):
    results = body.find('div', class_='AZ_results')
    return results.select('li > a')


def get_all_diseases():
    for letter in ALPHABET:
        url = make_url(letter)
        page = get_page(url)
        if page is None:
            continue
        for d in get_disease_html_elements(page):
            yield d


def generate_patient_date():
    return fake.date_time_between(
        start_date="-110y", end_date="now"
    )


def generate_random_list(Table_):
    max_count = Table_.query.count()
    quota = randint(0, max_count)
    cursors = set()
    while (len(cursors) < quota):
        cursors.add(randint(0, max_count - 1))
    return [Table_.query.offset(cursor).first() for cursor in cursors]


def generate_fake_user():
    return dict(
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        hire_date=fake.past_date(),
        is_admin=fake.boolean(chance_of_getting_true=5)
    )


def _get_random_user():
    if not randint(0, 3):  # 1 chance out of 4
        return None
    cursor = randint(0, User.query.count() - 1)
    return User.query.offset(cursor).first().id


def generate_fake_patient():
    latest_admission = generate_patient_date()
    return dict(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        address=fake.address(),
        email=fake.email(),
        phone=fake.phone_number(),
        job=fake.job(),
        social_number=fake.ssn(),
        latest_admission=latest_admission,
        latest_medical_exam=fake.date_time_between_dates(
            datetime_start=latest_admission,
            datetime_end=datetime.datetime.now()
        ),
        id_assigned_user=_get_random_user()
    )