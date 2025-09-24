<?php
header('Content-Type: application/json; charset=utf-8');
require __DIR__.'/config.php';

$method = $_SERVER['REQUEST_METHOD'];
$action = $_GET['action'] ?? '';

try {
  if ($method === 'POST' && $action === 'enviar') {
    $input = json_decode(file_get_contents('php://input'), true) ?? [];
    $nome     = trim($input['nome']     ?? '');
    $email    = trim($input['email']    ?? '');
    $telefone = trim($input['telefone'] ?? '');
    $empresa  = trim($input['empresa']  ?? '');
    $sistema  = trim($input['sistema']  ?? '');
    $mensagem = trim($input['mensagem'] ?? '');

    if (!$nome || !$email || !$telefone || !$mensagem) {
      http_response_code(400);
      echo json_encode(['status'=>'erro','mensagem'=>'Campos obrigatórios faltando.']);
      exit;
    }

    $stmt = pdo()->prepare("INSERT INTO clientes (nome, email, telefone, empresa, sistema, mensagem) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->execute([$nome, $email, $telefone, $empresa, $sistema, $mensagem]);

    http_response_code(201);
    echo json_encode(['status'=>'sucesso']);
    exit;
  }

  if ($method === 'GET' && $action === 'mensagens') {
    if (CLIENTES_TOKEN) {
      $ok = (!empty($_COOKIE['ctok']) && $_COOKIE['ctok'] === CLIENTES_TOKEN);
      if (!$ok) { http_response_code(403); echo json_encode(['status'=>'erro','mensagem'=>'sem acesso']); exit; }
    }
    $rows = pdo()->query("SELECT * FROM clientes ORDER BY data_hora DESC")->fetchAll();
    echo json_encode($rows);
    exit;
  }

  http_response_code(404);
  echo json_encode(['status'=>'erro','mensagem'=>'rota não encontrada']);
} catch (Throwable $e) {
  http_response_code(500);
  echo json_encode(['status'=>'erro','mensagem'=>$e->getMessage()]);
}
