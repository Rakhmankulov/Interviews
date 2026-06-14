## 📦 Что делает `python3 -m venv`

Команда:

```bash
python3 -m venv <имя_папки>
```

создаёт **изолированное Python-окружение** (virtual environment), где:

* своя версия `pip`
* свои зависимости
* не ломается системный Python
* удобно для LLM / RAG / k8s-утилит

---

# 🔹 Активируем окружение

### Linux / macOS

```bash
source rag/bin/activate
```

После активации увидишь:

```bash
(rag) user@host:~$
```

Теперь:

* `python` → это python из venv
* `pip` → ставит пакеты внутрь `rag`

---

# 🔹 Проверка

```bash
which python
```

Должно показать:

```
.../rag/bin/python
```

---

# 🔹 Установка зависимостей (например для RAG)

```bash
pip install --upgrade pip
pip install langchain faiss-cpu sentence-transformers fastapi uvicorn
```

---

# 🔹 Деактивация

```bash
deactivate
```
---

# 💡 DevOps Best Practice

Для прод-проекта:

```bash
python3 -m venv .venv
```

Скрытая папка `.venv` — стандарт де-факто.

И добавить в `.gitignore`:

```
.venv/
```


