<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Flask API with JWT boilerplate</h3>

  <p align="center">
    <br />
    <a href="https://github.com/quaxsze/flask-api-jwt-boilerplate/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)



<!-- ABOUT THE PROJECT -->
## About The Project

Flask API boilerplate featuring register, log in and log out using JWT authentication.


### Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Flask-migrate](https://github.com/miguelgrinberg/flask-migrate/)
* [Flask-bcrypt](https://github.com/maxcountryman/flask-bcrypt)
* [Python-JWT](https://github.com/jpadilla/pyjwt)
* [Python-dotenv](https://github.com/theskumar/python-dotenv)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The project uses Pipenv to manage requirements and uses Python 3.

### Installation
 
Clone the repo
```sh
git clone git@github.com:quaxsze/flask-api-jwt-boilerplate.git
```
Install all dependencies (including dev)
```sh
pipenv install --dev
```
Create the database or enable migrations if the database already exists
```sh
flask db init
```
Generate an initial migration
```sh
flask db migrate
```
Apply the migration
```sh
flask db upgrade
```
Run the development server
```sh
flask run
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/quaxsze/flask-api-jwt-boilerplate/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
