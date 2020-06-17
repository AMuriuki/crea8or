from app import create_app, db
from flask_script import Manager
from app.models import Gallery
import datetime
from sqlalchemy import or_

app = create_app()
manager = Manager(app)


@manager.command
def seed_and_data():
    """Create Galleries"""

    galleries = [
        Gallery(title="Advertisement", image="advertisement.jpg"),
        Gallery(title="African Painting", image="africanpainting.jpg"),
        Gallery(title="Architecture", image="architecture.jpg"),
        Gallery(title="Branding", image="branding.jpg"),
        Gallery(title="Clay Works", image="clayworks.jpg"),
        Gallery(title="Fashion", image="fashion.jp"),
        Gallery(title="Fine Arts", image="finearts.jpg"),
        Gallery(title="Illustrations", image="illustrations.jpg"),
        Gallery(title="Interior Design", image="interiordesign.jpg"),
        Gallery(title="Metal Art", image="metalart.jpg"),
        Gallery(title="Mobile App Design", image="Mobile.jpg"),
        Gallery(title="Motion Graphics", image="motion.gif"),
        Gallery(title="Photography", image="photography.jpg"),
        Gallery(title="T-Shirt Designs", image="tshirtdesigns.jpg"),
        Gallery(title="Typography", image="typography.jpg"),
        Gallery(title="Vectors", image="vectors.jpg"),
        Gallery(title="Web Design", image="webdesign.jpg"),
        Gallery(title="Wood Art", image="Woodart.jpg")
    ]
    db.session.bulk_save_objects(galleries)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
