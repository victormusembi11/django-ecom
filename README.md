# Ecommerce Project

This is a simple ecommerce project using Django.

## Virtual Environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

## Environment Variables

Create a .env file in the root directory and add the following variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

## Installation

```bash
pip install -r requirements.txt
```

## Database

```python
python manage.py migrate
```

## Usage

```python
python manage.py runserver
```

## Testing

```python
python manage.py test
```
