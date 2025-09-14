# Daria's Digest

A simple blogging site built with Flask backend and vanilla HTML, CSS, and JavaScript frontend.

## Project Structure

```
dariasdigest/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker container configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker ignore file
├── templates/            # HTML templates
│   ├── base.html        # Base template with common layout
│   ├── home.html        # Home page template
│   ├── blog.html        # Blog listing page template
│   └── article.html     # Individual article page template
├── static/               # Static assets
│   ├── style.css        # CSS styles for all pages
│   └── script.js        # JavaScript functionality
└── README.md            # This file
```

## Features

- **Home Page**: Clean landing page with "Daria's Digest" title and navigation to blog
- **Blog Listing**: Displays article cards with title, description, image, and date
- **Article View**: Full article page with Lorem ipsum content
- **Responsive Design**: Mobile-friendly layout
- **Smooth Navigation**: JavaScript-enhanced user interactions

## File Descriptions

### Backend Files

- **`app.py`**: Main Flask application containing:
  - Route handlers for home (`/`), blog (`/blog`), and article (`/article/<id>`) pages
  - Sample article data with Lorem ipsum content
  - Template rendering logic

- **`requirements.txt`**: Lists Python dependencies (Flask 2.3.3)

### Frontend Files

- **`templates/base.html`**: Base template providing common HTML structure, CSS, and JavaScript includes

- **`templates/home.html`**: Home page template with centered title and blog navigation button

- **`templates/blog.html`**: Blog listing page showing article cards with click functionality

- **`templates/article.html`**: Individual article page with title, date, image, and content

- **`static/style.css`**: Comprehensive CSS styling including:
  - Responsive grid layout for article cards
  - Hover effects and animations
  - Mobile-responsive design
  - Clean typography and color scheme

- **`static/script.js`**: JavaScript functionality for:
  - Article navigation
  - Button click animations
  - Page load animations
  - Enhanced user interactions

### Containerization Files

- **`Dockerfile`**: Multi-stage Docker configuration for production deployment

- **`docker-compose.yml`**: Simple Docker Compose setup for easy container management

- **`.dockerignore`**: Excludes unnecessary files from Docker build context

## Running Locally

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup and Run

1. **Clone or navigate to the project directory**:
   ```bash
   cd dariasdigest
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the site**:
   Open your browser and go to `http://localhost:8000`

### Navigation

- **Home Page** (`/`): Landing page with site title and blog button
- **Blog Page** (`/blog`): Click the "blog" button to see the article listing
- **Article Page** (`/article/1`): Click on any article card to view the full article

## Containerization

### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t darias-digest .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 darias-digest
   ```

3. **Access the site**:
   Open your browser and go to `http://localhost:8000`

### Using Docker Compose (Recommended)

1. **Start the application**:
   ```bash
   docker-compose up -d
   ```

2. **View logs** (optional):
   ```bash
   docker-compose logs -f
   ```

3. **Stop the application**:
   ```bash
   docker-compose down
   ```

4. **Access the site**:
   Open your browser and go to `http://localhost:8000`

## Development

### Adding New Articles

To add new articles, modify the `ARTICLES` list in `app.py`:

```python
ARTICLES = [
    {
        'id': 1,
        'title': 'Article Title',
        'description': 'Brief description',
        'image': 'https://example.com/image.jpg',
        'date': datetime(2024, 1, 15),
        'content': 'Full article content...'
    },
    # Add more articles here
]
```

### Customizing Styles

Modify `static/style.css` to change the appearance:
- Colors are defined using CSS custom properties
- Responsive breakpoints are set for mobile devices
- Grid layout can be adjusted for different article card arrangements

### Adding JavaScript Features

Extend `static/script.js` to add:
- More interactive animations
- AJAX functionality for dynamic content loading
- Form handling for user interactions

## Production Considerations

- The current setup uses Flask's built-in development server
- For production deployment, consider using a WSGI server like Gunicorn
- Add environment variables for configuration management
- Implement proper error handling and logging
- Add database integration for dynamic article management

## License

This project is created for educational purposes.