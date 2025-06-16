import os
import zipfile

def zip_pasta(caminho_pasta, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, dirs, arquivos in os.walk(caminho_pasta):
            for arquivo in arquivos:

                caminho_completo = os.path.join(raiz, arquivo)
                caminho_relativo = os.path.relpath(caminho_completo, caminho_pasta)
                print(caminho_completo)
                print(caminho_relativo)
                zipf.write(caminho_completo, caminho_relativo)
        print('Processo finalizado com sucesso.')

# Exemplo de uso:
zip_pasta('/home/digolab/Downloads/meu-servlet-jetty',
           '/home/digolab/Downloads/meu-servlet-jetty.zip')
