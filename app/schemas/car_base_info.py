from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class CarBaseInfoInitDataItem(BaseModel):
    name: str
    release_date: Optional[str]  # 假设日期是字符串类型，可以是 None
    wheelbase: int
    car_type_id: int


class CarBaseInfoListInitData(BaseModel):
    carinitdata: List[CarBaseInfoInitDataItem]

    class Config:
        schema_extra = {
            "example": {"carinitdata":
                [
                    {
                        "name": "M1A",
                        "release_date": None,
                        "wheelbase": 2650,
                        "car_type_id": 1
                    },
                    {
                        "name": "M16 PH2",
                        "release_date": None,
                        "wheelbase": 2700,
                        "car_type_id": 1
                    },
                    {
                        "name": "M1D-半载",
                        "release_date": "2018-08-01",
                        "wheelbase": 2650,
                        "car_type_id": 1
                    },
                    {
                        "name": "M1E1.6T",
                        "release_date": "2022-03-28",
                        "wheelbase": 2700,
                        "car_type_id": 1
                    },
                    {
                        "name": "M1EPHEV",
                        "release_date": "2023-07-12",
                        "wheelbase": 2700,
                        "car_type_id": 1
                    },
                    {
                        "name": "E03 RWD螺簧",
                        "release_date": "2023-03-21",
                        "wheelbase": 3000,
                        "car_type_id": 1
                    },
                    {
                        "name": "E03 AWD空簧",
                        "release_date": "2023-03-04",
                        "wheelbase": 3000,
                        "car_type_id": 1
                    },
                    {
                        "name": "EH3 AWD 空簧",
                        "release_date": "2023-07-10",
                        "wheelbase": 2950,
                        "car_type_id": 1
                    },
                    {
                        "name": "Vios",
                        "release_date": "2011-04-08",
                        "wheelbase": 2550,
                        "car_type_id": 1
                    },
                    {
                        "name": "悦动",
                        "release_date": "2011-07-15",
                        "wheelbase": 2650,
                        "car_type_id": 1
                    },
                    {
                        "name": "观致3",
                        "release_date": "2012-01-12",
                        "wheelbase": 2690,
                        "car_type_id": 1
                    },
                    {
                        "name": "福克斯",
                        "release_date": "2013-08-01",
                        "wheelbase": 2631,
                        "car_type_id": 1
                    },
                    {
                        "name": "GOlF 6",
                        "release_date": "2010-09-02",
                        "wheelbase": 2578,
                        "car_type_id": 1
                    },
                    {
                        "name": "Sagitar",
                        "release_date": "2010-02-22",
                        "wheelbase": 2731,
                        "car_type_id": 1
                    },
                    {
                        "name": "Camry",
                        "release_date": "2010-12-03",
                        "wheelbase": 2825,
                        "car_type_id": 1
                    },
                    {
                        "name": "捷豹I-PACE",
                        "release_date": "2020-03-24",
                        "wheelbase": 2990,
                        "car_type_id": 1
                    },
                    {
                        "name": "Benz S350",
                        "release_date": "2010-08-12",
                        "wheelbase": 3165,
                        "car_type_id": 1
                    },
                    {
                        "name": "Audi A4 wagon",
                        "release_date": "2010-09-01",
                        "wheelbase": 2828,
                        "car_type_id": 1
                    },
                    {
                        "name": "帝豪GL-半载",
                        "release_date": "2018-06-13",
                        "wheelbase": 2700,
                        "car_type_id": 1
                    },
                    {
                        "name": "朗逸-半载",
                        "release_date": "2020-01-01",
                        "wheelbase": 2688,
                        "car_type_id": 1
                    },
                    {
                        "name": "卡罗拉",
                        "release_date": "2020-05-06",
                        "wheelbase": 2700,
                        "car_type_id": 1
                    },
                    {
                        "name": "秦PLUS",
                        "release_date": "2021-11-16",
                        "wheelbase": 2718,
                        "car_type_id": 1
                    },
                    {
                        "name": "轩逸",
                        "release_date": "2022-07-20",
                        "wheelbase": 2712,
                        "car_type_id": 1
                    },
                    {
                        "name": "小鹏P7",
                        "release_date": "2021-05-28",
                        "wheelbase": 2975,
                        "car_type_id": 1
                    },
                    {
                        "name": "Model 3",
                        "release_date": "2021-03-16",
                        "wheelbase": 2875,
                        "car_type_id": 1
                    },
                    {
                        "name": "Benz E260",
                        "release_date": "2021-10-17",
                        "wheelbase": 3014,
                        "car_type_id": 1
                    },
                    {
                        "name": "E03 REEV  RWD螺簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "car_type_id": 1
                    },
                    {
                        "name": "奔驰EQS",
                        "release_date": None,
                        "wheelbase": 3210,
                        "car_type_id": 1
                    }
                ]

            }
        }


