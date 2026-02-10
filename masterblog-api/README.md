# 📚 Masterblog API

A Flask REST API and simple web frontend for managing blog posts. The backend exposes CRUD endpoints with sorting and search; the frontend lets you add, list, delete, and configure the API base URL. Run backend and frontend separately and connect via the configurable API URL.

## ✨ Features

- **REST API**: List posts (with optional sort by `title` or `content`), search by title/content, add, update, and delete posts
- **Configurable API URL**: Enter the backend base URL in the UI; it’s stored in `localStorage` for the next visit
- **Simple UI**: Load posts, add new posts, and delete posts from a single page
- **CORS-enabled backend**: Flask app configured with CORS for cross-origin requests from the frontend
- **Responsive layout**: Styling in `frontend/static/styles.css` with Poppins font

## 🚀 Getting Started

**Backend (API)**

Create a virtual environment and install dependencies (use `python3` on macOS/Linux):

```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install flask flask-cors
```

Run the API server:

```
cd backend
python3 backend_app.py
```

The API runs at `http://127.0.0.1:5002` (or `http://0.0.0.0:5002` when bound to all interfaces).

**Frontend**

In another terminal:

```
cd frontend
python3 frontend_app.py
```

Open `http://127.0.0.1:5002` in your browser. The default API base URL is `http://127.0.0.1:5002/api`; use **Load Posts** to fetch and display posts.

## 🗂️ Project Structure

- `backend/backend_app.py`: Flask app — GET/POST/PUT/DELETE for `/api/posts`, search at `/api/posts/search`, sort via query params
- `frontend/frontend_app.py`: Flask app that serves the blog UI (routes render `index.html`)
- `frontend/templates/index.html`: Main page with API URL input, add-post form, and post list container
- `frontend/static/main.js`: Fetch calls to load, add, and delete posts; persists API base URL in `localStorage`
- `frontend/static/styles.css`: Global styles for the blog UI

## 🎮 How to Use

1. Start the **backend** (`backend/backend_app.py`) and the **frontend** (`frontend/frontend_app.py`) as above.
2. In the browser, confirm or set the **API Base URL** (e.g. `http://127.0.0.1:5002/api`).
3. Click **Load Posts** to fetch and display posts from the API.
4. Use the title and content fields and **Add Post** to create a new post.
5. Click **Delete** on a post to remove it via the API; the list refreshes after each action.

## 🛠️ Customization

- Change the in-memory `POSTS` list or add persistence (e.g. JSON file or database) in `backend/backend_app.py`.
- Add or change sort fields and search logic in the backend routes.
- Adjust default API URL, layout, or styles in `frontend/templates/index.html` and `frontend/static/styles.css`.
- Extend `frontend/static/main.js` to support update (PUT) from the UI if desired.

## 🧰 Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML, CSS (Poppins from Google Fonts), vanilla JavaScript (Fetch API)
- **API**: REST (JSON); in-memory storage for posts
