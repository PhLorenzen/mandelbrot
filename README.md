# Fraktal Viewer
## Projektbeschreibung
Der Fraktal Viewer ist eine Anwendung, die es Benutzern ermöglicht, zwischen verschiedenen Fraktalen zu wählen und sie anzeigen zu lassen.

## Funktionalitäten
- Auswahl verschiedener Fraktale.
- Anzeige des ausgewählten Fraktals.
- Benutzerfreundliche Oberfläche zur Navigation und Auswahl der Fraktale

## Fraktale
Die Anwendung bietet derzeit die folgenden Fraktale zur Auswahl:

- Mandelbrot-Menge
- Julia-Menge
- Koch-Schneeflocke
- Sierpinski-Dreieck

## Klassenmodell
- **FractalViewer**:\
   Diese Klasse ist für die Steuerung des Fraktal-Viewers verantwortlich.
  
  - **Attribute**:
    - **selected_fractal**: Das ausgewählte Fraktal.
  - **Methoden**:
    - **\_\_init\_\_()**: Initialisiert das Fenster und die Benutzeroberfläche.
    - **show_fractal()**: Zeigt das ausgewählte Fraktal an.
    - **select_fractal(fractal)**: Wählt das angegebene Fraktal aus.


## Ziel
Das Ziel dieses Projekts ist es, eine Anwendung bereitzustellen, die es Benutzern ermöglicht, zwischen verschiedenen Fraktalen zu wählen und sie anzuzeigen.

## Anforderungen
- Python 3.x
- Tkinter
## Installation und Verwendung
1. Klone das Repository: `git clone https://github.com/PhLorenzen/mandelbrot.git`
2. Navigiere in das Verzeichnis: `cd mandelbrot`
3. Führe das Programm aus: `python fractal_generator.py`
4. Wähle das gewünschte Fraktal aus der Liste aus.
5. Das ausgewählte Fraktal wird angezeigt.
### Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.