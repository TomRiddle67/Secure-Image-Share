from sqlalchemy import Column, String, DateTime
from datetime import datetime
from database import Base


class ImageRecord(Base):
    __tablename__= "images"

    id = Column (String, primary_key=True)
    filename = Column (String)
    uploaded_by = Column(String)
    file_path = Column (String)
    created_at = Column (DateTime, default= datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)