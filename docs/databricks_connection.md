# Configuração da conexão Databricks no Airflow

Este documento descreve como configurar a conexão `databricks_default` para usar com os DAGs deste projeto.

## 1. Configuração via CLI

Use o comando abaixo para criar a conexão no Airflow:

```bash
airflow connections add 'databricks_default' \
  --conn-uri 'databricks://token:<DATABRICKS_TOKEN>@<DATABRICKS_HOST>'
```

Substitua:
- `<DATABRICKS_TOKEN>`: token de acesso do Databricks.
- `<DATABRICKS_HOST>`: host do workspace Databricks, por exemplo `https://adb-123456789012345.10.azuredatabricks.net`.

## 2. Configuração manual

No UI do Airflow, vá em `Admin > Connections` e crie uma conexão com:

- Conn Id: `databricks_default`
- Conn Type: `Databricks`
- Host: seu host Databricks
- Token: seu token de acesso
- Extras: opcionalmente, parâmetros adicionais em JSON.

## 3. Verificação

Após configurar a conexão, reinicie o Airflow e verifique se os DAGs carregam corretamente e se as tarefas conseguem conectar ao Databricks.

## 4. Observações

- Os DAGs de exemplo usam `DatabricksSubmitRunOperator` e `DatabricksRunNowOperator`.
- Ajuste os IDs de job e os caminhos de notebook antes de executar em produção.
