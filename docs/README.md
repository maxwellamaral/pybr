# GitHub Pages - PyBR

Esta pasta contém o site do GitHub Pages para o projeto PyBR.

## ✅ Configuração Correta para GitHub Pages

Esta pasta `docs/` está configurada corretamente para ser publicada pelo GitHub Pages.

## 📁 Estrutura

```
docs/
├── _config.yml          # Configuração do Jekyll
├── index.md             # Página inicial
├── tutorial.md          # Tutorial
├── exercicios.md        # Lista de exercícios
├── referencia.md        # Referência da linguagem
└── README.md            # Este arquivo
```

## 🚀 Como Publicar no GitHub Pages

### 1. Fazer Push para o GitHub

```bash
git add .
git commit -m "Adicionar site GitHub Pages"
git push origin main
```

### 2. Ativar GitHub Pages

1. Vá em **Settings** > **Pages** no repositório
2. Em **Source**, selecione:
   - **Branch:** `main`
   - **Folder:** `/docs`
3. Clique em **Save**

### 3. Aguardar

O site estará disponível em aproximadamente 2-5 minutos em:

```
https://maxwellamaral.github.io/pybr/
```

## 📝 Atualizar Configuração

Antes de fazer push, edite `_config.yml`:

```yaml
repository: maxwellamaral/pybr  # Seu GitHub username
```

E atualize os links nos arquivos `.md` substituindo:
- `seu-usuario` pelo seu username do GitHub (já atualizado para maxwellamaral)

## 🌐 Páginas do Site

- **Início:** `/`
- **Tutorial:** `/tutorial`
- **Exercícios:** `/exercicios`
- **Referência:** `/referencia`

## 🎨 Personalização

### Mudar Tema

Edite `_config.yml` e altere:

```yaml
theme: jekyll-theme-slate  # ou outro tema
```

Temas disponíveis:
- `jekyll-theme-cayman` (atual)
- `jekyll-theme-minimal`
- `jekyll-theme-slate`
- `jekyll-theme-architect`

## ⚙️ Desenvolvimento Local

Para testar o site localmente com Docker:

```bash
cd docs
docker-compose up -d
```

Acesse: **http://localhost:4000**

Ver logs:
```bash
docker-compose logs -f
```

Parar:
```bash
docker-compose down
```

## 🔗 Links

- [Documentação GitHub Pages](https://docs.github.com/pages)
- [Temas Jekyll](https://pages.github.com/themes/)
- [Projeto Principal](../README.md)
