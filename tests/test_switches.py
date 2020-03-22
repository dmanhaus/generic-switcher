import switcher

class TestSwitches:
  def test_month_init(self, capsys):
    month_instance = switcher.switch('switches.months')

    months = ['Invalid request','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range(0, len(months)):
      out = month_instance.numbers_to_months(i)
      assert out == months[i]

    out 