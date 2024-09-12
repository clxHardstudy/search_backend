from typing import Union, Optional, List

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class CarInitDataItem(BaseModel):
    name: str
    release_date: Optional[str]  # 假设日期是字符串类型，可以是 None
    wheelbase: int
    category: int


class CarTypeInitData(BaseModel):
    carinitdata: List[CarInitDataItem]

    class Config:
        schema_extra = {
            "example": {"carinitdata":
                [
                    {
                        "name": "M1A",
                        "release_date": None,
                        "wheelbase": 2650,
                        "category": 0
                    },
                    {
                        "name": "M16 PH2",
                        "release_date": None,
                        "wheelbase": 2700,
                        "category": 0
                    },
                    {
                        "name": "M1D-半载",
                        "release_date": "2018-08-01",
                        "wheelbase": 2650,
                        "category": 0
                    },
                    {
                        "name": "M1E1.6T",
                        "release_date": "2022-03-28",
                        "wheelbase": 2700,
                        "category": 0
                    },
                    {
                        "name": "M1EPHEV",
                        "release_date": "2023-07-12",
                        "wheelbase": 2700,
                        "category": 0
                    },
                    {
                        "name": "E03 RWD螺簧",
                        "release_date": "2023-03-21",
                        "wheelbase": 3000,
                        "category": 0
                    },
                    {
                        "name": "E03 AWD空簧",
                        "release_date": "2023-03-04",
                        "wheelbase": 3000,
                        "category": 0
                    },
                    {
                        "name": "EH3 AWD 空簧",
                        "release_date": "2023-07-10",
                        "wheelbase": 2950,
                        "category": 0
                    },
                    {
                        "name": "Vios",
                        "release_date": "2011-04-08",
                        "wheelbase": 2550,
                        "category": 0
                    },
                    {
                        "name": "悦动",
                        "release_date": "2011-07-15",
                        "wheelbase": 2650,
                        "category": 0
                    },
                    {
                        "name": "观致3",
                        "release_date": "2012-01-12",
                        "wheelbase": 2690,
                        "category": 0
                    },
                    {
                        "name": "福克斯",
                        "release_date": "2013-08-01",
                        "wheelbase": 2631,
                        "category": 0
                    },
                    {
                        "name": "GOlF 6",
                        "release_date": "2010-09-02",
                        "wheelbase": 2578,
                        "category": 0
                    },
                    {
                        "name": "Sagitar",
                        "release_date": "2010-02-22",
                        "wheelbase": 2731,
                        "category": 0
                    },
                    {
                        "name": "Camry",
                        "release_date": "2010-12-03",
                        "wheelbase": 2825,
                        "category": 0
                    },
                    {
                        "name": "捷豹I-PACE",
                        "release_date": "2020-03-24",
                        "wheelbase": 2990,
                        "category": 0
                    },
                    {
                        "name": "Benz S350",
                        "release_date": "2010-08-12",
                        "wheelbase": 3165,
                        "category": 0
                    },
                    {
                        "name": "Audi A4 wagon",
                        "release_date": "2010-09-01",
                        "wheelbase": 2828,
                        "category": 0
                    },
                    {
                        "name": "帝豪GL-半载",
                        "release_date": "2018-06-13",
                        "wheelbase": 2700,
                        "category": 0
                    },
                    {
                        "name": "朗逸-半载",
                        "release_date": "2020-01-01",
                        "wheelbase": 2688,
                        "category": 0
                    },
                    {
                        "name": "卡罗拉",
                        "release_date": "2020-05-06",
                        "wheelbase": 2700,
                        "category": 0
                    },
                    {
                        "name": "秦PLUS",
                        "release_date": "2021-11-16",
                        "wheelbase": 2718,
                        "category": 0
                    },
                    {
                        "name": "轩逸",
                        "release_date": "2022-07-20",
                        "wheelbase": 2712,
                        "category": 0
                    },
                    {
                        "name": "小鹏P7",
                        "release_date": "2021-05-28",
                        "wheelbase": 2975,
                        "category": 0
                    },
                    {
                        "name": "Model 3",
                        "release_date": "2021-03-16",
                        "wheelbase": 2875,
                        "category": 0
                    },
                    {
                        "name": "Benz E260",
                        "release_date": "2021-10-17",
                        "wheelbase": 3014,
                        "category": 0
                    },
                    {
                        "name": "E03 REEV  RWD螺簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "category": 0
                    },
                    {
                        "name": "奔驰EQS",
                        "release_date": None,
                        "wheelbase": 3210,
                        "category": 0
                    }
                ]
            }
        }


class CarTypeInitDataSUV(BaseModel):
    carinitdata: List[CarInitDataItem]

    class Config:
        schema_extra = {
            "example": {"carinitdata":
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


class CarTypeOnce(BaseModel):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 0  # 使用字符串 "id" 作为键
            }
        }


class CarTypeSearchName(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": '奔驰'  # 使用字符串 "id" 作为键
            }
        }


class CarTypeSearchWheelBase(BaseModel):
    WheelBase_Small: str
    WheelBase_Large: str

    class Config:
        schema_extra = {
            "example": {
                "WheelBase_Small": "2800",  # 使用字符串 "id" 作为键
                "WheelBase_Large": "3000"  # 使用字符串 "id" 作为键
            }
        }
