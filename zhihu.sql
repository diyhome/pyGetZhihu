-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-02-01 15:32:17
-- 服务器版本： 5.5.62-log
-- PHP 版本： 7.3.11

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
  `cname` text NOT NULL COMMENT '分类名',
  `count` int(11) NOT NULL COMMENT '引用计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `press_sentence`
--

CREATE TABLE `press_sentence` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `sentence_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `sentence`
--

CREATE TABLE `sentence` (
  `sid` int(11) NOT NULL COMMENT '句子id',
  `content` longtext CHARACTER SET utf8 NOT NULL COMMENT '内容',
  `howfrom` text NOT NULL COMMENT '出处',
  `hot` int(11) NOT NULL COMMENT '热度',
  `author` text NOT NULL COMMENT '作者'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转储表的索引
--

--
-- 表的索引 `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- 表的索引 `press_sentence`
--
ALTER TABLE `press_sentence`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `sentence_id` (`sentence_id`);

--
-- 表的索引 `sentence`
--
ALTER TABLE `sentence`
  ADD PRIMARY KEY (`sid`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `press_sentence`
--
ALTER TABLE `press_sentence`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 限制导出的表
--

--
-- 限制表 `press_sentence`
--
ALTER TABLE `press_sentence`
  ADD CONSTRAINT `press_sentence_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `press_sentence_ibfk_2` FOREIGN KEY (`sentence_id`) REFERENCES `sentence` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
