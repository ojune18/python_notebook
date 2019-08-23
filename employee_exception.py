class EmployeeException(Exception):

    def __init__(self, _msg):
        super()
        self._msg = _msg

    @property
    def msg(self):
        return self._msg


class RejoiningException(EmployeeException):
    pass


class ExitProcessingException(EmployeeException):
    pass


class ContractException(EmployeeException):
    pass


r = RejoiningException('op')
print(r.msg)

a = [[{'Line No ': '1', 'Line Bounding Box ': '(15, 2, 170, 79)', 'Lowest Confidence ': '0',
       'Line texts ': [{'Column_No': '2', 'text_item': 'stuff1', 'y2': 100}]}], [
         {'Line No ': '1', 'Line Bounding Box ': '(15, 2, 170, 79)', 'Lowest Confidence ': '0',
          'Line texts ': [{'Column_No': '1', 'text_item': 'stuff2', 'y2': 100}]}], [
         {'Line No ': '1', 'Line Bounding Box ': '(15, 2, 170, 79)', 'Lowest Confidence ': '0',
          'Line texts ': [{'Column_No': '5', 'text_item': 'stuff3', 'y2': 101}]}]]
