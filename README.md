# Gerador de Senhas Personalizável

Este projeto é um **gerador de senhas** em Python que permite a criação de senhas com diferentes níveis de complexidade ou com configurações personalizadas. Ele é útil para quem deseja gerar senhas seguras e adequadas às suas necessidades, sejam elas básicas ou avançadas.

## Funcionalidades

O script possui duas funções principais de geração de senhas:
1. **Senhas por Nível**: 
   - Básico (B): apenas letras, com 6 caracteres.
   - Médio (M): letras e números, com 8 caracteres.
   - Avançado (A): letras, números e caracteres especiais, com 12 caracteres.

2. **Senhas Customizáveis**:
   - O usuário pode definir o tamanho da senha e escolher se deseja incluir números e/ou caracteres especiais.

3. **Listar Senhas Geradas**:
   - O programa armazena e exibe todas as senhas geradas durante a sessão.

## Estrutura do Menu

Ao rodar o script, o usuário verá um menu com as seguintes opções:

1. **Gerar senha por nível**: Gera uma senha com base no nível de complexidade desejado:
   - [B] Básico
   - [M] Médio
   - [A] Avançado

2. **Gerar senha customizável**: Permite configurar o tamanho e os tipos de caracteres incluídos na senha (números e caracteres especiais).

3. **Listar senhas**: Mostra todas as senhas geradas na sessão atual.

4. **Sair**: Encerra o programa.

## Exemplo de Uso

O usuário seleciona uma das opções, como **Gerar senha customizável**, define o tamanho desejado e especifica se deseja incluir números e caracteres especiais. A senha é gerada de acordo com as configurações escolhidas e exibida no console.
