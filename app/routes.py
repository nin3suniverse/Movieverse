from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Movie, Review
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

@main.route("/")
def index():
    new_movies = Movie.query.order_by(Movie.created_at.desc()).limit(12).all()
    latest_reviews = Review.query.order_by(Review.created_at.desc()).limit(10).all()

    return render_template(
        "index.html",
        new_movies=new_movies,
        latest_reviews=latest_reviews
    )


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("სახელი უკვე დაკავებულია")
            return redirect(url_for("main.register"))

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        flash("თქვენ წარმატებით შექმენით ანგარიში")
        return redirect(url_for("main.login"))

    return render_template("register.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("ყველა ველი სავალდებულოა")
            return redirect(url_for("main.login"))

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("თქვენ წარმატებით შეხვედით!")
            return redirect(url_for("main.index"))
        else:
            flash("სახელი ან პაროლი არასწორია")
            return redirect(url_for("main.login"))

    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))




@main.route("/add_movie", methods=["GET", "POST"])
@login_required
def add_movie():
    genres=sorted(list({movie.genre for movie in Movie.query.all()}))
    if request.method == "POST":
        title = request.form["title"]
        genre = request.form["genre"]
        poster = request.form["poster"]
        description = request.form.get("description")
        if not title or not genre or not poster or not description:
            flash("ყველა ველი სავალდებულოა", "danger")
            return redirect(url_for("main.add_movie"))
        movie = Movie(title=title, genre=genre, poster=poster, user_id=current_user.id, description=description)
        db.session.add(movie)
        db.session.commit()
        flash("ფილმი დაემატა", "success")
        return redirect(url_for("main.index"))
    return render_template("add_movie.html", genres=genres)


@main.route("/delete_movie/<int:movie_id>", methods=["POST"])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if not (current_user.is_admin or movie.user_id == current_user.id):
        abort(403)

    for r in movie.reviews:
        db.session.delete(r)
    db.session.delete(movie)
    db.session.commit()
    flash("ფილმი წაიშალა", "success")
    return redirect(request.referrer or url_for("main.index"))



@main.route("/delete_review/<int:review_id>", methods=["POST"])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    if current_user.is_admin or review.user_id == current_user.id:
        db.session.delete(review)
        db.session.commit()
        flash("მიმოხილვა წაიშალა", "success")
        return redirect(request.referrer or url_for("main.index"))
    abort(403)


@main.route("/movies")
def movies():
    search = request.args.get("search", "").strip()
    genre_filter = request.args.get("genre")

    movies_query = Movie.query

    if search:
        movies_query = movies_query.filter(
            Movie.title.ilike(f"%{search}%")
        )

    if genre_filter:
        movies_query = movies_query.filter(
            Movie.genre == genre_filter
        )

    movies_list = movies_query.all()

    genres = sorted({movie.genre for movie in Movie.query.all()})

    return render_template(
        "movies.html",
        movies=movies_list,
        genres=genres,
        search=search
    )
@main.route("/profile")
@login_required
def profile():
    user_reviews = current_user.reviews
    my_movies = Movie.query.filter_by(user_id=current_user.id).all()

    return render_template("profile.html", user=current_user, reviews=user_reviews, my_movies=my_movies)


@main.route("/movie/<int:movie_id>")
@login_required
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    reviews = Review.query.filter_by(movie_id=movie.id).all()
    in_watchlist = current_user.watchlist.filter_by(id=movie.id).first() is not None
    return render_template("movie_detail.html", movie=movie, reviews=reviews, in_watchlist=in_watchlist)


@main.route("/add_review/<int:movie_id>", methods=["GET", "POST"])
@login_required
def add_review(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    rating = request.form.get("rating")
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("მიმოხილვა და შეფასება სავალდებულოა!", "danger")
            return redirect(url_for("main.add_review", movie_id=movie.id))

        review = Review(text=text, movie_id=movie.id, user_id=current_user.id, rating=int(rating))
        db.session.add(review)
        db.session.commit()
        flash("მიმოხილვა წარმატებით დაემატა!", "success")
        return redirect(url_for("main.movie_detail", movie_id=movie.id))

    return render_template("add_review.html", movie=movie)

@main.route('/watchlist')
@login_required
def watchlist():
    watchlist_movies = current_user.watchlist  # User მოდელში უნდა ჰქონდეს relationship
    return render_template('watchlist.html', watchlist=watchlist_movies)

@main.route('/add_to_watchlist/<int:movie_id>', methods=['POST'])
@login_required
def add_to_watchlist(movie_id):
    print ("WATCHLIST ROUTE HIT")
    movie = Movie.query.get_or_404(movie_id)
    if movie not in current_user.watchlist:
        current_user.watchlist.append(movie)
        db.session.commit()
        flash('ფილმი დაემატა სანახავში!', 'success')
    return redirect(url_for('main.movie_detail', movie_id=movie.id))

@main.route('/remove_from_watchlist/<int:movie_id>', methods=['POST'])
@login_required
def remove_from_watchlist(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if movie in current_user.watchlist:
        current_user.watchlist.remove(movie)
        db.session.commit()
        flash('ფილმი წაიშალა სანახავიდან!', 'success')
    return redirect(url_for('main.movie_detail', movie_id=movie.id))