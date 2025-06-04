from datetime import date
from typing import List, Dict

class Control_Agendamento:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self) -> None:
        """Cria a tabela agendamentos no banco (se não existir)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_entrada TEXT NOT NULL,
                data_saida TEXT NOT NULL,
                cliente_cpf TEXT NOT NULL,
                numero_quarto INTEGER NOT NULL,
                FOREIGN KEY (cliente_cpf) REFERENCES clientes(cpf),
                FOREIGN KEY (numero_quarto) REFERENCES quartos(numero_quarto)
            );
        """)
        self.conn.commit()

    def adicionar_agendamento(self, data_entrada: date, data_saida: date, cpf: str, numero_quarto: int) -> int:
        """Adiciona um novo agendamento e retorna o id criado"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO agendamentos (data_entrada, data_saida, cliente_cpf, numero_quarto) VALUES (?, ?, ?, ?)",
            (data_entrada, data_saida, cpf, numero_quarto)
        )
        self.conn.commit()
        return cursor.lastrowid

    def remover_agendamento(self, agendamento_id: int) -> None:
        """Remove um agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (agendamento_id,))
        self.conn.commit()

    def listar_agendamentos(self):
        cursor = self.conn.cursor()
        query = '''
            SELECT 
                ag.id,
                ag.data_entrada,
                ag.data_saida,
                cl.nome AS cliente_nome,
                qt.numero_quarto,
                tp.nome AS tipo_quarto
            FROM agendamentos ag
            JOIN clientes cl ON ag.cliente_cpf = cl.cpf
            JOIN quartos qt ON ag.numero_quarto = qt.numero_quarto
            JOIN tipos tp ON qt.tipo_id = tp.id
        '''
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado

    def carregar_dados(self) -> List[Dict]:
        """Carrega dados formatados para a interface"""
        agendamentos = self.listar_agendamentos()
        dados_formatados = []
        for ag in agendamentos:
            dados_formatados.append({
                "id": ag["id"],
                "nome": ag["cliente_nome"],
                "data": f"{ag['data_entrada']} a {ag['data_saida']}",
                "quarto": f"{ag['numero_quarto']} - {ag['tipo_quarto']}"
            })
        return dados_formatados

    def atualizar_agendamento(self, id_agendamento: int, data_entrada: date, data_saida: date, cpf: str, numero_quarto: int) -> None:
        """Atualiza os dados do agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE agendamentos
            SET data_entrada = ?, data_saida = ?, cliente_cpf = ?, numero_quarto = ?
            WHERE id = ?
        """, (data_entrada, data_saida, cpf, numero_quarto, id_agendamento))
        self.conn.commit()
