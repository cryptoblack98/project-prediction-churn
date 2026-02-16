# Projeto: Previsão de Churn 

## Objetivo

Prever quais clientes têm maior chance de cancelar o serviço nos próximos meses usando Machine Learning.

## Dataset

- **Fonte**: Telco Customer Churn (Kaggle)
- **Tamanho**: 7.032 clientes
- **Variáveis**: 21 features (demográficas, planos, uso de serviços)

## Estrutura do Projeto
```
project-previsão-churn/
├── data/
│   ├── raw/churn.csv (dados originais)
│   └── processed/churn_processed.csv (dados limpos)
├── notebooks/analysis.ipynb
├── src/model.py
├── README.md
└── .gitignore
```

## Modelos Utilizados

1. **Regressão Logística**: 73,21% de acurácia
2. **Gradient Boosting**: 79,10% de acurácia (melhor)

## Resultados

- ROC-AUC: 0,8317
- Precisão em detectar churn: 64%
- Recall em detectar churn: 49%

## Principais Fatores de Churn

- Internet fibra óptica
- Pagamento por cheque eletrônico
- Custos mensais altos
- Tempo de cliente baixo

## Como Usar

1. Ativar ambiente virtual: `source venv/bin/activate`
2. Abrir notebook: `jupyter notebook notebooks/analysis.ipynb`
3. Executar todas as células

## Bibliotecas Utilizadas

- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- scipy (testes estatísticos)