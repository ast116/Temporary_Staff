-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 26 jan. 2025 à 16:09
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `vacataire`
--

-- --------------------------------------------------------

--
-- Structure de la table `cours`
--

DROP TABLE IF EXISTS `cours`;
CREATE TABLE IF NOT EXISTS `cours` (
  `idc` int NOT NULL AUTO_INCREMENT,
  `vacataire_c` int NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `objectif` varchar(100) NOT NULL,
  `heures_prevues` int NOT NULL,
  PRIMARY KEY (`idc`),
  KEY `ck_vacataire` (`vacataire_c`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `cours`
--

INSERT INTO `cours` (`idc`, `vacataire_c`, `matiere`, `objectif`, `heures_prevues`) VALUES
(1, 1, 'Python / React Native', 'Cas Pratique de la programmation + Projet en fin de session', 65),
(2, 2, 'Laravel / Wordpresse-Joomla', 'Initiation du monde web et création de site basique', 50),
(3, 3, 'CCNA1 / CCNA2', 'Etre capable d\'administrer le réseau d\'entités', 50),
(5, 5, 'v', 'v', 2);

-- --------------------------------------------------------

--
-- Structure de la table `heures`
--

DROP TABLE IF EXISTS `heures`;
CREATE TABLE IF NOT EXISTS `heures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `vacataire_h` int NOT NULL,
  `cours_h` int NOT NULL,
  `Debut_Travail` date NOT NULL,
  `Fin_Travail` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vacataire` (`vacataire_h`),
  KEY `hk_cours` (`cours_h`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `heures`
--

INSERT INTO `heures` (`id`, `vacataire_h`, `cours_h`, `Debut_Travail`, `Fin_Travail`) VALUES
(1, 1, 0, '2025-01-01', '2025-06-12'),
(2, 2, 0, '2025-02-14', '2025-05-20'),
(3, 3, 0, '2025-01-26', '2025-05-01');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `username`, `password`) VALUES
(1, 'uin', 'uin'),
(2, 'ahmed', '1234');

-- --------------------------------------------------------

--
-- Structure de la table `vacataires`
--

DROP TABLE IF EXISTS `vacataires`;
CREATE TABLE IF NOT EXISTS `vacataires` (
  `idv` int NOT NULL AUTO_INCREMENT,
  `nom_prenom` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `telephone` int NOT NULL,
  `activite_principale` varchar(30) NOT NULL,
  `date_inscription` date NOT NULL,
  PRIMARY KEY (`idv`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `vacataires`
--

INSERT INTO `vacataires` (`idv`, `nom_prenom`, `email`, `telephone`, `activite_principale`, `date_inscription`) VALUES
(1, 'Modagara Ahmed', 'ahmed@gmail.com', 77770000, 'Data Analyst', '2024-10-07'),
(2, 'Soumana Ibrahim', 'bramaroot@gmail.com', 88885555, 'Web-dev / Designer', '2021-02-01'),
(3, 'Aissata Diallo', 'diallo@gmail.com', 11112222, 'Administrateur Réseau', '2019-08-15');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
