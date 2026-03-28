from datetime import date

CUTOFF_DATE = date(2026, 6, 3)

def is_after_cutoff(today=None) -> bool:
  """Devuelve True si hoy (o la fecha pasada) es >= CUTOFF_DATE."""
  if today is None:
    today = date.today()
  return today >= CUTOFF_DATE