# Backup Automático de Arquivos

Este script em Python realiza o backup automático dos arquivos contidos em uma pasta selecionada pelo usuário, criando uma cópia com data e hora em uma subpasta chamada `backup`.

## Funcionalidades

- Abre uma janela para o usuário selecionar uma pasta do computador.
- Cria uma pasta de backup dentro da pasta selecionada.
- Cria um novo subdiretório com a data e hora atual.
- Copia arquivos e subpastas (exceto a pasta de backup) para esse novo diretório.

## Requisitos

- Python 3.x
- Módulos padrão: `os`, `shutil`, `datetime`, `tkinter`

## Como Usar

1. Certifique-se de ter o Python instalado.
2. Execute o script:
   ```bash
   python nome_do_arquivo.py
3. Uma janela será aberta solicitando que você selecione uma pasta.
4. O backup será criado dentro dessa pasta, em um diretório chamado backup/YYYY-MM-DD HHMMSS.

## Observações

* Arquivos são copiados utilizando shutil.copy2, preservando metadados.
* Subpastas (exceto backup) são copiadas com shutil.copytree.
* O script evita sobrescrever backups anteriores ao incluir a data e hora no nome da pasta.

## Exemplo de Estrutura de Backup

    pasta_selecionada/
    │
    ├── arquivo1.txt/
    ├── subpasta/
    ├── backup/
       └── 2025-05-06 153045/
          ├── arquivo1.txt
          └── subpasta/
        
## Licença
Este projeto é de uso livre para fins educacionais e pessoais.

