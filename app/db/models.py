from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime



Base = declarative_base()


class JobRawData(Base):
    __tablename__ = "job_raw_data"
    id = Column(Integer, primary_key=True)
    source = Column(String(100))
    source_job_id = Column(String(100))
    raw_payload = Column(JSONB)
    fetched_at = Column(DateTime, default=datetime.now)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    company = Column(String(255))
    location = Column(String(255))
    country = Column(String(100))
    remote_type = Column(String(50))
    description = Column(Text())
    job_url = Column(String())
    posted_at = Column(DateTime)
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

class JobSkill(Base):
    __tablename__ = "job_skills"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))