# KidzBookHub 📚

A lightweight Django application that lets students browse and download educational books organized by grade/standard and subject.

## Features

- 📖 Browse books by grade level and subject
- 📥 Download PDF educational materials
- 🖼️ View book covers and metadata
- 🔍 Filter and search functionality
- 🌐 Public access - no authentication required

## Tech Stack

- **Framework:** Django 5.x
- **Database:** SQLite (development) / PostgreSQL (production recommended)
- **Frontend:** HTML, CSS, Bootstrap
- **Media Storage:** Local filesystem (development) / Cloud storage (production)

## Project Structure

```
kidzbookhub/          # Django project settings
courses/              # Main app: books, models, views
templates/            # HTML templates
static/               # CSS, JavaScript, images
media/                # Uploaded book PDFs and covers
manage.py             # Django CLI
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/tanish-chopra/kidzbookhub.git
cd kidzbookhub
```

2. **Create a virtual environment**

```bash
python -m venv .venv

# On Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install django pillow django-widget-tweaks
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

6. **Access the application**

Open your browser and go to: `http://127.0.0.1:8000/`

## Usage

### Admin Panel

Create a superuser to access the admin panel and manage books:

```bash
python manage.py createsuperuser
```

Then access: `http://127.0.0.1:8000/admin/`

### Adding Books

1. Login to the admin panel
2. Navigate to "Books" under the Courses section
3. Add book details: title, grade, subject, PDF file, cover image
4. Save and publish

## Configuration

### Environment Variables

For production, set these environment variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Your domain name
- `DATABASE_URL` - Production database connection string

### Media Files

- Book PDFs and covers are stored in `media/` directory
- For production, use cloud storage (AWS S3, Azure Blob, etc.)

### Static Files

For production deployment:

```bash
python manage.py collectstatic
```

## Testing

Run the test suite:

```bash
python manage.py test
```

## Deployment

### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Set up PostgreSQL or MySQL database
- [ ] Configure static file serving (WhiteNoise or CDN)
- [ ] Set up media file storage (S3, Azure Blob)
- [ ] Use HTTPS/SSL certificates
- [ ] Configure WSGI server (Gunicorn, uWSGI)
- [ ] Set up reverse proxy (Nginx, Apache)

### Deployment Options

- **Heroku:** Use the provided `Procfile`
- **AWS/Azure:** Deploy with Elastic Beanstalk or App Service
- **DigitalOcean:** Use App Platform or Droplets
- **Docker:** Containerize with the included Dockerfile (if provided)

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows Django best practices and includes appropriate tests.

## Security

⚠️ **Important Security Notes:**

- Never commit `SECRET_KEY` or credentials to version control
- Rotate secrets if accidentally committed
- Use `.gitignore` to exclude sensitive files
- Keep dependencies updated for security patches

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Designed for educational accessibility
- Community contributions welcome

---

**Note:** This application provides public access to educational materials without requiring user authentication.

