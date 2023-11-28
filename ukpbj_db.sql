-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2023 at 04:35 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ukpbj_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `pekerjaan`
--

CREATE TABLE `pekerjaan` (
  `uuid` BINARY(16) NOT NULL PRIMARY KEY UNIQUE,
  `nama_unit` varchar(128) DEFAULT NULL,
  `nama_pekerjaan` varchar(255) DEFAULT NULL,
  `pagu` varchar(13) DEFAULT NULL,
  `tgl_pengajuan` datetime DEFAULT NULL,
  `nama_ppk` varchar(255) DEFAULT NULL,
  `kak` varchar(255) DEFAULT NULL,
  `hps` varchar(255) DEFAULT NULL,
  `spesifikasi_teknis` varchar(255) DEFAULT NULL,
  `r_kontrak` varchar(255) DEFAULT NULL,
  `dokum_penyedia` varchar(255) DEFAULT NULL,
  `data_pemilihan` varchar(255) DEFAULT NULL,
  `daftar_harga` varchar(255) DEFAULT NULL,
  `jadwal` varchar(255) DEFAULT NULL,
  `rancangan_kerja` varchar(255) DEFAULT NULL,
  `dc_studi_kelayakan` varchar(255) DEFAULT NULL,
  `dc_penawaran` varchar(255) DEFAULT NULL,
  `surat_penawaran` varchar(255) DEFAULT NULL,
  `sertifikat` varchar(255) DEFAULT NULL,
  `ba_pemberian` varchar(255) DEFAULT NULL,
  `ba_pengumuman` varchar(255) DEFAULT NULL,
  `ba_sanggah` varchar(255) DEFAULT NULL,
  `ba_penetapan` varchar(255) DEFAULT NULL,
  `laporan_hasil` varchar(255) DEFAULT NULL,
  `dc_kontrak` varchar(255) DEFAULT NULL,
  `surat_pemerintah` varchar(255) DEFAULT NULL,
  `surat_jaminan` varchar(255) DEFAULT NULL,
  `surat_jamninan_uang` varchar(255) DEFAULT NULL,
  `surat_jamninan_pemeliharaan` varchar(255) DEFAULT NULL,
  `surat_tagihan` varchar(255) DEFAULT NULL,
  `surat_pesanan_epurchasing` varchar(255) DEFAULT NULL,
  `surat_perintah_membayar` varchar(255) DEFAULT NULL,
  `surat_perintah_pencairan_dana` varchar(255) DEFAULT NULL,
  `laporan_pelaksanaan` varchar(255) DEFAULT NULL,
  `laporan_penyelesaian` varchar(255) DEFAULT NULL,
  `ba_pemeriksa_hasil` varchar(255) DEFAULT NULL,
  `ba_serah_terima_sementara` varchar(255) DEFAULT NULL,
  `ba_serah_terima` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `no_induk` varchar(128) NOT NULL,
  `password` varchar(64) NOT NULL,
  `nama` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pekerjaan`
--
ALTER TABLE `pekerjaan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pekerjaan`
--
ALTER TABLE `pekerjaan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
