-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.32 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win32
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 authbase 的数据库结构
CREATE DATABASE IF NOT EXISTS `authbase` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `authbase`;

-- 导出  表 authbase.syonline 结构
CREATE TABLE IF NOT EXISTS `syonline` (
  `ID` varchar(36) NOT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `IP` varchar(100) DEFAULT NULL,
  `LOGINNAME` varchar(100) DEFAULT NULL,
  `TYPE` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syonline 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `syonline` DISABLE KEYS */;
/*!40000 ALTER TABLE `syonline` ENABLE KEYS */;

-- 导出  表 authbase.syorganization 结构
CREATE TABLE IF NOT EXISTS `syorganization` (
  `ID` varchar(36) NOT NULL,
  `ADDRESS` varchar(200) DEFAULT NULL,
  `CODE` varchar(200) DEFAULT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `ICONCLS` varchar(100) DEFAULT NULL,
  `NAME` varchar(200) DEFAULT NULL,
  `SEQ` int(11) DEFAULT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  `SYORGANIZATION_ID` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_acf7qlb04quthktalwx8c7q69` (`SYORGANIZATION_ID`),
  CONSTRAINT `FK_acf7qlb04quthktalwx8c7q69` FOREIGN KEY (`SYORGANIZATION_ID`) REFERENCES `syorganization` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syorganization 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `syorganization` DISABLE KEYS */;
INSERT INTO `syorganization` (`ID`, `ADDRESS`, `CODE`, `CREATEDATETIME`, `ICONCLS`, `NAME`, `SEQ`, `UPDATEDATETIME`, `SYORGANIZATION_ID`) VALUES
	('0', NULL, NULL, '2016-11-28 10:34:54', 'ext-icon-bricks', '总部', 100, '2016-11-28 10:35:12', NULL);
/*!40000 ALTER TABLE `syorganization` ENABLE KEYS */;

-- 导出  表 authbase.syorganization_syresource 结构
CREATE TABLE IF NOT EXISTS `syorganization_syresource` (
  `SYRESOURCE_ID` varchar(36) NOT NULL,
  `SYORGANIZATION_ID` varchar(36) NOT NULL,
  PRIMARY KEY (`SYORGANIZATION_ID`,`SYRESOURCE_ID`),
  KEY `FK_acpjp8a7fjo0cnn02eb0ia6uf` (`SYORGANIZATION_ID`),
  KEY `FK_m4mfglk7odi78d8pk9pif44vc` (`SYRESOURCE_ID`),
  CONSTRAINT `FK_acpjp8a7fjo0cnn02eb0ia6uf` FOREIGN KEY (`SYORGANIZATION_ID`) REFERENCES `syorganization` (`ID`),
  CONSTRAINT `FK_m4mfglk7odi78d8pk9pif44vc` FOREIGN KEY (`SYRESOURCE_ID`) REFERENCES `syresource` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syorganization_syresource 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `syorganization_syresource` DISABLE KEYS */;
/*!40000 ALTER TABLE `syorganization_syresource` ENABLE KEYS */;

-- 导出  表 authbase.syresource 结构
CREATE TABLE IF NOT EXISTS `syresource` (
  `ID` varchar(36) NOT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `DESCRIPTION` varchar(200) DEFAULT NULL,
  `ICONCLS` varchar(100) DEFAULT NULL,
  `NAME` varchar(100) NOT NULL,
  `SEQ` int(11) DEFAULT NULL,
  `TARGET` varchar(100) DEFAULT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  `URL` varchar(200) DEFAULT NULL,
  `SYRESOURCE_ID` varchar(36) DEFAULT NULL,
  `SYRESOURCETYPE_ID` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_n8kk2inhw4y4gax3nra2etfup` (`SYRESOURCE_ID`),
  KEY `FK_93qfpiiuk3rwb32gc5mcmmlgh` (`SYRESOURCETYPE_ID`),
  CONSTRAINT `FK_93qfpiiuk3rwb32gc5mcmmlgh` FOREIGN KEY (`SYRESOURCETYPE_ID`) REFERENCES `syresourcetype` (`ID`),
  CONSTRAINT `FK_n8kk2inhw4y4gax3nra2etfup` FOREIGN KEY (`SYRESOURCE_ID`) REFERENCES `syresource` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syresource 的数据：~32 rows (大约)
/*!40000 ALTER TABLE `syresource` DISABLE KEYS */;
INSERT INTO `syresource` (`ID`, `CREATEDATETIME`, `DESCRIPTION`, `ICONCLS`, `NAME`, `SEQ`, `TARGET`, `UPDATEDATETIME`, `URL`, `SYRESOURCE_ID`, `SYRESOURCETYPE_ID`) VALUES
	('jgbj', '2015-08-25 10:34:53', '编辑机构', 'ext-icon-bullet_wrench', '编辑机构', 2, '', '2015-08-25 10:34:53', '/base/syorganization!update', 'jggl', '1'),
	('jgck', '2015-08-25 10:34:53', '查看机构', 'ext-icon-bullet_wrench', '查看机构', 4, '', '2015-08-25 10:34:53', '/base/syorganization!getById', 'jggl', '1'),
	('jggl', '2015-08-25 10:34:53', '管理系统中用户的机构', 'ext-icon-group_link', '机构管理', 3, '', '2015-08-25 10:34:53', '/securityJsp/base/Syorganization.jsp', 'xtgl', '0'),
	('jglb', '2015-08-25 10:34:53', '查询机构列表', 'ext-icon-bullet_wrench', '机构列表', 0, '', '2016-11-28 14:09:52', '/base/syorganization!treeGrid', 'jggl', '1'),
	('jgsc', '2015-08-25 10:34:53', '删除机构', 'ext-icon-bullet_wrench', '删除机构', 3, '', '2015-08-25 10:34:53', '/base/syorganization!delete', 'jggl', '1'),
	('jgsq', '2015-08-25 10:34:53', '机构授权', 'ext-icon-bullet_wrench', '机构授权', 5, '', '2015-08-25 10:34:53', '/base/syorganization!grant', 'jggl', '1'),
	('jgtj', '2015-08-25 10:34:53', '添加机构', 'ext-icon-bullet_wrench', '添加机构', 1, '', '2015-08-25 10:34:53', '/base/syorganization!save', 'jggl', '1'),
	('jsbj', '2015-08-25 10:34:53', '编辑角色', 'ext-icon-bullet_wrench', '编辑角色', 2, '', '2015-08-25 10:34:53', '/base/syrole!update', 'jsgl', '1'),
	('jsck', '2015-08-25 10:34:53', '查看角色', 'ext-icon-bullet_wrench', '查看角色', 4, '', '2015-08-25 10:34:53', '/base/syrole!getById', 'jsgl', '1'),
	('jsgl', '2015-08-25 10:34:53', '管理系统中用户的角色', 'ext-icon-tux', '角色管理', 2, '', '2015-08-25 10:34:53', '/securityJsp/base/Syrole.jsp', 'xtgl', '0'),
	('jslb', '2015-08-25 10:34:53', '查询角色列表', 'ext-icon-bullet_wrench', '角色列表', 0, '', '2015-08-25 10:34:53', '/base/syrole!grid', 'jsgl', '1'),
	('jssc', '2015-08-25 10:34:53', '删除角色', 'ext-icon-bullet_wrench', '删除角色', 3, '', '2015-08-25 10:34:53', '/base/syrole!delete', 'jsgl', '1'),
	('jssq', '2015-08-25 10:34:53', '角色授权', 'ext-icon-bullet_wrench', '角色授权', 5, '', '2015-08-25 10:34:53', '/base/syrole!grant', 'jsgl', '1'),
	('jstj', '2015-08-25 10:34:53', '添加角色', 'ext-icon-bullet_wrench', '添加角色', 1, '', '2015-08-25 10:34:53', '/base/syrole!save', 'jsgl', '1'),
	('online', '2015-08-25 10:34:53', '监控用户登录、注销', 'ext-icon-chart_line', '用户登录历史监控', 4, '', '2015-08-25 10:34:53', '/securityJsp/base/Syonline.jsp', 'xtjk', '0'),
	('onlineGrid', '2015-08-25 10:34:53', '用户登录、注销历史记录列表', 'ext-icon-bullet_wrench', '用户登录历史列表', 0, '', '2015-08-25 10:34:53', '/base/syonline!grid', 'online', '1'),
	('xtgl', '2015-08-25 10:34:53', '管理系统的资源、角色、机构、用户等信息', 'ext-icon-application_view_tile', '系统管理', 5, '', '2015-08-25 10:34:53', '/welcome.jsp', NULL, '0'),
	('xtjk', '2015-08-25 10:34:53', '监控系统运行情况等信息', 'ext-icon-monitor', '系统监控', 6, '', '2015-08-25 10:34:53', '/welcome.jsp', NULL, '0'),
	('yhbj', '2015-08-25 10:34:53', '编辑用户', 'ext-icon-bullet_wrench', '编辑用户', 2, '', '2015-08-25 10:34:53', '/base/syuser!update', 'yhgl', '1'),
	('yhck', '2015-08-25 10:34:53', '查看用户', 'ext-icon-bullet_wrench', '查看用户', 4, '', '2015-08-25 10:34:53', '/base/syuser!getById', 'yhgl', '1'),
	('yhgl', '2015-08-25 10:34:53', '管理系统中用户的用户', 'ext-icon-user_suit', '用户管理', 4, '', '2015-08-25 10:34:53', '/securityJsp/base/Syuser.jsp', 'xtgl', '0'),
	('yhjg', '2015-08-25 10:34:53', '编辑用户机构', 'ext-icon-bullet_wrench', '用户机构', 6, '', '2015-08-25 10:34:53', '/base/syuser!grantOrganization', 'yhgl', '1'),
	('yhjs', '2015-08-25 10:34:53', '编辑用户角色', 'ext-icon-bullet_wrench', '用户角色', 5, '', '2015-08-25 10:34:53', '/base/syuser!grantRole', 'yhgl', '1'),
	('yhlb', '2015-08-25 10:34:53', '查询用户列表', 'ext-icon-bullet_wrench', '用户列表', 0, '', '2015-08-25 10:34:53', '/base/syuser!grid', 'yhgl', '1'),
	('yhsc', '2015-08-25 10:34:53', '删除用户', 'ext-icon-bullet_wrench', '删除用户', 3, '', '2015-08-25 10:34:53', '/base/syuser!delete', 'yhgl', '1'),
	('yhtj', '2015-08-25 10:34:53', '添加用户', 'ext-icon-bullet_wrench', '添加用户', 1, '', '2015-08-25 10:34:53', '/base/syuser!save', 'yhgl', '1'),
	('zybj', '2015-08-25 10:34:53', '编辑资源', 'ext-icon-bullet_wrench', '编辑资源', 2, '', '2015-08-25 10:34:53', '/base/syresource!update', 'zygl', '1'),
	('zyck', '2015-08-25 10:34:53', '查看资源', 'ext-icon-bullet_wrench', '查看资源', 4, '', '2015-08-25 10:34:53', '/base/syresource!getById', 'zygl', '1'),
	('zygl', '2015-08-25 10:34:53', '管理系统的资源', 'ext-icon-newspaper_link', '资源管理', 1, '', '2015-08-25 10:34:53', '/securityJsp/base/Syresource.jsp', 'xtgl', '0'),
	('zylb', '2015-08-25 10:34:53', '查询资源', 'ext-icon-bullet_wrench', '资源列表', 0, '', '2015-08-25 10:34:53', '/base/syresource!treeGrid', 'zygl', '1'),
	('zysc', '2015-08-25 10:34:53', '删除资源', 'ext-icon-bullet_wrench', '删除资源', 3, '', '2015-08-25 10:34:53', '/base/syresource!delete', 'zygl', '1'),
	('zytj', '2015-08-25 10:34:53', '添加资源', 'ext-icon-bullet_wrench', '添加资源', 1, '', '2015-08-25 10:34:53', '/base/syresource!save', 'zygl', '1');
/*!40000 ALTER TABLE `syresource` ENABLE KEYS */;

-- 导出  表 authbase.syresourcetype 结构
CREATE TABLE IF NOT EXISTS `syresourcetype` (
  `ID` varchar(36) NOT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `DESCRIPTION` varchar(200) DEFAULT NULL,
  `NAME` varchar(100) NOT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syresourcetype 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `syresourcetype` DISABLE KEYS */;
INSERT INTO `syresourcetype` (`ID`, `CREATEDATETIME`, `DESCRIPTION`, `NAME`, `UPDATEDATETIME`) VALUES
	('0', '2015-08-25 10:34:53', '菜单类型会显示在系统首页左侧菜单中', '菜单', '2015-08-25 10:34:53'),
	('1', '2015-08-25 10:34:53', '功能类型不会显示在系统首页左侧菜单中', '功能', '2015-08-25 10:34:53');
/*!40000 ALTER TABLE `syresourcetype` ENABLE KEYS */;

-- 导出  表 authbase.syrole 结构
CREATE TABLE IF NOT EXISTS `syrole` (
  `ID` varchar(36) NOT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `DESCRIPTION` varchar(200) DEFAULT NULL,
  `ICONCLS` varchar(100) DEFAULT NULL,
  `NAME` varchar(100) NOT NULL,
  `SEQ` int(11) DEFAULT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syrole 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `syrole` DISABLE KEYS */;
INSERT INTO `syrole` (`ID`, `CREATEDATETIME`, `DESCRIPTION`, `ICONCLS`, `NAME`, `SEQ`, `UPDATEDATETIME`) VALUES
	('0', '2015-08-25 10:34:53', '拥有系统所有权限', NULL, '超管', 0, '2015-08-25 10:34:53'),
	('19f00d46-8f1b-45b5-b7b7-6197d7b8cb33', '2016-11-28 14:24:00', NULL, NULL, '管理员', 100, '2016-11-28 14:24:00');
/*!40000 ALTER TABLE `syrole` ENABLE KEYS */;

-- 导出  表 authbase.syrole_syresource 结构
CREATE TABLE IF NOT EXISTS `syrole_syresource` (
  `SYROLE_ID` varchar(36) NOT NULL,
  `SYRESOURCE_ID` varchar(36) NOT NULL,
  PRIMARY KEY (`SYRESOURCE_ID`,`SYROLE_ID`),
  KEY `FK_kkrartsovl2frhfvriqdi7jwl` (`SYRESOURCE_ID`),
  KEY `FK_r139h669pg4ts6mbvn3ip5472` (`SYROLE_ID`),
  CONSTRAINT `FK_kkrartsovl2frhfvriqdi7jwl` FOREIGN KEY (`SYRESOURCE_ID`) REFERENCES `syresource` (`ID`),
  CONSTRAINT `FK_r139h669pg4ts6mbvn3ip5472` FOREIGN KEY (`SYROLE_ID`) REFERENCES `syrole` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syrole_syresource 的数据：~32 rows (大约)
/*!40000 ALTER TABLE `syrole_syresource` DISABLE KEYS */;
INSERT INTO `syrole_syresource` (`SYROLE_ID`, `SYRESOURCE_ID`) VALUES
	('0', 'jgbj'),
	('0', 'jgck'),
	('0', 'jggl'),
	('0', 'jglb'),
	('0', 'jgsc'),
	('0', 'jgsq'),
	('0', 'jgtj'),
	('0', 'jsbj'),
	('0', 'jsck'),
	('0', 'jsgl'),
	('0', 'jslb'),
	('0', 'jssc'),
	('0', 'jssq'),
	('0', 'jstj'),
	('0', 'online'),
	('0', 'onlineGrid'),
	('0', 'xtgl'),
	('0', 'xtjk'),
	('0', 'yhbj'),
	('0', 'yhck'),
	('0', 'yhgl'),
	('0', 'yhjg'),
	('0', 'yhjs'),
	('0', 'yhlb'),
	('0', 'yhsc'),
	('0', 'yhtj'),
	('0', 'zybj'),
	('0', 'zyck'),
	('0', 'zygl'),
	('0', 'zylb'),
	('0', 'zysc'),
	('0', 'zytj');
/*!40000 ALTER TABLE `syrole_syresource` ENABLE KEYS */;

-- 导出  表 authbase.syuser 结构
CREATE TABLE IF NOT EXISTS `syuser` (
  `ID` varchar(36) NOT NULL,
  `AGE` int(11) DEFAULT NULL,
  `CREATEDATETIME` datetime DEFAULT NULL,
  `LOGINNAME` varchar(100) NOT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  `PHOTO` varchar(200) DEFAULT NULL,
  `PWD` varchar(100) DEFAULT NULL,
  `SEX` varchar(1) DEFAULT NULL,
  `UPDATEDATETIME` datetime DEFAULT NULL,
  `EMPLOYDATE` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UK_eiov1gsncrds3rean3dmu822p` (`LOGINNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syuser 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `syuser` DISABLE KEYS */;
INSERT INTO `syuser` (`ID`, `AGE`, `CREATEDATETIME`, `LOGINNAME`, `NAME`, `PHOTO`, `PWD`, `SEX`, `UPDATEDATETIME`, `EMPLOYDATE`) VALUES
	('0', 30, '2015-08-25 10:34:54', 'admin', '超级管理员', '', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-09-27 15:41:11', NULL);
/*!40000 ALTER TABLE `syuser` ENABLE KEYS */;

-- 导出  表 authbase.syuser_syorganization 结构
CREATE TABLE IF NOT EXISTS `syuser_syorganization` (
  `SYUSER_ID` varchar(36) NOT NULL,
  `SYORGANIZATION_ID` varchar(36) NOT NULL,
  PRIMARY KEY (`SYORGANIZATION_ID`,`SYUSER_ID`),
  KEY `FK_14ewqc5wtscac0dd5rswrm5j2` (`SYORGANIZATION_ID`),
  KEY `FK_63bdmtxwlk259id13rp4iryy` (`SYUSER_ID`),
  CONSTRAINT `FK_14ewqc5wtscac0dd5rswrm5j2` FOREIGN KEY (`SYORGANIZATION_ID`) REFERENCES `syorganization` (`ID`),
  CONSTRAINT `FK_63bdmtxwlk259id13rp4iryy` FOREIGN KEY (`SYUSER_ID`) REFERENCES `syuser` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syuser_syorganization 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `syuser_syorganization` DISABLE KEYS */;
INSERT INTO `syuser_syorganization` (`SYUSER_ID`, `SYORGANIZATION_ID`) VALUES
	('0', '0'),
	('346e8333-b644-4939-8b06-f23654963c6a', '0');
/*!40000 ALTER TABLE `syuser_syorganization` ENABLE KEYS */;

-- 导出  表 authbase.syuser_syrole 结构
CREATE TABLE IF NOT EXISTS `syuser_syrole` (
  `SYUSER_ID` varchar(36) NOT NULL,
  `SYROLE_ID` varchar(36) NOT NULL,
  PRIMARY KEY (`SYROLE_ID`,`SYUSER_ID`),
  KEY `FK_j7iwtgslc2esrjx0ptieleoko` (`SYROLE_ID`),
  KEY `FK_1pi4p5h4y5ghbs5f4gdlgn620` (`SYUSER_ID`),
  CONSTRAINT `FK_1pi4p5h4y5ghbs5f4gdlgn620` FOREIGN KEY (`SYUSER_ID`) REFERENCES `syuser` (`ID`),
  CONSTRAINT `FK_j7iwtgslc2esrjx0ptieleoko` FOREIGN KEY (`SYROLE_ID`) REFERENCES `syrole` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- 正在导出表  authbase.syuser_syrole 的数据：~3 rows (大约)
/*!40000 ALTER TABLE `syuser_syrole` DISABLE KEYS */;
INSERT INTO `syuser_syrole` (`SYUSER_ID`, `SYROLE_ID`) VALUES
	('0', '0'),
	('0', '19f00d46-8f1b-45b5-b7b7-6197d7b8cb33'),
	('346e8333-b644-4939-8b06-f23654963c6a', '19f00d46-8f1b-45b5-b7b7-6197d7b8cb33');
/*!40000 ALTER TABLE `syuser_syrole` ENABLE KEYS */;

-- 导出  函数 authbase.to_pinyin 结构
DELIMITER //
CREATE DEFINER=`root`@`localhost` FUNCTION `to_pinyin`(NAME VARCHAR(255) CHARSET gbk) RETURNS varchar(255) CHARSET gbk
BEGIN
    DECLARE mycode INT;
    DECLARE tmp_lcode VARCHAR(2) CHARSET gbk;
    DECLARE lcode INT;
    DECLARE tmp_rcode VARCHAR(2) CHARSET gbk;
    DECLARE rcode INT;
    DECLARE mypy VARCHAR(255) CHARSET gbk DEFAULT '';
    DECLARE lp INT;
    SET mycode = 0;
    SET lp = 1;
    SET NAME = HEX(NAME);
    WHILE lp < LENGTH(NAME) DO
        SET tmp_lcode = SUBSTRING(NAME, lp, 2);
        SET lcode = CAST(ASCII(UNHEX(tmp_lcode)) AS UNSIGNED); 
        SET tmp_rcode = SUBSTRING(NAME, lp + 2, 2);
        SET rcode = CAST(ASCII(UNHEX(tmp_rcode)) AS UNSIGNED); 
        IF lcode > 128 THEN
            SET mycode =65536 - lcode * 256 - rcode ;
            SELECT CONCAT(mypy,pin_yin_) INTO mypy FROM t_base_pinyin WHERE CODE_ >= ABS(mycode) ORDER BY CODE_ ASC LIMIT 1;
            SET lp = lp + 4;
        ELSE
            SET mypy = CONCAT(mypy,CHAR(CAST(ASCII(UNHEX(SUBSTRING(NAME, lp, 2))) AS UNSIGNED)));
            SET lp = lp + 2;
        END IF;
    END WHILE;
    RETURN LOWER(mypy);
END//
DELIMITER ;

-- 导出  表 authbase.t_base_pinyin 结构
CREATE TABLE IF NOT EXISTS `t_base_pinyin` (
  `pin_yin_` varchar(255) CHARACTER SET gbk NOT NULL,
  `code_` int(11) NOT NULL,
  PRIMARY KEY (`code_`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  authbase.t_base_pinyin 的数据：~396 rows (大约)
/*!40000 ALTER TABLE `t_base_pinyin` DISABLE KEYS */;
INSERT INTO `t_base_pinyin` (`pin_yin_`, `code_`) VALUES
	('zuo', 10254),
	('zun', 10256),
	('zui', 10260),
	('zuan', 10262),
	('zu', 10270),
	('zou', 10274),
	('zong', 10281),
	('zi', 10296),
	('zhuo', 10307),
	('zhun', 10309),
	('zhui', 10315),
	('zhuang', 10322),
	('zhuan', 10328),
	('zhuai', 10329),
	('zhua', 10331),
	('zhu', 10519),
	('zhou', 10533),
	('zhong', 10544),
	('zhi', 10587),
	('zheng', 10764),
	('zhen', 10780),
	('zhe', 10790),
	('zhao', 10800),
	('zhang', 10815),
	('zhan', 10832),
	('zhai', 10838),
	('zha', 11014),
	('zeng', 11018),
	('zen', 11019),
	('zei', 11020),
	('ze', 11024),
	('zao', 11038),
	('zang', 11041),
	('zan', 11045),
	('zai', 11052),
	('za', 11055),
	('yun', 11067),
	('yue', 11077),
	('yuan', 11097),
	('yu', 11303),
	('you', 11324),
	('yong', 11339),
	('yo', 11340),
	('ying', 11358),
	('yin', 11536),
	('yi', 11589),
	('ye', 11604),
	('yao', 11781),
	('yang', 11798),
	('yan', 11831),
	('ya', 11847),
	('xun', 11861),
	('xue', 11867),
	('xuan', 12039),
	('xu', 12058),
	('xiu', 12067),
	('xiong', 12074),
	('xing', 12089),
	('xin', 12099),
	('xie', 12120),
	('xiao', 12300),
	('xiang', 12320),
	('xian', 12346),
	('xia', 12359),
	('xi', 12556),
	('wu', 12585),
	('wo', 12594),
	('weng', 12597),
	('wen', 12607),
	('wei', 12802),
	('wang', 12812),
	('wan', 12829),
	('wai', 12831),
	('wa', 12838),
	('tuo', 12849),
	('tun', 12852),
	('tui', 12858),
	('tuan', 12860),
	('tu', 12871),
	('tou', 12875),
	('tong', 12888),
	('ting', 13060),
	('tie', 13063),
	('tiao', 13068),
	('tian', 13076),
	('ti', 13091),
	('teng', 13095),
	('te', 13096),
	('tao', 13107),
	('tang', 13120),
	('tan', 13138),
	('tai', 13147),
	('ta', 13318),
	('suo', 13326),
	('sun', 13329),
	('sui', 13340),
	('suan', 13343),
	('su', 13356),
	('sou', 13359),
	('song', 13367),
	('si', 13383),
	('shuo', 13387),
	('shun', 13391),
	('shui', 13395),
	('shuang', 13398),
	('shuan', 13400),
	('shuai', 13404),
	('shua', 13406),
	('shu', 13601),
	('shou', 13611),
	('shi', 13658),
	('sheng', 13831),
	('shen', 13847),
	('she', 13859),
	('shao', 13870),
	('shang', 13878),
	('shan', 13894),
	('shai', 13896),
	('sha', 13905),
	('seng', 13906),
	('sen', 13907),
	('se', 13910),
	('sao', 13914),
	('sang', 13917),
	('san', 14083),
	('sai', 14087),
	('sa', 14090),
	('ruo', 14092),
	('run', 14094),
	('rui', 14097),
	('ruan', 14099),
	('ru', 14109),
	('rou', 14112),
	('rong', 14122),
	('ri', 14123),
	('reng', 14125),
	('ren', 14135),
	('re', 14137),
	('rao', 14140),
	('rang', 14145),
	('ran', 14149),
	('qun', 14151),
	('que', 14159),
	('quan', 14170),
	('qu', 14345),
	('qiu', 14353),
	('qiong', 14355),
	('qing', 14368),
	('qin', 14379),
	('qie', 14384),
	('qiao', 14399),
	('qiang', 14407),
	('qian', 14429),
	('qia', 14594),
	('qi', 14630),
	('pu', 14645),
	('po', 14654),
	('ping', 14663),
	('pin', 14668),
	('pie', 14670),
	('piao', 14674),
	('pian', 14678),
	('pi', 14857),
	('peng', 14871),
	('pen', 14873),
	('pei', 14882),
	('pao', 14889),
	('pang', 14894),
	('pan', 14902),
	('pai', 14908),
	('pa', 14914),
	('ou', 14921),
	('o', 14922),
	('nuo', 14926),
	('nue', 14928),
	('nuan', 14929),
	('nv', 14930),
	('nu', 14933),
	('nong', 14937),
	('niu', 14941),
	('ning', 15109),
	('nin', 15110),
	('nie', 15117),
	('niao', 15119),
	('niang', 15121),
	('nian', 15128),
	('ni', 15139),
	('neng', 15140),
	('nen', 15141),
	('nei', 15143),
	('ne', 15144),
	('nao', 15149),
	('nang', 15150),
	('nan', 15153),
	('nai', 15158),
	('na', 15165),
	('mu', 15180),
	('mou', 15183),
	('mo', 15362),
	('miu', 15363),
	('ming', 15369),
	('min', 15375),
	('mie', 15377),
	('miao', 15385),
	('mian', 15394),
	('mi', 15408),
	('meng', 15416),
	('men', 15419),
	('mei', 15435),
	('me', 15436),
	('mao', 15448),
	('mang', 15454),
	('man', 15625),
	('mai', 15631),
	('ma', 15640),
	('luo', 15652),
	('lun', 15659),
	('lue', 15661),
	('luan', 15667),
	('lv', 15681),
	('lu', 15701),
	('lou', 15707),
	('long', 15878),
	('liu', 15889),
	('ling', 15903),
	('lin', 15915),
	('lie', 15920),
	('liao', 15933),
	('liang', 15944),
	('lian', 15958),
	('lia', 15959),
	('li', 16155),
	('leng', 16158),
	('lei', 16169),
	('le', 16171),
	('lao', 16180),
	('lang', 16187),
	('lan', 16202),
	('lai', 16205),
	('la', 16212),
	('kuo', 16216),
	('kun', 16220),
	('kui', 16393),
	('kuang', 16401),
	('kuan', 16403),
	('kuai', 16407),
	('kua', 16412),
	('ku', 16419),
	('kou', 16423),
	('kong', 16427),
	('keng', 16429),
	('ken', 16433),
	('ke', 16448),
	('kao', 16452),
	('kang', 16459),
	('kan', 16465),
	('kai', 16470),
	('ka', 16474),
	('jun', 16647),
	('jue', 16657),
	('juan', 16664),
	('ju', 16689),
	('jiu', 16706),
	('jiong', 16708),
	('jing', 16733),
	('jin', 16915),
	('jie', 16942),
	('jiao', 16970),
	('jiang', 16983),
	('jian', 17185),
	('jia', 17202),
	('ji', 17417),
	('huo', 17427),
	('hun', 17433),
	('hui', 17454),
	('huang', 17468),
	('huan', 17482),
	('huai', 17487),
	('hua', 17496),
	('hu', 17676),
	('hou', 17683),
	('hong', 17692),
	('heng', 17697),
	('hen', 17701),
	('hei', 17703),
	('he', 17721),
	('hao', 17730),
	('hang', 17733),
	('han', 17752),
	('hai', 17759),
	('ha', 17922),
	('guo', 17928),
	('gun', 17931),
	('gui', 17947),
	('guang', 17950),
	('guan', 17961),
	('guai', 17964),
	('gua', 17970),
	('gu', 17988),
	('gou', 17997),
	('gong', 18012),
	('geng', 18181),
	('gen', 18183),
	('gei', 18184),
	('ge', 18201),
	('gao', 18211),
	('gang', 18220),
	('gan', 18231),
	('gai', 18237),
	('ga', 18239),
	('fu', 18446),
	('fou', 18447),
	('fo', 18448),
	('feng', 18463),
	('fen', 18478),
	('fei', 18490),
	('fang', 18501),
	('fan', 18518),
	('fa', 18526),
	('er', 18696),
	('en', 18697),
	('e', 18710),
	('duo', 18722),
	('dun', 18731),
	('dui', 18735),
	('duan', 18741),
	('du', 18756),
	('dou', 18763),
	('dong', 18773),
	('diu', 18774),
	('ding', 18783),
	('die', 18952),
	('diao', 18961),
	('dian', 18977),
	('di', 18996),
	('deng', 19003),
	('de', 19006),
	('dao', 19018),
	('dang', 19023),
	('dan', 19038),
	('dai', 19212),
	('da', 19218),
	('cuo', 19224),
	('cun', 19227),
	('cui', 19235),
	('cuan', 19238),
	('cu', 19242),
	('cou', 19243),
	('cong', 19249),
	('ci', 19261),
	('chuo', 19263),
	('chun', 19270),
	('chui', 19275),
	('chuang', 19281),
	('chuan', 19288),
	('chuai', 19289),
	('chu', 19467),
	('chou', 19479),
	('chong', 19484),
	('chi', 19500),
	('cheng', 19515),
	('chen', 19525),
	('che', 19531),
	('chao', 19540),
	('chang', 19715),
	('chan', 19725),
	('chai', 19728),
	('cha', 19739),
	('ceng', 19741),
	('ce', 19746),
	('cao', 19751),
	('cang', 19756),
	('can', 19763),
	('cai', 19774),
	('ca', 19775),
	('bu', 19784),
	('bo', 19805),
	('bing', 19976),
	('bin', 19982),
	('bie', 19986),
	('biao', 19990),
	('bian', 20002),
	('bi', 20026),
	('beng', 20032),
	('ben', 20036),
	('bei', 20051),
	('bao', 20230),
	('bang', 20242),
	('ban', 20257),
	('bai', 20265),
	('ba', 20283),
	('ao', 20292),
	('ang', 20295),
	('an', 20304),
	('ai', 20317),
	('a', 20319);
/*!40000 ALTER TABLE `t_base_pinyin` ENABLE KEYS */;

-- 导出  视图 authbase.v_pinyin 结构
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `v_pinyin` (
	`id` VARCHAR(36) NOT NULL COLLATE 'gbk_chinese_ci',
	`py` VARCHAR(255) NULL COLLATE 'gbk_chinese_ci',
	`name` VARCHAR(100) NULL COLLATE 'gbk_chinese_ci'
) ENGINE=MyISAM;

-- 导出  视图 authbase.v_pinyin 结构
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `v_pinyin`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` VIEW `v_pinyin` AS SELECT
    u.id,
    to_pinyin (u.name) AS py,
    u.name
FROM
    syuser u ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
