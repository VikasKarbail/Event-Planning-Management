-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2023 at 03:46 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` text DEFAULT NULL,
  `password` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin'),
('admin', 'admin'),
('admin', 'admin'),
('admin', 'admin'),
('admin123', 'admin123'),
('admin123', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `birthday`
--

CREATE TABLE `birthday` (
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `event_date` date NOT NULL,
  `message` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `birthday`
--

INSERT INTO `birthday` (`name`, `email`, `phone`, `place`, `event_date`, `message`) VALUES
('suhas', 'suhas@gmail.com', 1234567890, 'bengal', '2023-09-10', 'cgfghfhg'),
('Spoorthi O', 'suhas@gmail.com', 2147483647, 'chitradurga', '2023-09-10', 'sugas');

-- --------------------------------------------------------

--
-- Table structure for table `corporate`
--

CREATE TABLE `corporate` (
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(11) NOT NULL,
  `place` varchar(100) NOT NULL,
  `event_date` date NOT NULL,
  `message` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `corporate`
--

INSERT INTO `corporate` (`name`, `email`, `phone`, `place`, `event_date`, `message`) VALUES
('0', '0', 1234567890, '0', '0000-00-00', '0'),
('suhas', 'spoorthiospoorthi204@gmail.com', 1234567890, 'xnmnc', '2023-09-17', 'vzbV');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `userlog`
--

CREATE TABLE `userlog` (
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(11) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userlog`
--

INSERT INTO `userlog` (`username`, `email`, `phone`, `password`) VALUES
('suhas123', 'spoorthiospoorthi204@gmail.com', 123456767, 'suhas123'),
('admin', 'spoorthiospoorthi204@gmail.com', 0, '123'),
('suhas12', 'su@gmail.com', 123456767, '1234'),
('admin123', 'spoorthiospoorthi204@gmail.com', 123456767, '1234'),
('su1234', 'suhaso2002@gmail.com', 2147483647, '12345'),
('ravi1234', 'ravi@gmail.com', 123456767, '1234'),
('ravi1234', 'ravi@gmail.com', 123456767, '1234'),
('raju1234', 'suhas@gmail.com', 2147483647, '1234');

-- --------------------------------------------------------

--
-- Table structure for table `wedding`
--

CREATE TABLE `wedding` (
  `hname` varchar(100) NOT NULL,
  `wname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int(100) NOT NULL,
  `event_date` date NOT NULL,
  `message` varchar(100) NOT NULL,
  `k` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wedding`
--

INSERT INTO `wedding` (`hname`, `wname`, `email`, `phone`, `event_date`, `message`, `k`) VALUES
('bajkxb', 'xbajkxb', 'spoorthiospoorthi204@gmail.com', 1234567890, '2023-09-05', 'xHSVXHJVXHJV', 'on'),
('bajkxb', 'xbajkxb', 'spoorthiospoorthi204@gmail.com', 1234567890, '2023-09-05', 'xHSVXHJVXHJV', 'on'),
('raju', 'rani', 'ravi@gmail.com', 123456767, '2023-08-27', 'wedding should be arrenged in grand', 'on, on, on'),
('raju n', 'rani p', 'abc@gmail.com', 2147483647, '2023-09-04', 'wedding should be arrenged in a grand', 'on');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
