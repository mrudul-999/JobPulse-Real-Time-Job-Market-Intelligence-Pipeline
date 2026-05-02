import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import JobRawData, Base

DATABASE_URL = "postgresql://postgres:password@localhost:54302/job_pulse"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


session = SessionLocal()

url = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(url)
jobs = response.json()

print(jobs["data"][0]) 

for job in jobs["data"]:
    job_raw = JobRawData(
        source = "arbeitenow",
        source_job_id = job['slug'],
        raw_payload = job
    )
    session.add(job_raw)

try:
    session.commit()
    print("Successfully stored raw job data!")
except Exception as e:
    session.rollback()
    print(f"Error saving to database: {e}")
finally:
    session.close()

