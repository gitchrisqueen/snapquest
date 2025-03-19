Here’s a **README.md** file for your **SnapQuest** project:

---

### **`README.md` - SnapQuest 📸🔍**
# SnapQuest: A Location-Based Picture Hunt Game

**SnapQuest** is an interactive **SMS-based scavenger hunt game** where players receive location-based riddles, find real-world locations, and submit photos for verification. Built with **FastAPI, MySQL, Twilio, and AI-powered riddle generation**, SnapQuest makes real-world exploration fun and competitive.

---

## 🚀 **Features**
✅ **SMS-Based Gameplay** – Receive riddles and submit answers via text  
✅ **AI-Generated Riddles** – Dynamically created challenges for each location  
✅ **Image Verification** – Check if submitted photos match expected locations  
✅ **Game Code System** – Players join challenges using unique game codes  
✅ **MySQL Backend** – Tracks users, submissions, and progress  
✅ **Fully Dockerized** – Easy setup and deployment  

---

## 📜 **How It Works**
1️⃣ **Sign up with your phone number** via SMS  
2️⃣ **Receive a verification code** via Twilio and confirm your number  
3️⃣ **Join or create a game** with a unique code  
4️⃣ **Get location-based riddles** via SMS  
5️⃣ **Visit the location and submit a photo**  
6️⃣ **AI verifies your submission** – Get a ✅ for correct or ❌ for incorrect answers  
7️⃣ **Complete all locations to win!** 🎉  

---

## 🔧 **Tech Stack**
- **Backend:** FastAPI (Python)
- **Database:** MySQL (SQLAlchemy + Alembic)
- **Messaging:** Twilio SMS API
- **Image Processing:** AI-powered verification (Google Vision API in future)
- **Containerization:** Docker & Docker Compose
- **Dependency Management:** Poetry

---

## 📥 **Installation & Setup**
### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/snapquest-game.git
cd snapquest-game
```

### **2. Install Dependencies with Poetry**
```sh
poetry install
```

### **3. Setup Database & Migrations**
```sh
docker-compose up -d
poetry run alembic upgrade head
```

### **4. Run the App**
```sh
poetry run uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### **5. Access the API**
📍 Open **http://localhost:8000/docs** for interactive API documentation.

---

## 📩 **Opt-In Story for Twilio SMS**
To participate in SnapQuest, users must **opt-in** by signing up with their phone number.  
1. The player **texts "JOIN"** to the SnapQuest Twilio number.  
2. They receive an **SMS verification code** to confirm their identity.  
3. Once verified, they can **receive game messages, riddles, and submission confirmations**.  
4. Players can opt-out anytime by texting **"STOP"**, which **immediately halts all game messages**.  

✅ **SnapQuest strictly adheres to SMS best practices, ensuring user privacy and consent.**  

---

## 🛠 **API Endpoints**
| Method | Endpoint | Description |
|--------|------------|--------------------------------|
| `POST` | `/register/` | Register a new player |
| `POST` | `/create_game/` | Create a new game |
| `POST` | `/add_location/` | Add locations to a game |
| `POST` | `/start_game/` | Send riddle to player |
| `POST` | `/submit_image/` | Submit a photo for verification |

Full API docs available at: **`/docs`** 📜

---

## 🏗 **Contributing**
Interested in contributing? Please follow these steps:
1. **Fork** the repository  
2. **Create a new branch** (`feature/new-feature`)  
3. **Commit your changes**  
4. **Push to your branch and submit a PR**  

---

## 📄 **License**
SnapQuest is licensed under the **MIT License**. See `LICENSE` for details.

---

### 🎯 **Join the Adventure with SnapQuest!**
🌎 Solve riddles.  
📸 Capture the moment.  
🏆 Win the game.  

Let’s **play SnapQuest!** 🚀  

---

This README provides **all key information** about SnapQuest, including:
- **Project overview**
- **Features & installation**
- **Twilio opt-in story**
- **API documentation**
- **Contribution guide**

