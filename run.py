from app import create_app, db
from app.models import User, Movie
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            password_hash=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)


    if Movie.query.count() == 0:
        movies = [
            Movie(
                title="Fight Club - მერძოლთა კლუბი",
                genre ="დრამა",
                poster="https://m.media-amazon.com/images/I/51v5ZpFyaFL._AC_.jpg",
                description="უსახელო ნარატორი აფუძნებს მებრძოლთა კლუბს, საპნის გამყიდველ ტაილერ დურდენთან ერთად."),
            Movie(
                title="Interstellar - ინტერსტელარი",
                genre="სამეცნიერო ფანტასტიკა",
                poster="https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SL1500_.jpg",
                description="ავსტრონავტების გუნდი დასასახლებელ პლანეტას ეძებს,რათა კაცობრიობამ არსებობა არ შეწყვიტოს." ),
            Movie(
                title="The Dark Knight - ბნელი რაინდი",
                genre="მძაფრსიუჟეტიანი",
                poster="https://m.media-amazon.com/images/M/MV5BMDQ5MWU2YWUtNTQ4OC00Njk5LWI0NzctMjM4OGZiNmZmNGViXkEyXkFqcGc@._V1_.jpg",
                description="ბეტმენი ქალაქ გოთემში ჯოკერს გადააწყდება..."),
            Movie(
                title="Inception - დასაწყისი",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX1000_.jpg",
                description="ქურდობა სიზმრებში და გონების მანიპულირება."
            ),
            Movie(
                title="Avengers: Endgame - ევენჯერსები: ბოლო ბრძოლა",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_FMjpg_UX1000_.jpg",
                description="მთელი Avengers-ის გუნდი ერთვება ბრძოლაში."
            ),
            Movie(
                title="Joker - ჯოკერი",
                genre="დრამა",
                poster="https://m.media-amazon.com/images/M/MV5BNzY3OWQ5NDktNWQ2OC00ZjdlLThkMmItMDhhNDk3NTFiZGU4XkEyXkFqcGc@._V1_.jpg",
                description="ბავშვობის პრობლემებით და გაუსაძლის პირობებში შექმნილი საშინელი რეალობა."
            ),
            Movie(
                title="Titanic - ტიტანიკი",
                genre="რომანტიკა",
                poster="https://m.media-amazon.com/images/I/811lT7khIrL._AC_UF1000,1000_QL80_.jpg",
                description="სიყვარული ტრაგიკულ გემზე."
            ),
            Movie(
                title="The Lord of the Rings - ბეჭდების მბრძანებელი",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BNzIxMDQ2YTctNDY4MC00ZTRhLTk4ODQtMTVlOWY4NTdiYmMwXkEyXkFqcGc@._V1_.jpg",
                description="ფროდოს მოგზაურობა ბეჭდისთვის."
            ),
            Movie(
                title="The Matrix - მატრიცა",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BN2NmN2VhMTQtMDNiOS00NDlhLTliMjgtODE2ZTY0ODQyNDRhXkEyXkFqcGc@._V1_.jpg",
                description="რეალობის სიმულაცია."
            ),
            Movie(
                title="Parasite - პარაზიტი",
                genre="დრამა",
                poster="https://s3.amazonaws.com/nightjarprod/content/uploads/sites/130/2024/03/29150816/7IiTTgloJzvGI1TAYymCfbfl3vT-scaled.jpg",
                description="ორ ოჯახს შორის სოციალური განსხვავებების რეალობა."
            ),
            Movie(
                title="La La Land - ლა ლა ლენდი",
                genre="რომანტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg",
                description="სიყვარული და კარიერა ლოს ანჯელესში."
            ),
            Movie(
                title="Forrest Gump - ფორესტ გამპი",
                genre="კომედია",
                poster="https://m.media-amazon.com/images/M/MV5BNDYwNzVjMTItZmU5YS00YjQ5LTljYjgtMjY2NDVmYWMyNWFmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                description="ფორესტ გამპის გამორჩეული ცხოვრება."
            ),
            Movie(
                title="Gladiator - გლადიატორი",
                genre="დრამა",
                poster="https://m.media-amazon.com/images/M/MV5BYWQ4YmNjYjEtOWE1Zi00Y2U4LWI4NTAtMTU0MjkxNWQ1ZmJiXkEyXkFqcGc@._V1_.jpg",
                description="გლადიატორის ბრძოლა რომის იმპერიაში."
            ),
            Movie(
                title="Avatar - ავატარი",
                genre="ფანტასტიკა",
                poster="https://lumiere-a.akamaihd.net/v1/images/p_avatar_de27b20f.jpeg",
                description="პანდორას პლანეტაზე ბრძოლა უცხოპლანეტელებთან."
            ),
            Movie(
                title="The Lion King - მეფე ლომი",
                genre="ანიმაცია",
                poster="https://m.media-amazon.com/images/M/MV5BMjIwMjE1Nzc4NV5BMl5BanBnXkFtZTgwNDg4OTA1NzM@._V1_FMjpg_UX1000_.jpg",
                description="სიმბას თავგადასავალი, რათა ლომების მეფე გახდეს."
            ),
            Movie(
                title="Black Panther - შავი პანტერა",
                genre="ფანტასტიკა",
                poster="https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg",
                description="ვაკანდას მეფე ბრძოლაში სამყაროს დასაცავად."
            ),
            Movie(
                title="Wonder Woman - ვანდერ ვუმენი",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BMjEzYmZkNjktODBmYi00NzNkLWIzMjItMjhkMWZiZTZlN2MwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                description="დიანას ბრძოლა სამართლიანობისთვის."
            ),
            Movie(
                title="Coco - კოკო",
                genre="ანიმაცია",
                poster="https://lumiere-a.akamaihd.net/v1/images/p_coco_19736_fd5fa537.jpeg?region=0%2C0%2C540%2C810",
                description="მუსიკისადმი სიყვარული და ოჯახის საიდუმლოებები."
            ),
            Movie(
                title="Soul - სული",
                genre="ანიმაცია",
                poster="https://upload.wikimedia.org/wikipedia/en/3/39/Soul_%282020_film%29_poster.jpg",
                description="ჯაზ-მუსიკოსის სული და მისი თავგადასავალიი."
            ),
            Movie(
                title="Harry Potter and the Sorcerer's Stone - ჰარი პოტერი და ფილოსოფიური ქვა",
                genre="ფანტასტიკა",
                poster="https://m.media-amazon.com/images/M/MV5BNTU1MzgyMDMtMzBlZS00YzczLThmYWEtMjU3YmFlOWEyMjE1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                description="ჰარის პირველი წელი ჰოგვორტსში, მაგია და თავგადასავალი."
            ),
            Movie(
                title="Frozen - გაყინული",
                genre="ანიმაცია",
                poster="https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_.jpg",
                description="ელზას და ანას გაყინული დობის ისტორია."
            ),
        ]

        db.session.add_all(movies)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)