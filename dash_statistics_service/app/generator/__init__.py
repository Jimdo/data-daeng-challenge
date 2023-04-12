import math
import random
import uuid
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from typing import Iterable, Optional, Union

from dataclasses_json import dataclass_json


@dataclass
class Website:
    id: uuid.UUID
    locations: list[str]


@dataclass_json
@dataclass
class DashStatisticsDailyRecord:
    website_id: uuid.UUID
    date: str
    visitors: int
    visits: int
    sources: dict


def generate_records(
    n_websites: int,
    start_date: date,
    end_date: date,
    max_visitors: int = 100,
    visit_rate: float = 1.2,
) -> Iterable[DashStatisticsDailyRecord]:
    assert n_websites > 0
    assert max_visitors > 1
    assert end_date > start_date
    assert visit_rate > 1.0
    days = (end_date - start_date).days
    websites = [uuid.uuid4() for _ in range(n_websites)]
    for day in range(days):
        for website in websites:
            n_website_visitors = math.floor(random.uniform(1, max_visitors))
            yield DashStatisticsDailyRecord(
                website_id=website,
                date=str(start_date + timedelta(days=day)),
                visitors=n_website_visitors,
                visits=math.floor(n_website_visitors * visit_rate),
                sources=dict(
                    {
                        "facebook": math.floor(n_website_visitors * 0.2),
                        "google": math.floor(n_website_visitors * 0.3),
                        "direct": math.floor(n_website_visitors * 0.5),
                    }
                ),
            )
