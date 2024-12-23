/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : student_info

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 23/12/2024 13:21:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '账号',
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `role` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '角色',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='管理员表';

-- ----------------------------
-- Records of admin
-- ----------------------------
BEGIN;
INSERT INTO `admin` VALUES (1, 'admin', '$2b$12$s2IiNxWm2SmteLZKaSZGqOU5XKulRX3mYM606d2QfRu7LtDRCd1N2', '管理员', 'ADMIN');
COMMIT;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '课程ID',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '课程名称',
  `number` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '课程编号',
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '课程描述',
  `periods` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '课时',
  `teacher` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '任课老师',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='课程信息';

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
INSERT INTO `course` VALUES (1, '大学英语', 'cs-001', '大学英语很简单-6学分', '36课时', '张三');
INSERT INTO `course` VALUES (2, '高等数学', 'cs-002', '高等数学很难学-4学分', '24课时', '李四');
INSERT INTO `course` VALUES (3, '必修物理', 'cs-003', '必修物理有难度-2学分', '24课时', '王五');
INSERT INTO `course` VALUES (4, '思想政治', 'cs-004', '思想政治必修课-4学分', '18课时', '赵六');
INSERT INTO `course` VALUES (5, '微机原理', 'cs-005', '微机原理很基础-3学分', '24课时', '钱七');
INSERT INTO `course` VALUES (6, '通信原理', 'cs-006', '通信原理很难懂-4学分', '24课时', '孙八');
INSERT INTO `course` VALUES (7, '离散数学', 'cs-007', '离散数学太抽象-2学分', '18课时', '周九');
INSERT INTO `course` VALUES (8, '工程制图', 'cs-008', '工程制图好有趣-3学分', '24课时', '吴十');
INSERT INTO `course` VALUES (9, 'FastAPI从零入门', 'cs-009', '该门课程从零开始-3学分', '32课时', 'Zachary');
COMMIT;

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '学生成绩表主键ID',
  `course_id` int(11) DEFAULT NULL COMMENT '课程ID',
  `student_id` int(11) DEFAULT NULL COMMENT '学生ID',
  `score` double(10,1) DEFAULT NULL COMMENT '成绩',
  `comment` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '教师评语',
  `feedback` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '学生评价',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='学生成绩表';

-- ----------------------------
-- Records of grade
-- ----------------------------
BEGIN;
INSERT INTO `grade` VALUES (2, 9, 1, 99.0, '很棒', '老师很nice');
INSERT INTO `grade` VALUES (3, 9, 2, 99.0, '1', NULL);
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '学生表主键ID',
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '学号/用户名',
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '学生姓名',
  `gender` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `phone` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号',
  `birthday` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '出生日期',
  `avatar` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '头像',
  `role` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户角色',
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_pk2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='学生信息';

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES (1, '202001', '$2b$12$ElsjivXFBIVmFYfk1qSnreaAO/YL7g6jblmweEedDKsGfRDd0bFtm', '谢赟晴', '男', '15577887788', '2019-06-06', 'http://localhost:9090/files/download?filename=1716187848_91bc9549514241a88afee0813eb27639_1025119063.png', 'STUDENT');
INSERT INTO `student` VALUES (2, '202002', '$2b$12$bH0ozdeuosIZpWfEPksBcOdmMgw3F3L2bGxfo/TgLZo.AAQmeHaSG', '武泽天', '男', '13309090000', '1991-02-06', 'http://localhost:9090/files/download?filename=1716188387_ef91d37acdf1482bb8aca4f1ca5bab95.pngtplv-6bxrjdptv7-image.png', 'STUDENT');
INSERT INTO `student` VALUES (3, '202003', '$2b$12$zD2oCz8/IQ9rfOcCmZp1ReBJ4tjdYtmm6Otfp03dNr.9/PHjDQNP2', '张秦', '女', '13300008888', '2000-03-02', 'http://localhost:9090/files/download?filename=1734529599_WechatIMG1734_.jpg', 'STUDENT');
INSERT INTO `student` VALUES (5, '202004', '$2b$12$xCn/qwwnoOMYdKcOwLNNVOsH13cD8.ts90UtbcAOklbR8RMwb3t7W', '202004', NULL, NULL, NULL, NULL, 'STUDENT');
INSERT INTO `student` VALUES (6, '202005', '$2b$12$Lysr0Uf8eeZiH06KkPIIGuvYM1SX82MwfpBOfYLRob/6/OMnlLvEG', '202005', NULL, NULL, NULL, NULL, 'STUDENT');
INSERT INTO `student` VALUES (7, '202006', '$2b$12$zkU0n7qP8RyPIQySeNk8CeyDRN1764hmsuNkPXDwgI6v0eTlVUIsi', '202006', NULL, NULL, NULL, NULL, 'STUDENT');
INSERT INTO `student` VALUES (8, '202088', '$2b$12$PJ3os6YY8zUjWjwiUTu3duYInPQ2dXclFTqQmIfwff2sQYzuCAMjO', 'lixiang', '男', '13309098888', '2024-12-01', NULL, 'STUDENT');
COMMIT;

-- ----------------------------
-- Table structure for student_course
-- ----------------------------
DROP TABLE IF EXISTS `student_course`;
CREATE TABLE `student_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '选课表主键ID',
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '课程名称',
  `number` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '课程编号',
  `student_id` int(11) DEFAULT NULL COMMENT '学生ID',
  `course_id` int(11) DEFAULT NULL COMMENT '课程ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='学生选课表';

-- ----------------------------
-- Records of student_course
-- ----------------------------
BEGIN;
INSERT INTO `student_course` VALUES (4, 'FastAPI从零入门', 'cs-009', 1, 9);
INSERT INTO `student_course` VALUES (7, 'FastAPI从零入门', 'cs-009', 2, 9);
INSERT INTO `student_course` VALUES (8, '工程制图', 'cs-008', 2, 8);
INSERT INTO `student_course` VALUES (9, '离散数学', 'cs-007', 2, 7);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
