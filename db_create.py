from app import db
from models import BlogPost

db.create_all()

#insert
db.session.add(BlogPost("GOOD", "I\'m good."))
db.session.add(BlogPost("GOOD", "I\'m well."))

#commit changes
db.session.commit()