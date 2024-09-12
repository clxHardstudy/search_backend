CREATE TABLE `checkinfo` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(255) DEFAULT NULL COMMENT '姓名',
  `first_checkin` int DEFAULT NULL COMMENT '上班打卡',
  `second_checkin` int DEFAULT NULL COMMENT '下班打卡',
  `workinghours` int DEFAULT NULL COMMENT '工时',
  `state` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '状态\n0:工作中\n1:加班\n2:早退',
  `staff_id` int DEFAULT NULL COMMENT '员工id',
  PRIMARY KEY (`id`),
  KEY `ix_checkinfo_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `staff` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(255) DEFAULT NULL,
  `create_time` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password_hash` varchar(255) DEFAULT NULL COMMENT '哈希密码',
  `auth_token` varchar(255) DEFAULT NULL COMMENT '登录token',
  `create_time` int DEFAULT NULL COMMENT '创建时间',
  `update_time` int DEFAULT NULL COMMENT '更新时间',
  `last_login` int DEFAULT NULL COMMENT '最近时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `ix_user_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;