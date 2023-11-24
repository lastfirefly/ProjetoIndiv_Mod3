import mysql.connector
from faker import Faker
import random

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="RESILIADATA"
)

cursor = conn.cursor()

# Instância do Faker
fake = Faker()

# Preencher a tabela Areas
for i in range(1, 6):  # Inserir 5 áreas
    area_nome = fake.word()
    cursor.execute("INSERT INTO Areas (AreaID, NomeArea) VALUES (%s, %s)", (i, area_nome))

# Preencher a tabela Tecnologias
for i in range(1, 11):  # Inserir 10 tecnologias
    tecnologia_nome = fake.word()
    area_id = random.randint(1, 5)  # Escolher uma área aleatória
    cursor.execute("INSERT INTO Tecnologias (TecnologiaID, NomeTecnologia, AreaID) VALUES (%s, %s, %s)",
                   (i, tecnologia_nome, area_id))

# Preencher a tabela Empresas
for i in range(1, 11):  # Inserir 10 empresas
    empresa_nome = fake.company()
    localizacao = fake.city()
    contato_email = fake.email()
    cursor.execute("INSERT INTO Empresas (EmpresaID, NomeEmpresa, Localizacao, ContatoEmail) VALUES (%s, %s, %s, %s)",
                   (i, empresa_nome, localizacao, contato_email))

# Preencher a tabela EmpresaTecnologia (relacionamento entre Empresas e Tecnologias)
for i in range(1, 11):  # Relacionar cada empresa com até 3 tecnologias aleatórias
    empresa_id = i
    tecnologias_ids = random.sample(range(1, 11), random.randint(1, 3))
    for tecnologia_id in tecnologias_ids:
        cursor.execute("INSERT INTO EmpresaTecnologia (EmpresaID, TecnologiaID) VALUES (%s, %s)", (empresa_id, tecnologia_id))

# Preencher a tabela Colaboradores
for i in range(1, 21):  # Inserir 20 colaboradores
    colaborador_nome = fake.name()
    cargo = fake.job()
    empresa_id = random.randint(1, 10)  # Escolher uma empresa aleatória
    cursor.execute("INSERT INTO Colaboradores (ColaboradorID, NomeColaborador, Cargo, EmpresaID) VALUES (%s, %s, %s, %s)",
                   (i, colaborador_nome, cargo, empresa_id))

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()
