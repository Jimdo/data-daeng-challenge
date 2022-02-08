
import math
import random
import uuid
from dataclasses import  dataclass
from dataclasses_json import dataclass_json
from datetime import date, datetime, timedelta, timezone
from typing import Iterable, Optional, Union


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
    top_pages: dict
    sources: dict
    sent_contact_form: int
    clicked_booking_button: int
    engaged_visitors: int



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
                date= str(start_date + timedelta(days=day)),
                visitors=n_website_visitors,
                visits=math.floor(n_website_visitors * visit_rate),
                top_pages=dict(
                    {
                        "/": math.floor(n_website_visitors * 0.8),
                        "/about": math.floor(n_website_visitors * 0.3),
                        "/privacy-policy": math.floor(n_website_visitors * 0.2),
                    }
                ),
                sources=dict(
                    {
                        "facebook": math.floor(n_website_visitors * 0.2),
                        "google": math.floor(n_website_visitors * 0.3),
                        "direct": math.floor(n_website_visitors * 0.5),
                    }
                ),
                sent_contact_form=math.floor(n_website_visitors * 0.1),
                clicked_booking_button=math.floor(n_website_visitors * 0.1),
                engaged_visitors=math.floor(n_website_visitors * 0.33),
            )


# def random_user_agent() -> str:
#     return random.choice(USER_AGENTS)
#
#
# USER_AGENTS = [
#     "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1 at_load_test_tool",
#     "Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1 at_load_test_tool",
#     "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3 at_load_test_tool",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254 at_load_test_tool",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536 at_load_test_tool",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246 at_load_test_tool",
#     "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9 at_load_test_tool",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 at_load_test_tool",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 at_load_test_tool",
#     "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36 at_load_test_tool",
#     "Roku4640X/DVP-7.70 (297.70E04154A) at_load_test_tool",
#     "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 at_load_test_tool",
#     "Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36 at_load_test_tool",
#     "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T) at_load_test_tool",
#     "AppleTV6,2/11.1 at_load_test_tool",
#     "AppleTV5,3/9.1.1 at_load_test_tool",
#     "Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US at_load_test_tool",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393 at_load_test_tool",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586 at_load_test_tool",
#     "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko) at_load_test_tool",
#     "Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2 at_load_test_tool",
#     "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU at_load_test_tool",
#     "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) at_load_test_tool",
#     "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) at_load_test_tool",
#     "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp) at_load_test_tool",
#     "Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+ at_load_test_tool",
#     "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate) at_load_test_tool",
# ]