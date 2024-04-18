from django.core.cache import cache
from django.contrib.auth.models import User

USERS_CACHE_KEY = 'users_cache'


def cache_all_books():
    all_users = User.objects.all()
    cache.set(USERS_CACHE_KEY, list(all_users))


def get_cached_books():
    return cache.get(USERS_CACHE_KEY)