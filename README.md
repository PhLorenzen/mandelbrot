# Fraktal Viewer

## Projektbeschreibung
Der Fraktal Viewer ist eine Anwendung, die es Benutzern ermöglicht, verschiedene Fraktale auszuwählen, anzuzeigen und mit ihnen zu interagieren.

## Funktionalitäten
- Auswahl verschiedener Fraktale.
- Anzeige des ausgewählten Fraktals.
- Benutzerfreundliche Oberfläche zur Navigation und Auswahl der Fraktale.
- Zoom in das Fraktal mit der `+`-Taste.
- Zoom aus dem Fraktal mit der `-`-Taste.
- Bewegung des Fraktals mit den Pfeiltasten.

## Fraktale
Die Anwendung bietet derzeit die folgenden Fraktale zur Auswahl:
- Mandelbrot-Menge
- Julia-Menge
- Burning-Ship-Fraktal

## Klassenmodell
- **FractalGenerator**:\
   Diese Klasse ist für die Steuerung des Fraktal-Viewers verantwortlich.
  
  - **Attribute**:
    - **fractal_type**: Der Typ des ausgewählten Fraktals.
    - **x_min, x_max, y_min, y_max**: Grenzen des angezeigten Bereichs.
    - **width, height**: Breite und Höhe des Anzeigebereichs.
    - **max_iter**: Maximale Anzahl der Iterationen.
    - **zoom_factor**: Faktor zum Zoomen.
    - **move_factor**: Faktor zum Bewegen.
  - **Methoden**:
    - **\_\_init\_\_()**: Initialisiert das Fenster und die Benutzeroberfläche.
    - **create_widgets()**: Erstellt die Benutzeroberfläche.
    - **generate_fractal(fractal_type)**: Generiert das ausgewählte Fraktal.
    - **draw_fractal()**: Zeichnet das ausgewählte Fraktal.
    - **draw_mandelbrot()**: Zeichnet die Mandelbrot-Menge.
    - **draw_julia()**: Zeichnet die Julia-Menge.
    - **draw_burning_ship()**: Zeichnet das Burning-Ship-Fraktal.
    - **on_key_press(event)**: Handhabt Tastendrücke für Zoom und Bewegung.
    - **zoom_in()**: Zoomt in das Fraktal hinein.
    - **zoom_out()**: Zoomt aus dem Fraktal heraus.
    - **move_left()**: Bewegt das Fraktal nach links.
    - **move_right()**: Bewegt das Fraktal nach rechts.
    - **move_up()**: Bewegt das Fraktal nach oben.
    - **move_down()**: Bewegt das Fraktal nach unten.

## Ziel
Das Ziel dieses Projekts ist es, eine Anwendung bereitzustellen, die es Benutzern ermöglicht, verschiedene Fraktale auszuwählen, anzuzeigen und mit ihnen zu interagieren.

## Anforderungen
- Python 3.x
- Tkinter
- Matplotlib
- NumPy

## Installation und Verwendung
1. Klone das Repository: `git clone https://github.com/PhLorenzen/mandelbrot.git`
2. Navigiere in das Verzeichnis: `cd mandelbrot`
3. Installiere die erforderlichen Abhängigkeiten:
   ```sh
   pip install matplotlib numpy
4. Führe das Programm aus: python fractal_generator.py
5. Wähle das gewünschte Fraktal aus der Liste aus.
Verwende die +- und --Tasten zum Zoomen.
6. Verwende die Pfeiltasten, um das Fraktal zu bewegen.
## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.