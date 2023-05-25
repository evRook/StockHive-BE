# StockHive Backend

### This README provides an overview of the Django backend and PostgreSQL database setup. The project contains routes for retrieving user details, company information, ticker list, and historical data. Below, you will find instructions on how to set up and use the backend.

<br/>

### Instalation:

1. Fork and Close this repository
2. Install dependencies:

```
$ pip install -r requirements.txt
```

3. Create a PostgreSQL database

<br/>

### Configuration:

1. Open the project in your text editor
2. In the projects settings(`settings.py`), configure the database settings to connect to your PostgreSQL database. Update the following settings:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host'
    }
}
```

3. Apply database migrations:

```
$ python3 manage.py migrate
```

4. Start the Django development server:

```
$ python3 manage.py runserver
```

<br/>


## Routes:

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `users/` | Show current Users | 
| `GET` | `company/{Ticker}` | Company Info by Ticker Symbol |
| `GET` | `ticker` | List of popular Ticker Symbols |
| `GET` | `history/{Ticker}/{Duration}` | List Historical Data for a Company by Ticker Symbol |

### Djoser Authentication:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/auth/users/` | Create New User from Form Data | 
| `POST` | `/auth/users/activation/` | Verify New User |
| `POST` | `auth/jwt/create/` | Creates JWT for Verified User Login |
| `POST` | `auth/users/reset_password/` | Send User an Email for Password Reset Request |
| `POST` | `auth/users/reset_password_confirm/` | Updates Current Users Password |

<br/>

## Built With:

![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)

![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

![image](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)


## Later Additions:
- User favorites.
- AI Predictions

## Contributions

### Contributions to the project are welcome! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

- [Deployed Render App](https://stockhive-be.onrender.com/ticker)
- [Repository](https://github.com/evRook/StockHive-BE)
- [Issue Tracker](https://github.com/evRook/StockHive-BE/issues)




<br/>

### Author:


![Your Repository's Stats](https://contrib.rocks/image?repo=evRook/StockHive-FE) [evRook](https://github.com/evRook) | Eric Spychalski