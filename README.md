# lateshow-evelyne-joseph
# 🎙️ Late Show Guest Appearance API

A RESTful Flask API that models and manages guest appearances on the Late Show. The API allows users to retrieve episodes and guests, and manage guest appearances on different episodes with ratings.

---

## 📁 Project Structure

lateshow-evelyne-joseph/
├── app.py
├── config.py
├── models.py
├── resources.py
├── seed.py
├── migrations/
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 Features

- View all Late Show episodes
- Retrieve episode details with nested guest appearances
- View all guests
- Create guest appearances and associate them with episodes
- Validation to ensure appearance ratings are between 1–5
- Cascading deletes for appearances when episodes or guests are removed

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Flask**
- **Flask-RESTful**
- **Flask-SQLAlchemy**
- **Flask-Migrate**
- **SQLite** (for local development)
- **Postman** (for testing endpoints)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Eve-code93/lateshow-evelyne-joseph.git
cd lateshow-evelyne-joseph
2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not yet present, install manually:

bash
Copy
Edit
pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Migrate
4. Set Environment Variables
Create a .env file or set manually:

bash
Copy
Edit
export FLASK_APP=app.py
export FLASK_ENV=development
5. Initialize Database
bash
Copy
Edit
flask db init      # Only once
flask db migrate -m "Initial migration"
flask db upgrade
6. Seed the Database
bash
Copy
Edit
python seed.py
This will populate the database with episodes, guests, and appearances.

📬 API Endpoints
GET /episodes
Returns a list of all episodes.

json
Copy
Edit
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  ...
]
GET /episodes/<id>
Returns details of a single episode with all appearances and nested guest info.

json
Copy
Edit
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 10,
      "rating": 5,
      "guest_id": 1,
      "episode_id": 1,
      "episode": {
        "id": 1,
        "date": "1/11/99",
        "number": 1
      },
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
If the episode does not exist:

json
Copy
Edit
{
  "error": "Episode not found"
}
DELETE /episodes/<id>
Deletes an episode and all associated appearances.

http
Copy
Edit
204 No Content
GET /guests
Returns a list of all guests.

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  ...
]
POST /appearances
Creates a new guest appearance on a specific episode.

Request Body
json
Copy
Edit
{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
Successful Response
json
Copy
Edit
{
  "id": 20,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
}
Validation Errors
json
Copy
Edit
{
  "errors": ["rating must be between 1 and 5"]
}
🧪 Testing with Postman
Download the collection: challenge-4-lateshow.postman_collection.json

In Postman:

Click Import

Select Upload Files

Choose the JSON file

Run requests and test endpoints

✅ Validation Rules
rating must be an integer from 1 to 5

An Appearance must be associated with existing guest_id and episode_id

📌 Dev Notes
Deleting an Episode or Guest will also delete related Appearances (via cascade)

The models use .to_dict() methods with shallow nesting to avoid infinite recursion

Designed to be easily extended with authentication, pagination, or admin tools

🤝 Contributing
PRs are welcome! For major changes, open an issue first to discuss what you’d like to change.

📜 License
MIT License

👩🏽‍💻 Author
Built by Evelyne Joseph
GitHub: @Eve-code93

yaml
Copy
Edit

---
