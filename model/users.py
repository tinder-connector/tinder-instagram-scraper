from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from model.base import Base
from model.job import Job
from model.sexualorientation import SexualOrientation
from model.school import School
from model.astrologicalsign import AstrologicalSign
from model.levelstudy import LevelStudy
from model.familyprojects import FamilyProjects
from model.personality import Personality
from model.communication import Communication
from model.languageoflove import LanguageOfLove
from model.bloodgroup import BloodGroup
from model.pet import Pet
from model.alcohol import Alcohol
from model.smokingfrequency import SmokingFrequency
from model.sport import Sport
from model.foodpreferences import FoodPreferences
from model.socialnetworks import SocialNetworks
from model.sleephabits import SleepHabits
from model.relationshipintent import RelationshipIntent
from model.position import Position

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    id_tinder = Column(String(255), nullable=False)
    bio = Column(String(255))
    birth_date = Column(DateTime)
    name = Column(String(255), nullable=False)
    gender = Column(Integer)
    sexual_orientation_id = Column(Integer, ForeignKey('sexualorientation.id'))
    sexual_orientation = relationship(SexualOrientation, backref="users")
    job_id = Column(Integer, ForeignKey('job.id'))
    job = relationship(Job, backref="users")
    school_id = Column(Integer, ForeignKey('school.id'))
    school = relationship(School, backref="users")
    measurement = Column(Integer)
    astrological_sign_id = Column(Integer, ForeignKey('astrologicalsign.id'))
    astrological_sign = relationship(AstrologicalSign, backref="users")
    level_study_id = Column(Integer, ForeignKey('levelstudy.id'))
    level_study = relationship(LevelStudy, backref="users")
    family_projects_id = Column(Integer, ForeignKey('familyprojects.id'))
    family_projects = relationship(FamilyProjects, backref="users")
    covid_vaccine = Column(Boolean)
    personality_id = Column(Integer, ForeignKey('personality.id'))
    personality = relationship(Personality, backref="users")
    communication_id = Column(Integer, ForeignKey('communication.id'))
    communication = relationship(Communication, backref="users")
    language_of_love_id = Column(Integer, ForeignKey('languageoflove.id'))
    language_of_love = relationship(LanguageOfLove, backref="users")
    blood_group_id = Column(Integer, ForeignKey('bloodgroup.id'))
    blood_group = relationship(BloodGroup, backref="users")
    pet_id = Column(Integer, ForeignKey('pet.id'))
    pet = relationship(Pet, backref="users")
    alcohol_id = Column(Integer, ForeignKey('alcohol.id'))
    alcohol = relationship(Alcohol, backref="users")
    smoking_frequency_id = Column(Integer, ForeignKey('smokingfrequency.id'))
    smoking_frequency = relationship(SmokingFrequency, backref="users")
    sport_id = Column(Integer, ForeignKey('sport.id'))
    sport = relationship(Sport, backref="users")
    food_preferences_id = Column(Integer, ForeignKey('foodpreferences.id'))
    food_preferences = relationship(FoodPreferences, backref="users")
    social_networks_id = Column(Integer, ForeignKey('socialnetworks.id'))
    social_networks = relationship(SocialNetworks, backref="users")
    sleep_habits_id = Column(Integer, ForeignKey('sleephabits.id'))
    sleep_habits = relationship(SleepHabits, backref="users")
    relationship_intent_id = Column(Integer, ForeignKey('relationshipintent.id'))
    relationship_intent = relationship(RelationshipIntent, backref="users")
    distance = Column(Integer)
    position_id = Column(Integer, ForeignKey('position.id'), nullable=False)
    position = relationship(Position, backref="users")