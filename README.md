# 🍵 Chai Order System

![Chai Banner](https://drive.google.com/uc?export=view&id=16_PpBlcL6r9YygV8mFB0pwF-AmHMHKsb)

A **modern, responsive Django web application** for tea lovers. Explore flavors, place orders, and contact the team—all in one cozy platform. ☕💛

---

## 🚀 Features

- 🌟 Browse multiple chai flavors with **beautiful images** and descriptions.
- 🛒 **Order Now** button: place orders directly into the database.
- 📱 Fully **responsive design** for mobile, tablet, and desktop.
- 📝 **Contact form** with live validation and email notifications.
- 💬 **Testimonials slider** to showcase happy customers.
- 🔗 Integrated **Django backend** with Orders and Contact models.

---

## 🖼️ Screenshots

**Hero Section**  
![Hero Section](https://drive.google.com/file/d/1Q78rcnkQsxs9d4c2O1W_ko0Rtg2eOhk6/view?usp=sharing)

**Flavors Section**  
![Chai Flavors](https://drive.google.com/file/d/1TMqAruWGIaTsfacGX6HMDhXKlpjte1MV/view?usp=sharing)

**Contact Section**  
![https://drive.google.com/file/d/1u2loSJZ4l90mXFSKVcSKry2_Z0qifoX9/view?usp=sharing)



---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Sharatpsd/chai-order-system.git
cd chai-order-system
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open in your browser: http://127.0.0.1:8000/

🗂️ Database Models
Order

flavor – Chosen chai flavor

created_at – Timestamp

Contact

name – User name

email – User email

message – User message

created_at – Timestamp

🔧 Project Structure
bash
Copy code
chaiheadq/
├─ manage.py
├─ tweet/
│  ├─ migrations/
│  ├─ static/
│  │  ├─ tweet/css/style.css
│  │  ├─ tweet/js/script.js
│  │  └─ tweet/images/
│  ├─ templates/
│  │  └─ tweet/index.html
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
├─ db.sqlite3
├─ requirements.txt
└─ README.md
🤝 Contributing
Fork the repository

Create a new branch: git checkout -b feature-name

Make changes and commit: git commit -m "Add feature"

Push your branch: git push origin feature-name

Create a pull request

📧 Contact
Created by Sharat Acharja Mugdho

GitHub: Sharatpsd

Email: sharatacharjee6@gmail.com
