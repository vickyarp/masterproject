import base64
from io import BytesIO
import dash_html_components as html

import numpy as np
from PIL import Image

DATA_PATH = './assets/keypoints/'
THUMBNAIL_PATH = './assets/thumbnails/'

DATASET_VIDEOS = [
    'contemp1',
    'TB_F_FB',
    'UP3',
    'UP2',
    'UP1',
    'TR_S',
    'TR_F',
    'TOS_S',
    'TOS_F',
    'TL_S',
    'TL_F',
    'TF_S',
    'TF_F',
    'TB_S',
    'TB_S_FB',
    'TA',
    'SYN_U',
    'SYN_S',
    'SYN_R',
    'SYN_K',
    'SYN_B',
    'SS_S_RT',
    'SS_S_LT',
    'SS_S_FT',
    'SS_S_BK',
    'SS_F_RT',
    'SS_F_LT',
    'SS_F_FT',
    'SS_F_BK',
    'SJ_RT',
    'SJ_LT',
    'SJ_FT',
    'SJ_BK',
    'SB_R_WA',
    'SB_R_NA',
    'RV_R_S',
    'RV_R_F',
    'PV_R_S',
    'PV_R_F',
    'PE',
    'PC_F',
    'PC_S',
    'PB_S',
    'PB_F',
    'P3',
    'P2',
    'P1',
    'LU_S_dis',
    'LU_S_big',
    'LU_F_dis',
    'LU_F_big',
    'LD_S_small',
    'LD_S_dis',
    'LD_F_small',
    'FR_R_WA',
    'LD_F_dis',
    'FR_R_NA',
    'EF',
    'CU_R_WA',
    'CU_R_NA',
    'CH',
    'BSS_S_FT',
    'BSS_S_BK',
    'BS_S_RT',
    'BSS_F_FT',
    'BSS_F_BK',
    'BS_S_LT',
    'BS_S_FT',
    'BS_S_BK',
    'BS_F_RT',
    'BS_F_LT',
    'BS_F_FT',
    'BS_F_BK',
    'BJ_RT',
    'BJ_LT',
    'BJ_FT',
    'BJ_BK',
    'BBS_S_FT',
    'BBS_S_BK',
    'BBS_F_FT',
    'BBS_F_BK',
    'BA_R_WA',
    'BA_R_NA',
    'AS_L_WA',
    'AS_L_NA',
    'TB_F_FB',
    'AR',
]

COLORS = [
    'rgb(255, 0, 85)',
    'rgb(255, 0, 0)',
    'rgb(255, 85, 0)',
    'rgb(255, 170, 0)',
    'rgb(255, 255, 0)',
    'rgb(170, 255, 0)',
    'rgb(85, 255, 0)',
    'rgb(0, 255, 0)',
    'rgb(255, 0, 0)',
    'rgb(0, 255, 85)',
    'rgb(0, 255, 170)',
    'rgb(0, 255, 255)',
    'rgb(0, 170, 255)',
    'rgb(0, 85, 255)',
    'rgb(0, 0, 255)',
    'rgb(255, 0, 170)',
    'rgb(170, 0, 255)',
    'rgb(255, 0, 255)',
    'rgb(85, 0, 255)',
    'rgb(0, 0, 255)',
    'rgb(0, 0, 255)',
    'rgb(0, 0, 255)',
    'rgb(0, 255, 255)',
    'rgb(0, 255, 255)']

PAIRS_RENDER = np.array(
    [[1, 8], [1, 2], [1, 5], [2, 3], [3, 4], [5, 6], [6, 7], [8, 9], [9, 10], [10, 11], [8, 12], [12, 13], [13, 14],
     [1, 0], [0, 15], [15, 17], [0, 16], [16, 18], [14, 19], [19, 20], [14, 21], [11, 22], [22, 23], [11, 24]])

