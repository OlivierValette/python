# -*- coding: utf-8 -*-
import peewee
import datetime

db = peewee.SqliteDatabase("courses.db3")


class Artist(peewee.Model):
    """
    ORM Model of the Artist table
    """
    name = peewee.CharField()

    class Meta:
        database = db


class Album(peewee.Model):
    title = peewee.CharFiled()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharFiled()
    media_type = peewee.CharFiled()
    artist = peewee.ForeignKeyField(Artist)

    class Meta:
        database = db


# si fichier "main" (fichier d'amorçage)
if __name__ == "__Main__":
    try:
        Artist.create_table()
    except peewee.OperationalError:
        print("Table already exists")


# create new artist
new_artist = Artist.create(name="Newsboys")

# create new album
album_one = Album(artist=new_artist,
                  title="Read All About It",
                  release_date=datetime.date(1988, 12, 1),
                  publisher="Refuge",
                  media_type="CD")
# save in database both new artist and new album
album_one.save()

# create multiple albums
albums = [
    { "artist": new_artist,
      "title":...

    },
    {"artiste": ...

    }]
for album in albums:
    a = Album(**album)
    a.save()

# create multiple artists
bands = ["MXPX", "Kutless", "lu"]
for band in bands:
    artist = Artist.create(name=band)
    artist.save()

# queries
albums = Album.get()
album = Album.get(Album.title == "Hell is for Wimps")

# join
albums = Album.select().join(Artist).where(Artist.name == "Newsboys")
for album in albums:
    print(album.title)

# delete
band = Artist.get(Artist.name == "")
