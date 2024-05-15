class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # str(value).ljust(4, '0')
        return "%04d" % value