class CarBaseInfoListInitDataSUV(BaseModel):
    carinitdata: List[CarBaseInfoInitDataItem]

    class Config:
        schema_extra = {
            "example": {"carinitdata":
                [
                    {
                        "name": "T15 CVT ",
                        "release_date": "2015-03-18",
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "T17",
                        "release_date": None,
                        "wheelbase": 2610,
                        "car_type_id": 2
                    },
                    {
                        "name": "T19",
                        "release_date": None,
                        "wheelbase": 2610,
                        "car_type_id": 2
                    },
                    {
                        "name": "T19CEV",
                        "release_date": "2023-03-13",
                        "wheelbase": 2610,
                        "car_type_id": 2
                    },
                    {
                        "name": "T18",
                        "release_date": None,
                        "wheelbase": 2700,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1A",
                        "release_date": "2019-01-01",
                        "wheelbase": 2700,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1DPHEV ",
                        "release_date": "2020-03-06",
                        "wheelbase": 2700,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1C-半载",
                        "release_date": "2019-09-01",
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1E-半载",
                        "release_date": None,
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1EJ四驱",
                        "release_date": "2022-08-24",
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "T1X升级Mulecar",
                        "release_date": "2023-11-13",
                        "wheelbase": 2700,
                        "car_type_id": 2
                    },
                    {
                        "name": "M31T",
                        "release_date": "2018-09-26",
                        "wheelbase": 2697,
                        "car_type_id": 2
                    },
                    {
                        "name": "M36T-半载",
                        "release_date": "2019-08-03",
                        "wheelbase": 2780,
                        "car_type_id": 2
                    },
                    {
                        "name": "T22",
                        "release_date": "2022-08-17",
                        "wheelbase": 2800,
                        "car_type_id": 2
                    },
                    {
                        "name": "T26",
                        "release_date": "2023-04-17",
                        "wheelbase": 2800,
                        "car_type_id": 2
                    },
                    {
                        "name": "T28",
                        "release_date": "2023-04-17",
                        "wheelbase": 2750,
                        "car_type_id": 2
                    },
                    {
                        "name": "T22PHEV",
                        "release_date": "2023-08-29",
                        "wheelbase": 2800,
                        "car_type_id": 2
                    },
                    {
                        "name": "E0Y RWD空簧",
                        "release_date": "2023-06-06",
                        "wheelbase": 3000,
                        "car_type_id": 2
                    },
                    {
                        "name": "E0Y AWD空簧",
                        "release_date": "2023-06-06",
                        "wheelbase": 3000,
                        "car_type_id": 2
                    },
                    {
                        "name": "RAV4",
                        "release_date": "2010-08-31",
                        "wheelbase": 2660,
                        "car_type_id": 2
                    },
                    {
                        "name": "RAV4荣放",
                        "release_date": None,
                        "wheelbase": 2660,
                        "car_type_id": 2
                    },
                    {
                        "name": "CRV",
                        "release_date": "2010-08-30",
                        "wheelbase": 2620,
                        "car_type_id": 2
                    },
                    {
                        "name": "IX35",
                        "release_date": "2010-07-30",
                        "wheelbase": 2640,
                        "car_type_id": 2
                    },
                    {
                        "name": "逍客",
                        "release_date": "2012-12-10",
                        "wheelbase": 2665,
                        "car_type_id": 2
                    },
                    {
                        "name": "Tiguan",
                        "release_date": "2009-12-29",
                        "wheelbase": 2684,
                        "car_type_id": 2
                    },
                    {
                        "name": "P11",
                        "release_date": None,
                        "wheelbase": 2725,
                        "car_type_id": 2
                    },
                    {
                        "name": "Prado",
                        "release_date": None,
                        "wheelbase": 2790,
                        "car_type_id": 2
                    },
                    {
                        "name": "CS75",
                        "release_date": "2019-01-30",
                        "wheelbase": 2700,
                        "car_type_id": 2
                    },
                    {
                        "name": "CS55PLUS",
                        "release_date": "2022-05-06",
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "领克02",
                        "release_date": "2019-02-14",
                        "wheelbase": 2650,
                        "car_type_id": 2
                    },
                    {
                        "name": "长城坦克300",
                        "release_date": "2022-07-05",
                        "wheelbase": 2750,
                        "car_type_id": 2
                    },
                    {
                        "name": "长城H6",
                        "release_date": "2020-12-23",
                        "wheelbase": 2680,
                        "car_type_id": 2
                    },
                    {
                        "name": "途观L",
                        "release_date": "2019-09-02",
                        "wheelbase": 2791,
                        "car_type_id": 2
                    },
                    {
                        "name": "Creta半载",
                        "release_date": None,
                        "wheelbase": 2610,
                        "car_type_id": 2
                    },
                    {
                        "name": "博越Pro半载",
                        "release_date": "2019-11-11",
                        "wheelbase": 2670,
                        "car_type_id": 2
                    },
                    {
                        "name": "GLC半载",
                        "release_date": "2020-01-01",
                        "wheelbase": 2873,
                        "car_type_id": 2
                    },
                    {
                        "name": "Modle Y半载",
                        "release_date": "2021-07-02",
                        "wheelbase": 2890,
                        "car_type_id": 2
                    },
                    {
                        "name": "EC 6半载",
                        "release_date": "2021-05-21",
                        "wheelbase": 2915,
                        "car_type_id": 2
                    },
                    {
                        "name": "理想L8",
                        "release_date": "2023-04-18",
                        "wheelbase": 3005,
                        "car_type_id": 2
                    },
                    {
                        "name": "路虎卫士",
                        "release_date": "2023-02-23",
                        "wheelbase": 3025,
                        "car_type_id": 2
                    },
                    {
                        "name": "E0Y REEV AWD螺簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "car_type_id": 2
                    },
                    {
                        "name": "E0Y REEV AWD空簧",
                        "release_date": None,
                        "wheelbase": 3000,
                        "car_type_id": 2
                    },
                    {
                        "name": "奔驰EQS SUV",
                        "release_date": None,
                        "wheelbase": 3210,
                        "car_type_id": 2
                    }
                ]
            }
        }


