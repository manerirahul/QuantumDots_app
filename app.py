from flask import Flask, render_template_string

app = Flask(__name__)

# Frontend HTML inside Python using render_template_string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Twin Chemical Ensembles for Near-Infrared-Emitting Graphene Quantum Dot Therapeutics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            max-width: 700px;
            margin: 0 auto 30px;
        }
        .btn {
            display: inline-block;
            padding: 12px 20px;
            background: #e74c3c;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 1.1em;
        }
        .btn:hover {
            background: #c0392b;
        }
    </style>
</head>
<body>
    <h1>Cyber Twin Chemical Ensembles for Near-Infrared-Emitting Graphene Quantum Dot Therapeutics</h1>
    <section class="gqd-hero">
  <p>Designing NIR-bright, biocompatible graphene quantum dots using a digital “cyber twin” that learns from every experiment.</p>
  <img src="/assets/nir-invivo.jpg" alt="NIR in vivo imaging showing tumor contrast">
  <figcaption>Example NIR imaging in vivo; illustrates deep-tissue contrast. Credit: peer-reviewed literature (see references).</figcaption>
</section>

<section class="gqd-why">
  <h2>Why Near-Infrared GQDs?</h2>
  <ul>
    <li>Deeper, clearer imaging with reduced background</li>
    <li>Tunable red/NIR emission via size, edge states, and doping</li>
    <li>Theranostic platform: imaging + therapy</li>
  </ul>
  <div class="grid">
    <figure>
      <img src="/assets/gqd-tem.png" alt="TEM micrograph of graphene quantum dots">
      <figcaption>GQD morphology (TEM). Shows size/edge features related to emission.</figcaption>
    </figure>
    <figure>
      <img src="/assets/cell-internalization.png" alt="Confocal image of cells with GQDs">
      <figcaption>Cell internalization of functionalized GQDs; basis for targeted delivery.</figcaption>
    </figure>
  </div>
</section>

<section class="gqd-how">
  <h2>How the Cyber Twin Works</h2>
  <ol>
    <li><strong>Generate:</strong> create large virtual ensembles of GQD chemistries</li>
    <li><strong>Predict:</strong> model NIR emission, photostability, safety</li>
    <li><strong>Validate:</strong> synthesize top picks, characterize & test</li>
    <li><strong>Learn:</strong> feed results back to the twin to improve the next round</li>
  </ol>
  <img src="/assets/digital-twin.png" alt="Digital twin schematic linking data, models, and lab validation">
  <figcaption>Digital twin loop linking models ↔ lab data for rapid iteration.</figcaption>
</section>

<section class="gqd-use">
  <h2>Applications</h2>
  <ul>
    <li>NIR image-guided oncology (margin detection, response tracking)</li>
    <li>Multiplex biomarker imaging in NIR-I/II</li>
    <li>Personalized dosing via patient-specific twin simulations</li>
  </ul>
</section>

<section class="gqd-refs">
  <h2>References</h2>
  <p>See “Further Reading” below for sources and image credits.</p>
</section>
<section class="wavelength-checker">
  <h2>Wavelength Input</h2>
  <form action="/process" method="post">
    <label for="wavelength">Enter wavelength (in nm):</label>
    <input type="number" id="wavelength" name="wavelength" required>
    <button type="submit">Check</button>
  </form>
</section>

    <a href="#" class="btn">Learn More</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)