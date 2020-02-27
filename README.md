# Install:
- pip install -r requirements.txt
- python manage.py migrate

# Setup:
- python manage.py runserver 8000

# Configure:
- localhost:8000/admin/

# Test:
- http -v localhost:8000/experiments/
- http -v localhost:8000/groups/ idfa==123
