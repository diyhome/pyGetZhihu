-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2020-02-02 05:08:15
-- 服务器版本： 10.4.11-MariaDB
-- PHP 版本： 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `zhihu`
--

-- --------------------------------------------------------

--
-- 表的结构 `category`
--

CREATE TABLE `category` (
  `cid` int(11) NOT NULL COMMENT '分类id',
  `cname` text DEFAULT NULL COMMENT '分类名',
  `count` int(10) UNSIGNED DEFAULT NULL COMMENT '引用计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='所属分类';

-- --------------------------------------------------------

--
-- 表的结构 `press_sentence`
--

CREATE TABLE `press_sentence` (
  `id` int(11) NOT NULL COMMENT 'id',
  `category_id` int(11) DEFAULT NULL COMMENT '分类键',
  `sentence_id` int(11) DEFAULT NULL COMMENT '句子键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='关联表';

-- --------------------------------------------------------

--
-- 表的结构 `sentence`
--

CREATE TABLE `sentence` (
  `sid` int(11) NOT NULL COMMENT '句子id',
  `content` text DEFAULT NULL COMMENT '句子内容',
  `howfrom` text DEFAULT NULL COMMENT '句子出处',
  `hot` int(10) UNSIGNED NOT NULL COMMENT '句子热度',
  `author` text DEFAULT NULL COMMENT '句子作者'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='句子记录';

--
-- 转储表的索引
--

--
-- 表的索引 `category`
--
ALTER TABLE `category`
  ADD KEY `cid` (`cid`);

--
-- 表的索引 `press_sentence`
--
ALTER TABLE `press_sentence`
  ADD KEY `id` (`id`),
  ADD KEY `cid` (`category_id`),
  ADD KEY `sid` (`sentence_id`);

--
-- 表的索引 `sentence`
--
ALTER TABLE `sentence`
  ADD KEY `sid` (`sid`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `category`
--
ALTER TABLE `category`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT COMMENT '分类id';

--
-- 使用表AUTO_INCREMENT `press_sentence`
--
ALTER TABLE `press_sentence`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id';

--
-- 使用表AUTO_INCREMENT `sentence`
--
ALTER TABLE `sentence`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT COMMENT '句子id';

--
-- 限制导出的表
--

--
-- 限制表 `press_sentence`
--
ALTER TABLE `press_sentence`
  ADD CONSTRAINT `cid` FOREIGN KEY (`category_id`) REFERENCES `category` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sid` FOREIGN KEY (`sentence_id`) REFERENCES `sentence` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
