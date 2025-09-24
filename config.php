<?php
// ajuste os dados conforme criou no hPanel
const DB_HOST = 'localhost';
const DB_NAME = 'universo_db';
const DB_USER = 'universo_user';
const DB_PASS = 'SenhaForte123';

// Token para proteger a área de clientes (opcional)
const CLIENTES_TOKEN = 'chaveDeAcesso123';

function pdo() {
  static $pdo;
  if ($pdo) return $pdo;
  $dsn = 'mysql:host='.DB_HOST.';dbname='.DB_NAME.';charset=utf8mb4';
  $pdo = new PDO($dsn, DB_USER, DB_PASS, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
  ]);
  return $pdo;
}