PAIRS_RENDER_NEW = np.array(
    [[2, 9], [2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [9, 10], [10, 11], [11, 12], [9, 13], [13, 14], [14, 15],
     [2, 1], [1, 16], [16, 18], [1, 17], [17, 19], [15, 20], [20, 21], [15, 22], [12, 23], [23, 24], [12, 25]])

#
# x=[df.x[1], df.x[8], None, df.x[1], df.x[2], None, df.x[1], df.x[5], None,
#  df.x[2], df.x[3], None, df.x[3], df.x[4], None,df.x[5], df.x[6], None, df.x[6], df.x[7], None,
# df.x[8], df.x[9], None,df.x[9], df.x[10], None,df.x[10], df.x[11], None,df.x[8], df.x[12], None,df.x[12], df.x[13], None,
# df.x[13], df.x[14], None,df.x[1], df.x[0], None,df.x[0], df.x[15], None,df.x[15], df.x[17], None,df.x[0], df.x[16], None,df.x[16], df.x[18], None,
# df.x[14], df.x[19], None,df.x[19], df.x[20], None,df.x[14], df.x[21], None,df.x[11], df.x[22], None,df.x[22], df.x[23], None,df.x[11], df.x[24]],
#                                  y=[df.y[1], df.y[8], None, df.y[1], df.y[2], None, df.y[1], df.y[5], None,
#  df.y[2], df.y[3], None, df.y[3], df.y[4], None,df.y[5], df.y[6], None, df.y[6], df.y[7], None,
# df.y[8], df.y[9], None,df.y[9], df.y[10], None,df.y[10], df.y[11], None,df.y[8], df.y[12], None,df.y[12], df.y[13], None,
# df.y[13], df.y[14], None,df.y[1], df.y[0], None,df.y[0], df.y[15], None,df.y[15], df.y[17], None,df.y[0], df.y[16], None,df.y[16], df.y[18], None,
# df.y[14], df.y[19], None,df.y[19], df.y[20], None,df.y[14], df.y[21], None,df.y[11], df.y[22], None,df.y[22], df.y[23], None,df.y[11], df.y[24]]


BODYPART_INDEX = {
    0: 'nose_to_neck_to_left_shoulder',
    1: 'nose_to_neck_to_right_shoulder',
    2: 'left_shoulder_to_right_shoulder',
    3: 'left_shoulder_to_left_upper_arm',
    4: 'left_lower_arm_to_left_upper_arm',
    5: 'right_upper_arm_to_right_shoulder',
    6: 'right_upper_arm_to_right_lower_arm',
    7: 'left_eye_to_nose_to_left_ear_to_eye',
    8: 'left_eye_to_nose_to_neck',
    9: 'nose_to_neck_to_right_eye_to_nose',
    10: 'left_eye_to_nose_to_right_ear_to_eye',
    11: 'right_eye_to_nose_to_right_ear_to_eye',
    12: 'right_hip_to_right_upper_leg',
    13: 'right_upper_leg_to_right_lower_leg',
    14: 'left_hip_to_left_upper_leg',
    15: 'left_upper_leg_to_left_lower_leg',
    16: 'left_lower_leg_left_ankle_to_heel',
    17: 'right_lower_leg_to_right_ankle_to_heel',
    18: 'right_foot_to_right_toes',
    19: 'right_foot_to_right_lower_leg',
    20: 'right_foot_to_right_ankle_to_heel',
    21: 'left_foot_to_left_lower_leg',
    22: 'left_foot_to_left_ankle_to_heel',
    23: 'left_foot_to_left_toes',
    24: 'torso_to_right_shoulder',
    25: 'torso_to_left_shoulder',
    26: 'torso_to_nose_to_neck',
    27: 'torso_to_right_hip',
    28: 'torso_to_left_hip'
}

def get_thumbnail(path):
    path = '{}{}'.format(THUMBNAIL_PATH, path)
    i = Image.open(path)
    i.thumbnail((100, 100), Image.LANCZOS)
    buff = BytesIO()
    i.save(buff, format="PNG")
    encoded_image = base64.b64encode(buff.getvalue()).decode('UTF-8')
    return (html.Img(src='data:image/png;base64,{}'.format(encoded_image)))

# image = get_thumbnail('thumb.png')
# BODYPART_THUMBS = [
#     image,
#     image,
#     image,
#     image,
#     image,
#     image,
#     image,
#     image,
#     image,
#     image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
#      image,
# ]

BODYPART_THUMBS = [
    '![myImage-1](assets/thumbnails/nose_to_neck_to_left_shoulder.png)',
    '![myImage-2](assets/thumbnails/nose_to_neck_to_right_shoulder.png)',
    '![myImage-3](assets/thumbnails/left_shoulder_to_right_shoulder.png)',
    '![myImage-4](assets/thumbnails/left_shoulder_to_left_upper_arm.png)',
    '![myImage-5](assets/thumbnails/left_lower_arm_to_left_upper_arm.png)',
    '![myImage-6](assets/thumbnails/right_upper_arm_to_right_shoulder.png)',
    '![myImage-7](assets/thumbnails/right_upper_arm_to_right_lower_arm.png)',
    '![myImage-8](assets/thumbnails/left_eye_to_nose_to_left_ear_to_eye.png)',
    '![myImage-9](assets/thumbnails/left_eye_to_nose_to_neck.png)',
    '![myImage-10](assets/thumbnails/nose_to_neck_to_right_eye_to_nose.png)',
    '![myImage-11](assets/thumbnails/left_eye_to_nose_to_right_ear_to_eye.png)',
    '![myImage-12](assets/thumbnails/right_eye_to_nose_to_right_ear_to_eye.png)',
    '![myImage-13](assets/thumbnails/right_hip_to_right_upper_leg.png)',
    '![myImage-14](assets/thumbnails/right_upper_leg_to_right_lower_leg.png)',
    '![myImage-15](assets/thumbnails/left_hip_to_left_upper_leg.png)',
    '![myImage-16](assets/thumbnails/left_upper_leg_to_left_lower_leg.png)',
    '![myImage-17](assets/thumbnails/left_lower_leg_left_ankle_to_heel.png)',
    '![myImage-18](assets/thumbnails/right_lower_leg_to_right_ankle_to_heel.png)',
    '![myImage-19](assets/thumbnails/right_foot_to_right_toes.png)',
    '![myImage-20](assets/thumbnails/right_foot_to_right_lower_leg.png)',
    '![myImage-21](assets/thumbnails/right_foot_to_right_ankle_to_heel.png)',
    '![myImage-22](assets/thumbnails/left_foot_to_left_lower_leg.png)',
    '![myImage-23](assets/thumbnails/left_foot_to_left_ankle_to_heel.png)',
    '![myImage-24](assets/thumbnails/left_foot_to_left_toes.png)',
    '![myImage-25](assets/thumbnails/torso_to_right_shoulder.png)',
    '![myImage-26](assets/thumbnails/torso_to_left_shoulder.png)',
    '![myImage-27](assets/thumbnails/torso_to_nose_to_neck.png)',
    '![myImage-28](assets/thumbnails/torso_to_right_hip.png)',
    '![myImage-29](assets/thumbnails/torso_to_left_hip.png)'
    ]
