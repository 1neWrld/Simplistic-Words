# 📝 Personal Blog (Flask)

 **Blog Link**: [Line of Progress](https://line-of-progress-personal-blog.onrender.com/)

A full-featured personal blog web application built with Flask.
This project allows users to create, read, update, and delete blog posts through a clean web interface.
Posts are stored in a SQLite database with features like user authentication, password hashing,
post timestamps, and a modern responsive design following MVC architecture patterns.

## 🌐 Deployment

- **Render** - Free tier, easy Flask deployment

## 📌 Features

- **User Authentication System**
  - Secure registration with password hashing (bcrypt)
  - Login/logout functionality
  - Session management with Flask-Login
  - Protected routes - only authenticated users can create/edit/delete posts

- **Blog Post Management**
  - Create posts with title and content
  - Edit existing posts
  - Delete posts with confirmation
  - View individual post details
  - Auto-generated timestamps (created & updated)

- **User Experience**
  - Clean, modern, minimal design inspired by PaperMod theme
  - Responsive layout for all devices
  - Social media links (GitHub, LinkedIn, Email)
  - Category tags for content organization
  - Flash messages for user feedback
  - Author attribution on posts

- **Data Persistence**
  - SQLite database storage
  - SQLAlchemy ORM for database operations
  - User-post relationships (one-to-many)
  - Automatic database initialization

## 🛠️ Tech Stack

**Backend:** Python 3.11, Flask 3.x  
**Database:** SQLite with SQLAlchemy ORM  
**Authentication:** Flask-Login, Flask-Bcrypt  
**Forms:** Flask-WTF, WTForms  
**Frontend:** HTML5, CSS3, Jinja2 templating  
**Tools:** PyCharm IDE, Git  
**Version Control:** Git & GitHub

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/1neWrld/simplistic-words-blog.git
cd simplistic-words-blog
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

### 3. Activate the virtual environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python app.py
```

### 6. Open in browser
Navigate to `http://127.0.0.1:5000`

## 📂 Project Structure

```
simplistic-words-blog/
│
├── app.py                      # Main application entry point & routes
├── model.py                    # Database models (User, Post)
├── forms.py                    # Form classes with validation
├── database.py                 # Database configuration & session management
│
├── templates/                  # HTML templates (Jinja2)
│   ├── home.html              # Landing page with post listings
│   ├── post.html              # Individual post view
│   ├── create_post.html       # Post creation form
│   ├── edit_post.html         # Post editing form
│   ├── about.html             # About page
│   ├── login.html             # User login form
│   └── register.html          # User registration form
│
├── static/                     # Static assets (optional)
│   ├── css/
│   ├── images/
│   └── js/
│
├── blog.db                     # SQLite database (auto-generated)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 💡 Usage

### First Time Setup
1. **Register an account:**
   - Go to `/register`
   - Create your admin account with username, email, and password
   - After registration, you can disable the register route for security

2. **Login:**
   - Navigate to `/login`
   - Enter your credentials
   - You'll be redirected to the home page

### Creating Posts
```
1. Click "Create Post" in the navigation (only visible when logged in)
2. Enter a title (2-100 characters)
3. Write your post content (minimum 10 characters)
4. Click "Publish Post"
5. Post appears on the home page immediately
```

### Editing Posts
```
1. Click on a post to view it
2. Click "Edit" button (only visible to post author)
3. Modify title or content
4. Click "Publish Post" to save changes
```

### Deleting Posts
```
1. View the post you want to delete
2. Click "Delete" button (only visible to post author)
3. Confirm deletion in the popup
4. Post is permanently removed
```

## 🏗️ Architecture

This project follows the **MVC (Model-View-Controller)** pattern with Flask best practices:

- **Models** (`model.py`): Database schema definitions
  - `User`: User accounts with authentication
  - `Post`: Blog posts with relationships to users

- **Views** (`templates/`): HTML templates with Jinja2
  - Responsive design
  - Template inheritance for consistency
  - Dynamic content rendering

- **Controllers** (`app.py`): Route handlers and business logic
  - User authentication flows
  - CRUD operations for posts
  - Session management
  - Form validation

- **Forms** (`forms.py`): Input validation and sanitization
  - `PostForm`: Blog post creation/editing
  - `LoginForm`: User authentication
  - `RegistrationForm`: New user accounts

- **Database** (`database.py`): Data persistence layer
  - SQLAlchemy session management
  - Database initialization
  - Scoped sessions for thread safety

## 🔐 Security Features

- ✅ Password hashing with bcrypt
- ✅ CSRF protection on all forms
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ Session-based authentication
- ✅ Protected routes with `@login_required` decorator
- ✅ Author-only access for edit/delete operations

## 🎨 Design Inspiration

The visual design and layout of this blog were inspired by the clean, minimal aesthetic of the [PaperMod theme](https://www.htmly.com/theme/papermod), adapted for a Flask application with custom styling.

## 🔮 Future Enhancements

- [ ] Pagination for blog posts
- [ ] Search functionality
- [ ] Comment system
- [ ] Rich text editor (Markdown support)
- [ ] Image uploads for posts
- [ ] Tags and categories filtering
- [ ] RSS feed generation
- [ ] Dark mode toggle
- [ ] Post drafts functionality
- [ ] SEO optimization
- [ ] Social media sharing buttons
- [ ] Analytics dashboard


## 🙋‍♂️ Author

**Wandipa Marema**  
🎓 Computer and Information Sciences  
💻 Passionate about Python  
🌍 GitHub: [@1neWrld](https://github.com/1neWrld)  
💼 LinkedIn: [Wandipa Marema](https://www.linkedin.com/in/wandipa-marema-b2771a308/)  
📧 Email: wandipamarema@icloud.com

## 🔗 Project Resources

- **Theme Reference**: [PaperMod for HTMLy](https://www.htmly.com/theme/papermod)
- **Design Software**: [Draw.io](https://app.diagrams.net/)

## 📄 License

This project is open source and available for educational purposes.

---

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**
