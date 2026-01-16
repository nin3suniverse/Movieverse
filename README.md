# 🎬 Movieverse

Movieverse არის ფილმების საიტი, შექმნილი **Flask (Python)**-ის გამოყენებით, რომელიც მომხმარებლებს საშუალებას აძლევს აღმოაჩინონ ფილმები, დაწერონ მიმოხილვები, შეაფასონ ისინი და შექმნან საკუთარი სანახავი ფილმების სია (Watchlist).

პროექტი შექმნილია *TBC Tech School x GeoLab* კურსის ფარგლებში  
*Web Development (Back End: Python)*.

---

## 🌐 ფუნქციონალი

### 👤 მომხმარებლები
- რეგისტრაცია და ავტორიზაცია
- პირადი პროფილის გვერდი
- საკუთარი ფილმების და მიმოხილვების ნახვა

### 🎞 ფილმები
- ფილმების დამატება ავტორიზებული მომხმარებლების მიერ
- ფილმების დეტალური გვერდი
- ჟანრების მიხედვით ფილმების გაფილტვრა
- ფილმის წაშლა:
  - ადმინის მიერ
  - ან ფილმის ავტორის მიერ

### ✍️ მიმოხილვები
- ფილმებზე მიმოხილვების დაწერა
- ვარსკვლავებით შეფასება (რეიტინგი)
- მიმოხილვის წაშლა:
  - მიმოხილვის ავტორის მიერ
  - ან ადმინის მიერ

### ⭐ სანახავი ფილმების სია (Watchlist)
- ფილმის დამატება სანახავ სიაში
- ფილმის წაშლა სანახავი სიიდან
- ცალკე Watchlist გვერდი

### 🔐 ადმინის ფუნქციები
- ფილმების წაშლა
- მიმოხილვების წაშლა
- დამატებითი კონტროლი კონტენტზე

---

## 🛠 გამოყენებული ტექნოლოგიები

- *Python 3*
- *Flask*
- *Flask-SQLAlchemy*
- *Flask-Login*
- *SQLite*
- *HTML5 / Jinja2*
- *CSS3*
- *Bootstrap 5*
- *Swiper.js* (სლაიდერები)

---

## 🧱 მონაცემთა ბაზის სტრუქტურა (მოკლედ)

- *User*
  - id
  - username
  - password_hash
  - is_admin
- *Movie*
  - id
  - title
  - genre
  - poster
  - user_id
- *Review*
  - id
  - text
  - rating
  - user_id
  - movie_id
- *Watchlist*
  - user_id
  - movie_id

---

## 📁 პროექტის სტრუქტურა

app/
├── init.py
├── models.py
├── routes.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── movies.html
│   ├── movie_detail.html
│   ├── profile.html
│   ├── watchlist.html
│   └── …
├── static/
│   ├── css/
│   └── imag

---

## ▶️ ლოკალურად გაშვება

### 1️⃣ რეპოზიტორიის დაკლონვა
```bash
git clone https://github.com/nin3suniverse/Movieverse.git
cd movieverse

2️⃣ ვირტუალური გარემოს შექმნა

python -m venv venv
source venv/bin/activate

3️⃣ საჭირო პაკეტების დაყენება

pip install -r requirements.txt

4️⃣ აპლიკაციის გაშვება
flask run
 

ავტორი - ნინო მელიქიშვილი / Nino Melikishvili

Movieverse Project
© 2026

⸻

🎥 Movieverse — Discover. Review. Save./ აღმოაჩინე. შეაფასე. შეინახე
