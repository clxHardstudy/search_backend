from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


# 定义 WorkingConditions 模型
class WorkingConditions(BaseModel):
    coordinate_system: str
    working_conditions_list: List[int]  # 确保类型是 List[int]
    car_id_list: Optional[List[int]] = None  # 允许 car_id 为空

    class Config:
        schema_extra = {
            "example": {
                "coordinate_system": "0",
                "working_conditions_list": [1, 2, 3],  # 修改此字段名为 working_conditions_list
                "car_id_list": [1, 2, 3]
            }
        }


class WorkingConditionsDetailOnce(BaseModel):
    car_base_info_id: int

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 1,
            }
        }


class WorkingConditionsDetailAll(BaseModel):
    car_base_info_id: int
    coordinate_system: int
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 72,
                "coordinate_system": 0,
                "data": {
                    "vertical_parallel_arb_connected": {'wheel_rate': '25.3', 'vertical_force_hysteresis': '429',
                                                        'ride_frequency_no_tyre': '1.17', 'ride_rate': '22.8',
                                                        'ride_frequency_with_tyre': '1.11', 'tyre_radial_rate': '226.3',
                                                        'toe_angle_change': '-7.1', 'camber_change': '-7.1',
                                                        'spin_angle_change': '-9.9',
                                                        'kinematic_oll_centre_height': '24',
                                                        'fore_aft_displacement_wc': '1.6',
                                                        'fore_aft_displacement_tcp': '48.5'},
                    "vertical_parallel_arb_disconnected": {'wheel_rate': '25.6', 'vertical_force_hysteresis': '427'},
                    "vertical_roll_arb_connected": {'wheel_rate': '77.4', 'toe_angle_change': '-4.4',
                                                    'camber_change': '-11.7', 'kinematic_oll_centre_height': '36',
                                                    'suspension_roll_stiffness': '1634',
                                                    'total_vehicle_roll_stiffness': '-1224',
                                                    'roll_stiffness_distribution': '69'},
                    "vertical_roll_arb_disconnected": {'wheel_rate': '26.9', 'toe_angle_change': '-6.3',
                                                       'camber_change': '-7.5', 'kinematic_oll_centre_height': '14',
                                                       'suspension_roll_stiffness': '593',
                                                       'total_vehicle_roll_stiffness': '-520',
                                                       'roll_stiffness_distribution': '48'},
                    "steering_kinematics_pas_on": {'overall_steer_ratio': '15.6', 'on_center_steer_ratio': '16.2',
                                                   'steering_friction': '0.97', 'scrub_radius': '18.4',
                                                   'mechanical_trail': '15.7', 'kingpin_offset_pl': '-9.7',
                                                   'kingpin_offset_wc': '64.9', 'castor_angle': '3.6',
                                                   'kingpin_inclination_angle': '13.4'},
                    "lateral_parallel_in_phase": {'wc_compliance': '0.0889', 'toe_compliance': '0.0564',
                                                  'camber_compliance': '-0.166', 'lateral_stiffness_tcp': '103',
                                                  'force_roll_centre_height': '31'},
                    "lateral_parallel_out_of_phase": {'wc_compliance': '0.0192', 'toe_compliance': '0.0138',
                                                      'camber_compliance': '-0.159', 'lateral_stiffness_tcp': '104.6',
                                                      'force_roll_centre_height': '19'},
                    "lateral_parallel_thirty_millmeters_trail": {'wc_compliance': '0.0417', 'toe_compliance': '0.1581',
                                                                 'camber_compliance': '-0.184',
                                                                 'lateral_stiffness_tcp': '103.1'},
                    "aligning_torque_parallel": {'toe_compliance': '-2.9469', 'camber_compliance': '0.507'},
                    "aligning_torque_opposite": {'toe_compliance': '-1.2586', 'camber_compliance': '0.369'},
                    "longitudinal_acceleration": {'spin_angle_change': '-5.555', 'wc_compliance': '1.6671',
                                                  'toe_compliance': '0.0684', 'camber_compliance': '0.06',
                                                  'anti_lift_or_squat_angle': '0.5'},
                    "longitudinal_Braking": {'spin_angle_change': '-0.469', 'wc_compliance': '2.6658',
                                             'toe_compliance': '-0.03', 'camber_compliance': '0.025',
                                             'anti_lift_or_squat_angle': '-1.9', 'longitudinal_stiffness_tcp': '117.3'},
                }

            }
        }


class WorkingConditionsDetailTitle(BaseModel):
    working_conditions_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "working_conditions_list": [1, 2, 3],  # 修改此字段名为 working_conditions_list
            }
        }
