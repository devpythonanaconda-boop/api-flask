# Flask + SQLite (SQLAlchemy)

Application Flask minimale utilisant SQLite via SQLAlchemy.

Instructions (PowerShell):

1. Créer et activer un virtualenv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Installer les dépendances

```powershell
pip install -r requirements.txt
```

3. Lancer l'application

```powershell
$env:FLASK_APP='app.py'; $env:FLASK_ENV='development'; python -m flask run
```

4. Ouvrir dans le navigateur: `http://127.0.0.1:5000`

La base `app.db` est créée automatiquement à la première requête.
# api-flask