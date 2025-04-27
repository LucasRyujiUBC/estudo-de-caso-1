import os  # Biblioteca para manipulação de arquivos e diretórios
import pandas as pd  # type: ignore # Biblioteca para manipulação de dados
from sklearn.ensemble import RandomForestClassifier  # type: ignore # Algoritmo de aprendizado de máquina para classificação
from sklearn.model_selection import train_test_split  # type: ignore # Divisão dos dados para treinamento e teste
from sklearn.preprocessing import LabelEncoder  # type: ignore # Transformação de dados categóricos em numéricos
import matplotlib.pyplot as plt  # type: ignore # Biblioteca para criação de gráficos
import seaborn as sns  # type: ignore # Biblioteca para gráficos estatísticos

# Função para carregar logs a partir de um arquivo de texto
def carregar_logs(caminho):
    try:
        # Abre o arquivo e lê todas as linhas
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.readlines()
    except Exception as e:
        print(f"Erro ao carregar logs: {e}")  # Exibe mensagem de erro, se houver falha na leitura
        return []  # Retorna lista vazia em caso de erro

# Função para estruturar os dados do log em um DataFrame do Pandas
def estruturar_dados(logs):
    dados = []  # Lista para armazenar as linhas processadas
    for linha in logs:
        partes = linha.strip().split(" ", 2)  # Divide a linha em três partes: timestamp, tipo e mensagem
        if len(partes) >= 3:
            timestamp, resto = partes[0] + " " + partes[1], partes[2]
            if ": " in resto:
                tipo, mensagem = resto.split(": ", 1)  # Separa o tipo do evento e a mensagem correspondente
                dados.append([timestamp, tipo, mensagem])  # Adiciona os dados à lista
    return pd.DataFrame(dados, columns=["Timestamp", "Tipo", "Mensagem"])  # Retorna um DataFrame estruturado

# Função para pré-processamento dos logs
def preprocessar_logs(df):
    df["Timestamp"] = pd.to_datetime(df["Timestamp"].str.extract(r"\[(.*?)\]")[0], errors="coerce")  # Converte timestamp para formato de data/hora
    df["Mensagem_Limpa"] = df["Mensagem"].str.lower()  # Converte mensagens para minúsculas para análise uniforme
    df["Categoria"] = df["Tipo"].map({"INFO": 0, "WARNING": 1, "ERROR": 2, "CRITICAL": 3}).fillna(0)  # Mapeia categorias de eventos
    df["Mensagem_Limpa_Length"] = df["Mensagem_Limpa"].str.len()  # Calcula tamanho da mensagem para análise
    df["Palavra_Falha"] = df["Mensagem_Limpa"].apply(lambda x: 1 if "falha" in x or "grave" in x else 0)  # Identifica palavras críticas nas mensagens
    return df  # Retorna o DataFrame processado

# Função para detectar anomalias nos logs usando aprendizado de máquina
def detectar_anomalias(df):
    X = df[["Categoria", "Mensagem_Limpa_Length", "Palavra_Falha"]]  # Seleção de atributos para o modelo
    y = df["Categoria"]  # Rótulos da classificação
    
    # Divisão dos dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(random_state=42)  # Criação do modelo Random Forest
    modelo.fit(X_train, y_train)  # Treinamento do modelo
    
    df["Anomalia"] = modelo.predict(X)  # Predição de anomalias com base nos atributos
    return df  # Retorna o DataFrame atualizado

# Função para classificar eventos com base na previsão do modelo
def classificar_eventos(df):
    df["Classificacao"] = df["Anomalia"].apply(lambda x: "Normal" if x == 0 else "Suspeito" if x == 1 else "Crítico")  # Definição de categorias
    return df  # Retorna o DataFrame classificado

# Função para gerar alertas de eventos críticos
def gerar_alertas(df):
    eventos_criticos = df[df["Classificacao"] == "Crítico"]
    if not eventos_criticos.empty:
        print("🚨 ALERTA: Eventos Críticos Detectados!")
        print(eventos_criticos[["Timestamp", "Mensagem"]])
    else:
        print("Nenhum evento crítico detectado.")

# Função para gerar um relatório atualizado com os eventos processados
def gerar_relatorio(df):
    caminho_relatorio = r"relatorio\relatorio.txt"  # Caminho de saída do relatório
    
    try:
        os.makedirs(os.path.dirname(caminho_relatorio), exist_ok=True)  # Garante que o diretório existe
        
        # Escreve o relatório no arquivo
        with open(caminho_relatorio, "w", encoding="utf-8") as f:
            f.write("📌 RELATÓRIO DE LOGS 📌\n")
            f.write("=" * 50 + "\n")
            f.write(f"Total de eventos processados: {len(df)}\n")
            f.write(f"Eventos Críticos: {len(df[df['Classificacao'] == 'Crítico'])}\n")
            f.write(f"Eventos de Erro: {len(df[df['Tipo'] == 'ERROR'])}\n")
            f.write(f"Eventos de Aviso: {len(df[df['Tipo'] == 'WARNING'])}\n")
            
            # Adiciona eventos críticos ao relatório
            f.write("\n--- 🚨 Eventos Críticos ---\n")
            eventos_criticos = df[df["Classificacao"] == "Crítico"]
            for _, row in eventos_criticos.iterrows():
                f.write(f"{row['Timestamp']} - {row['Mensagem']}\n")
            
            # Adiciona eventos de erro
            f.write("\n--- ❌ Eventos de Erro ---\n")
            eventos_erro = df[df["Tipo"] == "ERROR"]
            for _, row in eventos_erro.iterrows():
                f.write(f"{row['Timestamp']} - {row['Mensagem']}\n")
            
            # Adiciona eventos de aviso
            f.write("\n--- ⚠️ Eventos de Aviso ---\n")
            eventos_aviso = df[df["Tipo"] == "WARNING"]
            for _, row in eventos_aviso.iterrows():
                f.write(f"{row['Timestamp']} - {row['Mensagem']}\n")
            
            f.write("\nRelatório gerado com sucesso!\n")  # Mensagem final
        print(f"✅ Relatório salvo em: {caminho_relatorio}")  # Confirmação de salvamento
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")  # Tratamento de erro

# Função para visualizar os dados com gráficos
def visualizar_dados(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="Classificacao", hue="Classificacao", palette="viridis", dodge=False, legend=False)  # Gráfico de contagem
    plt.title("Classificação de Eventos nos Logs")
    plt.xlabel("Classificação")
    plt.ylabel("Quantidade")
    plt.show()  # Exibe gráfico

# Caminho do log
caminho_logs = r"log\log.txt"

# Fluxo do programa: processamento completo dos logs
if os.path.exists(caminho_logs):
    logs = carregar_logs(caminho_logs)
    if logs:
        df_logs = estruturar_dados(logs)
        df_logs = preprocessar_logs(df_logs)
        df_logs = detectar_anomalias(df_logs)
        df_logs = classificar_eventos(df_logs)
        gerar_alertas(df_logs)
        gerar_relatorio(df_logs)
        visualizar_dados(df_logs)
    else:
        print("Não foi possível carregar os logs.")
else:
    print(f"Arquivo de logs não encontrado: {caminho_logs}")