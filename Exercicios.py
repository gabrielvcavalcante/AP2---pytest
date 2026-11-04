import re

def classificar_produto(quantidade):
    if quantidade < 0:
        return "Quantidade inválida"
    elif quantidade == 0:
        return "Sem estoque"
    elif 1 <= quantidade <= 5:
        return "Estoque baixo"
    elif 6 <= quantidade <= 20:
        return "Estoque normal"
    else:
        return "Estoque alto"

def inverter_palavras(texto):
    if not texto:
        return ""
    return " ".join(texto.split()[::-1])

def validar_documento(documento):
    doc_limpo = re.sub(r'[.-]', '', str(documento))
    if not doc_limpo.isdigit():
        return False
    return len(doc_limpo) == 11

def gerar_codigo():
    return "USR-0000"

def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."

def verificar_permissao(usuario):
    return False

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"

def obter_proximo_cliente():
    return None

def registrar_atendimento(cliente):
    return False

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if not cliente:
        return "Fila vazia"
    if registrar_atendimento(cliente):
        return "Atendimento realizado"
    return "Falha no atendimento"
