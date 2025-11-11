# web-2025-2-SistemaDeMonitoramentodeConsumodeEnergia-Matheus-Wilson-backend
# ⚡ Sistema de Monitoramento de Consumo de Energia - Backend

## 👥 Integrantes
- Antônio Matheus de Oliveira Lima
- José Wilson Bezerra Neto

---

## 📝 Descrição do Projeto
É um sistema web desenvolvido para registrar, monitorar e analisar o consumo de energia elétrica em diferentes períodos.  
O objetivo é permitir que usuários acompanhem seu gasto em kWh e custo estimado, auxiliando na **consciência energética e sustentabilidade**.

Este repositório contém o **backend** da aplicação, responsável por:
- Gerenciar o banco de dados;
- Processar registros de consumo;
- Oferecer uma API RESTful para o frontend.

---

## 🧠 Tecnologias Utilizadas
- **Python 3.10+**
- **FastAPI** (framework principal)
- **SQLite / PostgreSQL** (banco de dados)
- **SQLAlchemy** (ORM)
- **Uvicorn** (servidor ASGI)
- **Pydantic** (validação de dados)

---

## ⚙️ Instruções para Executar o Projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/usuario/web-2025-2-SistemaDeMonitoramentodeConsumodeEnergia-Matheus-Wilson-backend.git
cd web-2025-2-SistemaDeMonitoramentodeConsumodeEnergia-Matheus-Wilson-backend
```
### 2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
```
### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 4. Execute o servidor:
```bash
uvicorn main:app --reload
```
### 5. Acesse a API:

Documentação automática: http://127.0.0.1:8000/docs

