# Função para preprocessar dados novos
def preprocessar_dados(df):
    """
    Preprocessar dados para fazer predições
    """
    # Converter Yes/No para 1/0
    colunas_sim_nao = ['Partner', 'Dependents', 'PhoneService', 'OnlineSecurity', 
                       'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                       'StreamingTV', 'StreamingMovies', 'PaperlessBilling']
    
    for coluna in colunas_sim_nao:
        if coluna in df.columns:
            df[coluna] = df[coluna].map({'Yes': 1, 'No': 0})
    
    # Converter gender
    if 'gender' in df.columns:
        df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    
    return df

def fazer_predicao(modelo, dados):
    """
    Fazer predição com o modelo treinado
    """
    probabilidade = modelo.predict_proba(dados)[:, 1]
    predicao = modelo.predict(dados)
    
    return predicao, probabilidade
