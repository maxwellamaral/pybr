# Guia Rápido - Publicar no GitHub Pages

## ✅ Pré-requisitos

- Repositório no GitHub
- Git instalado

## 🚀 Passos para Publicar

### 1. Editar Configuração

Abra `docs/_config.yml` e altere:

```yaml
repository: SEU-USUARIO/pybr  # Seu username do GitHub
```

### 2. Commit e Push

```bash
git add .
git commit -m "Adicionar GitHub Pages"
git push origin main
```

### 3. Ativar GitHub Pages

1. Acesse seu repositório no GitHub
2. Vá em **Settings** > **Pages**
3. Em **Source**:
   - **Branch:** `main`
   - **Folder:** `/docs`
4. Clique em **Save**

### 4. Aguardar

O site estará em: `https://SEU-USUARIO.github.io/pybr/`

Leva ~2-5 minutos para ficar pronto.

## 🎯 Pronto!

Seu site estará online com:
- ✅ Tema profissional (Cayman)
- ✅ Tutorial interativo
- ✅ Lista de exercícios
- ✅ Referência completa
- ✅ Navegação entre páginas

## 📝 Personalizar

### Mudar tema

Edite `docs/_config.yml`:

```yaml
theme: jekyll-theme-slate  # ou outro
```

### Atualizar conteúdo

Edite os arquivos `.md` em `docs/` e faça push:

```bash
git add docs/
git commit -m "Atualizar conteúdo"
git push
```

O site atualiza automaticamente em ~2 minutos!

---

Para mais detalhes, veja [docs/README.md](docs/README.md)
