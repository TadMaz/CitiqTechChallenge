from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('sqlite:///:memory:', echo=True)
# DEFINE ENGINE 


Base = declarative_base()
Session = sessionmaker(bind=engine)
session:Session = Session()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50))
    name = Column(String(50))
    surname = Column(String(50))
    password = Column(String(50))
    groupID = Column(String(50))
    
    
    def __init__(self, username, name, surname, password, group_id):
        
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.password = password
        self.group_id = group_id

    @classmethod
    def authenticate(cls, data: dict):
        
        user = session.query(User).filter_by(username=data["username"]).one()
        if (user):
             
            if user.password == data["password"]:
                return True

        return False

    @classmethod
    def get_user(cls ,data:dict):

        user = session.query(User).filter_by(postID = data["ID"])
        
        user_dict = {"id": user.id, "username" : user.username, "name" : user.name,
                     "password" : user.password, "age" : user.age, 
                     "groupID": user.group_id }
        
        return user_dict

    @classmethod
    def add_user(cls, data:dict):

        user = User(data.pop("username"), data.pop("name"), data.pop("surname"),
                    data.pop("password"), data.pop("group_id", None))

        session.add(user)
        session.commit()

    @classmethod
    def delete_user (cls, data:dict):

        user = session.query(User).filter_by(ID = data["id"])

        session.delete(user)
        session.commit()

    @classmethod
    def update_user (cls, data:dict):

        user = session.query(User).filter_by(postID = data["ID"])

        user.username = data.pop("username", user.username)
        user.name = data.pop("name", user.name)
        user.surname = data.pop("surname", user.surname)
        user.password = data.pop("password", user.password)
        user.group_id =  data.pop("group_id", user.group_id)

        session.commit()

class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer(),primary_key=True)
    votes  =  Column(Integer())
    title = Column(String(50))
    text_body = Column(String(1000))
    groupID = Column(String (50))

    def __init__(self, postId, votes, title, text_body, groupId):
        
        self.id = postId
        self.votes = votes
        self.title = title
        self.text_body = text_body
        self.group_id = groupId

    @classmethod
    def authenticate(cls, data:dict):

        post = session.query(Post).filter_by(postID = data["ID"])

        if (post):
            return True

        return False
    
    @classmethod
    def add_to_DB(cls, data:dict):

        post =  Post(data["ID"], data["votes"],data["title"], data["text_body"],
                    data["groupID"])

        session.add(post)
        session.commit() 

    @classmethod
    def get_post(cls ,data:dict):

        post = session.query(Post).filter_by(ID = data["ID"])
        
        post_dict = {"ID": post.ID, "votes" :post.votes, "title" : post.tite,
                     "text_body" : post.text_body, "groupID" : post.groupID}
        
        return post_dict
     
    @classmethod
    def delete_user (cls, data:dict):

        post = session.query(User).filter_by(ID = data["ID"])

        session.delete(post)
        session.commit()

    @classmethod
    def upvote(cls, data:dict):

        post = session.query(Post).filter_by(ID = data["ID"])

        post.votes += 1

        session.commit()

    @classmethod
    def downvote(cls, data:dict):

        post = session.query(Post).filter_by(ID = data["ID"])
        
        post.votes -=1

        session.commit()

    @classmethod
    def get_votecount(cls, data:dict):

        post = session.query(Post).filter_by(ID = data["ID"])

        return {"votes":post.votes}