class CarBaseInfoOnce(BaseModel):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 0  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoList(BaseModel):
    car_base_info_id_list: Optional[List[int]] = None  # 默认为 None 表示允许为空

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id_list": [1, 2, 3, 4, 5]  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoCarTypeAndPlatform(BaseModel):
    car_type_id: int
    platform_id_list: List[int]

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2]  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoSearchName(BaseModel):
    car_type_id: int
    platform_id_list: List[int]
    name: str

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2],
                "name": '奔驰'  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoSearchWheelBase(BaseModel):
    car_type_id: int
    platform_id_list: List[int]
    wheelbase: str

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2],
                "wheelbase": "2800",  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoSearchNameAndWheelBase(BaseModel):
    car_type_id: int
    platform_id_list: List[int]
    name: str
    wheelbase: str

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2],
                "name": "T1",
                "wheelbase": "2800",  # 使用字符串 "id" 作为键
            }
        }


class CarBaseInfoMultipleConditionQuery(BaseModel):
    car_type_id: int
    platform_id_list: List[int]
    name: str
    wheelbase: str
    front_track: str
    rear_track: str

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2],
                "name": "T1",
                "wheelbase": "2800",
                "front_track": "2800",
                "rear_track": "2800",
            }
        }


class CarBaseInfoNewMultipleConditionQuery(BaseModel):
    car_type_id: int
    platform_id_list: List[int]
    name: str
    wheelbase: str
    front_track: str
    rear_track: str
    car_base_info_id_list: Optional[List[int]] = None  # 默认为 None 表示允许为空

    class Config:
        schema_extra = {
            "example": {
                "car_type_id": 1,
                "platform_id_list": [1, 2],
                "name": "T1",
                "wheelbase": "2800",
                "front_track": "2800",
                "rear_track": "2800",
                "car_base_info_id_list": [1, 2]
            }
        }
