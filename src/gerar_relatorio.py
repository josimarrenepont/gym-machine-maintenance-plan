def gerar_relatorio_preventivo(df):
    relatorio = []
    media_uso_por_maquina = df.groupby('Maquina')['Horas de Uso'].mean()
    
    for maquina, media_uso in media_uso_por_maquina.items():
        if media_uso > 300:
            relatorio.append(f"Sugere-se realizar manutenção preventiva na máquina {maquina}, pois ela ultrapassou as 300 horas de uso (Média: {media_uso:.2f} horas).")
        else:
            relatorio.append(f"A máquina {maquina} está dentro dos padrões normais de uso (Média: {media_uso:.2f} horas).")
    
    return relatorio
