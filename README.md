# Flask Translator

Flask Translator is a simple Flask extension for handling translations in your web applications. It provides easy
integration with Flask applications to support multiple languages.

## Installation

You can install Flask Translator using pip:

```bash
pip install flask-translator
```

## Usage

### Example Project Directory Structure

```bash
your_project_directory/
|-- app.py
|-- translations/
| |-- messages.en.yaml
| |-- messages.tr.yaml
|-- templates/
| |-- index.html
|-- README.md
|-- requirements.txt
```

### Translation File Examples

```yaml
# translations/messages.en.yaml

request:
  schema:
    invalid_email: 'Please enter a valid email address!'
    invalid_username: 'Please enter a valid username!'
    invalid_or_email_username: 'Please enter a valid username or email address!'
```

```yaml
# translations/messages.tr.yaml

request:
  schema:
    invalid_email: 'Lütfen geçerli bir e-posta adresi girin!'
    invalid_username: 'Lütfen geçerli bir kullanıcı adı girin!'
    invalid_or_email_username: 'Lütfen geçerli bir kullanıcı adı veya e-posta adresi girin!'
```

Make sure to place your translation files in the specified `TRANSLATIONS_PATH` directory with the corresponding language codes following the ISO 639-1 standard.


### App Factory Usage

```python
# app.py

from flask import Flask, render_template
from flask_translator import Translator


def create_app():
    app = Flask(__name__)

    # Configure Flask Translator
    app.config['DEFAULT_LANG'] = 'tr'
    app.config['LANG_INITIALIZER'] = 'headers'
    app.config['DEFAULT_MESSAGE'] = 'Process finished!'
    app.config['TRANSLATIONS_PATH'] = 'translations'

    # Initialize Flask Translator with the app
    t = Translator()
    t.init_app(app)

    @app.route('/')
    def home():
        message = t.translate('request.schema.invalid_or_email_username')
        return render_template('index.html', message=message)

    return app
```

### Normal Application Usage

```python
# app.py

from flask import Flask, render_template
from flask_translator import Translator

app = Flask(__name__)

# Configure Flask Translator
app.config['DEFAULT_LANG'] = 'tr'
app.config['LANG_INITIALIZER'] = 'headers'
app.config['DEFAULT_MESSAGE'] = 'Process finished!'
app.config['TRANSLATIONS_PATH'] = 'translations'

# Initialize Flask Translator with the app
t = Translator(app)

@app.route('/')
def home():
    message = t.translate('request.schema.invalid_or_email_username')
    return render_template('index.html', message=message)

```

### Configuration Options

`DEFAULT_LANG`: The default language to use if no language is explicitly specified. Should be in ISO 639-1 code
standards. Default is '`en`' (English).

`LANG_INITIALIZER`: Determines the method to initialize the language. Possible values are 'headers', 'cookies', '
sessions'. If none of these values are present, it falls back to the `DEFAULT_LANG` value. Default is '`headers`'.

`DEFAULT_MESSAGE`: The default message to display if a translation is not found for the given key. Default
is '`Process finished!`'.

`TRANSLATIONS_PATH`: The path to the directory containing translation files. Default is '`translations`'.