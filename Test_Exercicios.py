from unittest.mock import patch
import Exercicios

#Exercicio 1
def test_classificar_produto():
    assert Exercicios.classificar_produto(0) == "Sem estoque"
    assert Exercicios.classificar_produto(3) == "Estoque baixo"
    assert Exercicios.classificar_produto(10) == "Estoque normal"
    assert Exercicios.classificar_produto(25) == "Estoque alto"
    assert Exercicios.classificar_produto(-6) == "Quantidade inválida"

#Exercicio 2
def test_inverter_palavras():
    assert Exercicios.inverter_palavras("Python é muito interessante") == "interessante muito é Python"
    assert Exercicios.inverter_palavras("Olá") == "Olá"
    assert Exercicios.inverter_palavras("") == ""
    assert Exercicios.inverter_palavras("  muitos   espaços  ") == "espaços muitos"
    assert Exercicios.inverter_palavras("Python é 10") == "10 é Python"

#Exercicio 3
def test_validar_documento():
    assert Exercicios.validar_documento("12345678901") is True
    assert Exercicios.validar_documento("123.456.789-01") is True
    assert Exercicios.validar_documento("1234567890") is False
    assert Exercicios.validar_documento("123456789012") is False
    assert Exercicios.validar_documento("123.456.789-XX") is False
    assert Exercicios.validar_documento("") is False

#Exercicio 4
@patch('Exercicios.gerar_codigo')
def test_criar_identificacao(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    assert Exercicios.criar_identificacao("Carlos") == "Usuário Carlos cadastrado com código USR-1234."
    mock_gerar_codigo.assert_called_once()
    
    mock_gerar_codigo.return_value = "USR-9999"
    assert Exercicios.criar_identificacao("Ana") == "Usuário Ana cadastrado com código USR-9999."

#Exercicio 5
@patch('Exercicios.verificar_permissao')
def test_acessar_sistema(mock_verificar_permissao):
    mock_verificar_permissao.return_value = True
    assert Exercicios.acessar_sistema("joao") == "Acesso autorizado"
    mock_verificar_permissao.assert_called_with("joao")
    
    mock_verificar_permissao.return_value = False
    assert Exercicios.acessar_sistema("maria") == "Acesso negado"
    mock_verificar_permissao.assert_called_with("maria")

#Exercico 6
@patch('Exercicios.registrar_atendimento')
@patch('Exercicios.obter_proximo_cliente')
def test_atender_proximo_cliente(mock_obter, mock_registrar):
    mock_obter.return_value = "Cliente A"
    mock_registrar.return_value = True
    assert Exercicios.atender_proximo_cliente() == "Atendimento realizado"
    mock_obter.assert_called()
    mock_registrar.assert_called_with("Cliente A")
    
    mock_registrar.reset_mock()
    mock_obter.return_value = None
    assert Exercicios.atender_proximo_cliente() == "Fila vazia"
    mock_registrar.assert_not_called()
    
    mock_obter.return_value = "Cliente B"
    mock_registrar.return_value = False
    assert Exercicios.atender_proximo_cliente() == "Falha no atendimento"
