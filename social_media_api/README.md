# Social Media API - ALX Project

## Setup

1. Clone the repo
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

## Authentication

- **Register:** `/accounts/register/`
- **Login:** `/accounts/login/`
- **Profile:** `/accounts/profile/` (Token required)

## User Model

Custom user with `bio`, `profile_picture`, and `followers`.
## Likes & Notifications

### Likes
- **Like a post:** POST `/api/posts/<post_id>/like/`
- **Unlike a post:** POST `/api/posts/<post_id>/unlike/`

### Notifications
- **View notifications:** GET `/api/notifications/`
- Notifications include new likes, comments, and followers.
