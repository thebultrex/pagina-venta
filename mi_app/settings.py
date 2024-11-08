INSTALLED_APPS = [
    
    'corsheaders',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # URL de tu aplicación React
]