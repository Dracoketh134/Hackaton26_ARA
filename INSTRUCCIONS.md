# Aprèn Català amb Pictogrames - Joc Interactiu

Joc educatiu visual per aprendre vocabulari en català usant pictogrames i traducció multilingüe (àrab, anglès, castellà, romanès).

## Fitxers

- `Javasc.html` - Interfície del joc (HTML + CSS + JavaScript)
- `vocab.json` - Vocabulari amb imatges i traduccions
- `scores.json` - Puntuacions guardades automàticament cada 10 segons
- `server.py` - Servidor Python per servir els fitxers i guardar puntuacions
- `Imatges/` - Carpeta amb pictogrames
  - `Basiques/` - Salutacions i paraules bàsiques
  - `Cos/` - Parts del cos

## Com executar

### 1. Instal·lar dependències (primera vegada)

```powershell
pip install flask flask-cors
```

### 2. Inicia el servidor

```powershell
python server.py
```

Hauries de veure:
```
Starting Catalan Quiz Server on http://127.0.0.1:5000
```

### 3. Obri el joc

Obre el navegador a: **http://127.0.0.1:5000**

## Funcionament

- El joc carrega un pictograma aleatori
- Mostra la imatge i la introducció en múltiples idiomes
- L'usuari tria la paraula correcta en català
- Cada resposta es marca en verd (correcte) o vermell (incorrecte)
- Les puntuacions es guarden automàticament a `scores.json` cada 10 segons
- El vocabulari es pot actualitzar modificant `vocab.json` (el joc es recarrega cada 30 segons)

## Puntuacions

Les puntuacions es guarden al fitxer `scores.json` amb el següent format:

```json
{
  "meta": { ... },
  "scores": [
    {
      "timestamp": "2026-06-13T12:34:56.789Z",
      "correct": 5,
      "total": 8,
      "percentage": 62
    }
  ]
}
```

Cada entrada es crea cada 10 segons amb les puntuacions actuals del joc.

## Afegir més vocabulari

Modifica `vocab.json` amb noves entries:

```json
{
  "id": "nova_paraula",
  "category": "Categoria",
  "image": "./Imatges/Categoria/fitxer.png",
  "word": "Paraula",
  "translations": {
    "en": "English",
    "es": "Español",
    "ar": "العربية",
    "ro": "Română"
  },
  "options": ["Opció1", "Opció2", "Opció3", "Paraula"]
}
```

## Problemes comuns

**Les imatges no es veuen:**
- Assegura't que la ruta a `Imatges/` és correcta
- Verifica que els fitxers PNG existeixen a la carpeta corresponent
- El servidor ha d'estar en marxa a http://127.0.0.1:5000

**La puntuació no es guarda:**
- Revisa la consola del navegador (F12) per veure errors
- Assegura't que el servidor está executant-se
- Verifica que tens permisos d'escriptura en la carpeta

## Estil

- Disseny modern amb tema fosc
- Interfície responsiva (funciona en mòbil)
- Animacions suaus i feedback visual immediat
- Tipografia característica i colors distintius
