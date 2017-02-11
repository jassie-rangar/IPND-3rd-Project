import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toysn that come to life",
    "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",  # noqa
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io"
)

martian = media.Movie(
    "Martian",
    "When astronauts blast off from the planet Mars, they leave behind Mark "
    "Watney (Matt Damon), presumed dead after a fierce storm. With only a "
    "meager amount of supplies, the stranded visitor must utilize his wits "
    "and spirit to find a way to survive on the hostile planet. Meanwhile, "
    "back on Earth, members of NASA and a team of international scientists "
    "work tirelessly to bring him home, while his crew mates hatch their own "
    "plan for a daring rescue mission.",
    "http://cdn-static.denofgeek.com/sites/denofgeek/files/9/72//the-martian-main.jpg",  # noqa
    "https://youtu.be/ej3ioOneTy8"
)

movies = [toy_story, avatar, martian]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
