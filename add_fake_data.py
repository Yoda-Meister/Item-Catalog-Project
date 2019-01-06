from database_setup import Component, Base, Part, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///pcpart.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

# Create dummy user
user1 = User(
    name='Peesee Hellpar',
    email='southguy@live.co.uk',
    picture='https://pbs.twimg.com/media/DUp-1VMX0AEGw4-.jpg'

)

session.add(user1)
session.commit()

component1 = Component(
    name='GPU',
    user=user1
)

session.add(component1)
session.commit()

part1 = Part(
    name='GTX 2080 Ti',
    description='It is one of the most powerful graphics card to ever exist. Your PC will love you for installing it!',
    component=component1,
    user=user1
)

session.add(part1)
session.commit()

part2 = Part(
    name='GTX 1080 Ti',
    description='An incredibly powerful graphics card. Powerful enough to handle anything you throw at it!',
    component=component1,
    user=user1
)

session.add(part2)
session.commit()

part3 = Part(
    name='GTX 1060',
    description='A decently powerful graphics card. Will get you by for a while without any complaints!',
    component=component1,
    user=user1
)

session.add(part3)
session.commit()

print('Added the data!')
