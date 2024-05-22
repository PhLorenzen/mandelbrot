# Mandelbrot-Generator Python
## Projektbeschreibung
Dieses Projekt ist ein Fraktal-Generator, der die Mandelbrot-Menge visualisiert. Das Programm ermöglicht es Benutzern, durch Mausklicks zu zoomen und das Fraktal zu verschieben.

## Funktionalitäten
- Darstellung des Mandelbrot-Fraktals in einem grafischen Fenster.
- Interaktion durch Zoomen und Verschieben.
- Benutzerfreundliche Oberfläche zur Steuerung des Zooms und der Iterationstiefe.

## Klassenmodell
- **FractalGenerator**:\
   Diese Klasse ist für die Steuerung des Fraktal-Generators verantwortlich.
  
  - **Attribute**:
    - **canvas**: Tkinter Canvas, auf der das Fraktal dargestellt wird.
  - **Methoden**:
    - **\_\_init\_\_()**: Initialisiert das Fenster und die Canvas.
    - **draw_mandelbrot()**: Zeichnet das Mandelbrot-Fraktal.
    - **zoom_in(x, y)**: Vergrößert das Fraktal um den Punkt (x, y).
    - **zoom_out(x, y)**: Verkleinert das Fraktal um den Punkt (x, y).
    - **move(x_offset, y_offset)**: Verschiebt das Fraktal um die angegebene Verschiebung.

- **ZoomController (optional)**:\
Diese Klasse verwaltet das Zoomen des Fraktals.
   - **Methoden**:
     - **\_\_init\_\_()**(fractal_generator): Initialisiert den Zoom-Controller mit einer Instanz von FractalGenerator.
     - **zoom_in(x, y)**: Vergrößert das Fraktal um den Punkt (x, y).
     - **zoom_out(x, y)**: Verkleinert das Fraktal um den Punkt (x, y).

 - **MoveController (optional)**:\
Diese Klasse verwaltet das Verschieben des Fraktals.
Methoden:
   - **\_\_init\_\_(fractal_generator)**: Initialisiert den Move-Controller mit einer Instanz von FractalGenerator.
   - **move(x_offset, y_offset)**: Verschiebt das Fraktal um die angegebene Verschiebung.
## Beziehungen zwischen Klassen
- Die Klasse _**FractalGenerator**_ verwaltet die Darstellung und Interaktionen mit dem Fraktal.

- Der _**ZoomController**_ und der _**MoveController**_ können optional erstellt werden, um spezifische Funktionalitäten zu kapseln und mit der Hauptklasse zu interagieren.

## Ziel
Das Ziel dieses Projekts ist es, ein interaktives Fenster bereitzustellen, das die Mandelbrot-Menge darstellt. Benutzer sollen durch Mausklicks zoomen und das Fraktal verschieben können.

## Anforderungen
- Python 3.x
- Tkinter
## Installation und Verwendung
1. Klone das Repository: `git clone https://github.com/PhLorenzen/mandelbrot.git`
2. Navigiere in das Verzeichnis: `cd mandelbrot`
3. Führe das Programm aus: `python fractal_generator.py`
### Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.