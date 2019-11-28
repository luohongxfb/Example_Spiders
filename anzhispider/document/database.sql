# 建库
CREATE DATABASE app_anzhigame CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


USE app_anzhigame;
DROP TABLE games;

# 建表
CREATE TABLE games(
  id INTEGER(11)  UNSIGNED AUTO_INCREMENT COLLATE utf8mb4_general_ci,
  name VARCHAR(20) NOT NULL COLLATE utf8mb4_general_ci COMMENT '游戏名' ,
  versionCode VARCHAR(10) COLLATE utf8mb4_general_ci COMMENT '版本号' NOT NULL DEFAULT 'v1.0',
  icon VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '游戏图标icon' NOT NULL DEFAULT '',
  type VARCHAR(20) COLLATE utf8mb4_general_ci COMMENT '分类' NOT NULL DEFAULT '',
  onlineTime VARCHAR(20) COLLATE utf8mb4_general_ci COMMENT '上线时间',
  size VARCHAR(10) COLLATE utf8mb4_general_ci COMMENT '大小' NOT NULL DEFAULT '0B',
  download VARCHAR(10) COLLATE utf8mb4_general_ci COMMENT '下载量' NOT NULL DEFAULT '0',
  author VARCHAR(20) COLLATE utf8mb4_general_ci COMMENT '作者',
  intro VARCHAR(1500) COLLATE utf8mb4_general_ci COMMENT '简介',
  updateInfo VARCHAR(1500) COLLATE utf8mb4_general_ci COMMENT '更新说明',
  highlight VARCHAR(1500) COLLATE utf8mb4_general_ci COMMENT '精彩内容',
  image1 VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '市场图1',
  image2 VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '市场图2',
  image3 VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '市场图3',
  image4 VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '市场图4',
  image5 VARCHAR(100) COLLATE utf8mb4_general_ci COMMENT '市场图5',
  link VARCHAR(200) COLLATE utf8mb4_general_ci COMMENT '爬取链接',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE current_timestamp,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '安智市场爬取游戏列表';


