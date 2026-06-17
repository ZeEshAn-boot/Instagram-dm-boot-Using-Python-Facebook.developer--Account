# 🍽️ ZAIQA Restaurant - Instagram DM Automation Bot

An AI-powered Instagram chatbot for ZAIQA Restaurant built using **Python**, **Flask**, **Meta Instagram Messaging API**, and **Groq AI**. The bot automatically responds to customer inquiries regarding menu items, pricing, reservations, delivery, payment methods, and order tracking.

## 🚀 Features

* 🤖 AI-powered responses using Groq API
* 📩 Automatic Instagram DM replies
* 🍛 Menu and pricing information
* 🚚 Delivery information and tracking
* 📅 Table reservation support
* 💳 Payment method assistance
* ⏰ Opening hours information
* 🎉 Special deals and promotions
* 🔍 Order status tracking
* 🌐 Multi-language support (English, Urdu & Roman Urdu)

## 🛠️ Tech Stack

* Python 3
* Flask
* Meta Graph API
* Instagram Messaging API
* Groq API (LLaMA Models)
* ngrok
* Requests
* python-dotenv

## 📂 Project Structure

```bash
zaiqa-bot/
│
├── app.py              # Main Flask application
├── responses.py        # AI response logic
├── .env                # Environment variables
├── requirements.txt    # Project dependencies
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/zaiqa-bot.git
cd zaiqa-bot
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file:

```env
ACCESS_TOKEN=your_meta_access_token
VERIFY_TOKEN=your_verify_token
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run Application

Start Flask:

```bash
python app.py
```

Start ngrok:

```bash
ngrok http 5000
```

Use:

```text
https://your-ngrok-url/webhook
```

as the Meta Webhook Callback URL.

## 🔄 Workflow

Instagram User → Meta Webhook → Flask Backend → Groq AI → Automated Response → Instagram User

## 📌 Current Status

✅ Meta App Configured
✅ Instagram Business Connected
✅ Webhook Verified
✅ Groq AI Integrated
✅ AI Responses Working
✅ Test Instagram Account Working

⚠️ Public deployment and full Instagram access depend on Meta App Review and permission approval.

## 📷 Demo

A complete demo video showcasing the Instagram DM flow is available in the repository.

## 👨‍💻 Author

**Muhammad Zeeshan**

LinkedIn: https://www.linkedin.com/in/muhammad-zeeshan-1a9b32261/

---

⭐ If you like this project, don't forget to star the repository!
