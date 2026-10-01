from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Define the Declarative Base and User Model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Establish database engine and session factory
engine = create_engine('mysql+mysqlconnector://root:yourpassword@localhost/example_db')
Session = sessionmaker(bind=engine)

def init_db():
    """Create tables in the database using SQLAlchemy metadata."""
    Base.metadata.create_all(engine)

def create_user(session, username, email):
    """Create a new user using the ORM session."""
    if not username or not email:
        print("Username and email are required.")
        return
    try:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        print(f"User '{username}' created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating user: {e}")

def get_user_by_username(session, username):
    """Retrieve a user object by username using the ORM query API."""
    return session.query(User).filter_by(username=username).first()

def update_user_email(session, username, new_email):
    """Update a user's email using the ORM session."""
    try:
        user = session.query(User).filter_by(username=username).first()
        if user:
            user.email = new_email
            session.commit()
            print(f"User '{username}' email updated successfully.")
        else:
            print(f"User '{username}' not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating user: {e}")

def delete_user(session, username):
    """Delete a user using the ORM session."""
    try:
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting user: {e}")

def list_users(session):
    """List all users using the ORM session."""
    return session.query(User).all()
