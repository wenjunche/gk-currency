MONTH = {
  'label': 'MONTH',
  'values': (
    'month',
  ),
}

MONTH_PATTERNS = [
  [['MONTH']], 
]

ENTITY_DEFINITION = {
  'patterns': MONTH_PATTERNS,
  'extraTokens': (MONTH,),
  'spacing': {
    'default': '',
  }
}
