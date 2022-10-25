from datetime import datetime

class DateConverter:
   regex = r'[\d]{4}-[\d]{2}-[\d]{2}'
   format = '%Y-%m-%d'

   def to_python(self, str_value: str) -> datetime:
       return datetime.strptime(str_value, self.format)

   def to_url(self, py_value: datetime) -> str:
       return py_value.strftime(self.format)