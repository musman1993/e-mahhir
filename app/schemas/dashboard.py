from pydantic import BaseModel
from datetime import date
from typing import Dict, List

class WidgetData(BaseModel):
    title: str
    value: int | float
    change_percentage: float
    comparison_period: str

class ReportRequest(BaseModel):
    report_type: str
    start_date: date
    end_date: date
    filters: Dict[str, str] = {}

class ReportResponse(BaseModel):
    data: List[Dict]
    generated_at: str
    format: str = "json"