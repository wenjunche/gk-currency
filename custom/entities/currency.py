''' this contians the entity definition for a us license plate '''
# Each interpreter needs a list of patterns to look for

CURRENCY = {
  'label': 'CURRENCY',
  'values': (
    "eur",
    'jpy',
    'usd',
  )
}

STATION_ABBREVIATIONS = (
  ('j p y', 'JPY'),
  ('u s d', 'USD'),
)

def clean_currency(transcript):
  replacements = [
    ("euro", "EUR"),
    ("japan", "JPY"),
    # etc
  ]
  for key, value in replacements.items():
    transcript = transcript.replace(key, value)
  return transcript

CURRENCY_PATTERNS = [[['CURRENCY']]]

ENTITY_DEFINITION = {
  'extraTokens': (CURRENCY,),
  'patterns': CURRENCY_PATTERNS,
  'collapsiblePatterns': STATION_ABBREVIATIONS,
 }
