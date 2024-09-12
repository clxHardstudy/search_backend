from typing import Union, Optional, List

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class CarInitDataItem(BaseModel):
    name: str
    release_date: Optional[str]  # 假设日期是字符串类型，可以是 None
    wheelbase: int


class CarTypeInitData(BaseModel):
    carinitdata: List[CarInitDataItem]

    class Config:
        schema_extra = {
            "example":{"carinitdata":
                [
                    {
                        "name": "T15 CVT ",
                        "release_date": "2015-03-18",
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "T17",
                        "release_date": None,
                        "wheelbase": 2610,
                        "category": 1
                    },
                    {
                        "name": "T19",
                        "release_date": None,
                        "wheelbase": 2610,
                        "category": 1
                    },
                    {
                        "name": "T19CEV",
                        "release_date": "2023-03-13",
                        "wheelbase": 2610,
                        "category": 1
                    },
                    {
                        "name": "T18",
                        "release_date": None,
                        "wheelbase": 2700,
                        "category": 1
                    },
                    {
                        "name": "T1A",
                        "release_date": "2019-01-01",
                        "wheelbase": 2700,
                        "category": 1
                    },
                    {
                        "name": "T1DPHEV ",
                        "release_date": "2020-03-06",
                        "wheelbase": 2700,
                        "category": 1
                    },
                    {
                        "name": "T1C-半载",
                        "release_date": "2019-09-01",
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "T1E-半载",
                        "release_date": None,
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "T1EJ四驱",
                        "release_date": "2022-08-24",
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "T1X升级Mulecar",
                        "release_date": "2023-11-13",
                        "wheelbase": 2700,
                        "category": 1
                    },
                    {
                        "name": "M31T",
                        "release_date": "2018-09-26",
                        "wheelbase": 2697,
                        "category": 1
                    },
                    {
                        "name": "M36T-半载",
                        "release_date": "2019-08-03",
                        "wheelbase": 2780,
                        "category": 1
                    },
                    {
                        "name": "T22",
                        "release_date": "2022-08-17",
                        "wheelbase": 2800,
                        "category": 1
                    },
                    {
                        "name": "T26",
                        "release_date": "2023-04-17",
                        "wheelbase": 2800,
                        "category": 1
                    },
                    {
                        "name": "T28",
                        "release_date": "2023-04-17",
                        "wheelbase": 2750,
                        "category": 1
                    },
                    {
                        "name": "T22PHEV",
                        "release_date": "2023-08-29",
                        "wheelbase": 2800,
                        "category": 1
                    },
                    {
                        "name": "E0Y RWD空簧",
                        "release_date": "2023-06-06",
                        "wheelbase": 3000,
                        "category": 1
                    },
                    {
                        "name": "E0Y AWD空簧",
                        "release_date": "2023-06-06",
                        "wheelbase": 3000,
                        "category": 1
                    },
                    {
                        "name": "RAV4",
                        "release_date": "2010-08-31",
                        "wheelbase": 2660,
                        "category": 1
                    },
                    {
                        "name": "RAV4荣放",
                        "release_date": None,
                        "wheelbase": 2660,
                        "category": 1
                    },
                    {
                        "name": "CRV",
                        "release_date": "2010-08-30",
                        "wheelbase": 2620,
                        "category": 1
                    },
                    {
                        "name": "IX35",
                        "release_date": "2010-07-30",
                        "wheelbase": 2640,
                        "category": 1
                    },
                    {
                        "name": "逍客",
                        "release_date": "2012-12-10",
                        "wheelbase": 2665,
                        "category": 1
                    },
                    {
                        "name": "Tiguan",
                        "release_date": "2009-12-29",
                        "wheelbase": 2684,
                        "category": 1
                    },
                    {
                        "name": "P11",
                        "release_date": None,
                        "wheelbase": 2725,
                        "category": 1
                    },
                    {
                        "name": "Prado",
                        "release_date": None,
                        "wheelbase": 2790,
                        "category": 1
                    },
                    {
                        "name": "CS75",
                        "release_date": "2019-01-30",
                        "wheelbase": 2700,
                        "category": 1
                    },
                    {
                        "name": "CS55PLUS",
                        "release_date": "2022-05-06",
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "领克02",
                        "release_date": "2019-02-14",
                        "wheelbase": 2650,
                        "category": 1
                    },
                    {
                        "name": "长城坦克300",
                        "release_date": "2022-07-05",
                        "wheelbase": 2750,
                        "category": 1
                    },
                    {
                        "name": "长城H6",
                        "release_date": "2020-12-23",
                        "wheelbase": 2680,
                        "category": 1
                    },
                    {
                        "name": "途观L",
                        "release_date": "2019-09-02",
                        "wheelbase": 2791,
                        "category": 1
                    },
                    {
                        "name": "Creta半载",
                        "release_date": None,
                        "wheelbase": 2610,
                        "category": 1
                    },
                    {
                        "name": "博越Pro半载",
                        "release_date": "2019-11-11",
                        "wheelbase": 2670,
                        "category": 1
                    },
                    {
                        "name": "GLC半载",
                        "release_date": "2020-01-01",
                        "wheelbase": 2873,
                        "category": 1
                    },
                    {
                        "name": "Modle Y半载",
                        "release_date": "2021-07-02",
                        "wheelbase": 2890,
                        "category": 1
                    },
                    {
                        "name": "EC 6半载",
                        "release_date": "2021-05-21",
                        "wheelbase": 2915,
                        "category": 1
                    },
                    {
                        "name": "理想L8",
                        "release_date": "2023-04-18",
                        "wheelbase": 3005,
                        "category": 1
                    },
                    {
                        "name": "路虎卫士",
                        "release_date": "2023-02-23",
                        "wheelbase": 3025,
                        "category": 1
                    },
                    {
                        "name": "E0Y REEV AWD螺簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "category": 1
                    },
                    {
                        "name": "E0Y REEV AWD空簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "category": 1
                    },
                    {
                        "name": "奔驰EQS SUV",
                        "release_date": None,
                        "wheelbase": 3210,
                        "category": 1
                    }
                ]

            }
        }
