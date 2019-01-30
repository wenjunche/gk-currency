''' this contians the entity definition for a us license plate '''
# Each interpreter needs a list of patterns to look for

CURRENCY = {
  'label': 'CURRENCY',
  'values': (
    'USD',
    "EUR",
    'JPY',
  )
}

CURRENCY_PATTERNS = [[['CURRENCY']]]

ENTITY_DEFINITION = {
  'extraTokens': (CURRENCY,),
  'patterns': CURRENCY_PATTERNS,
}
