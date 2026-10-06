from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AgentRunModel(Base):
    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True, index=True)
    goal = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    status = Column(String(50), default="COMPLETED")
    created_at = Column(DateTime(timezone=True), server_default=func.now())