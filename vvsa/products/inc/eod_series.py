from vvsa.abstracts.time_series import Time_Series


class EOD_Series(Time_Series):
    def __init__(self, name, series, source, **alter_series_params):
        super().__init__(name, series, **alter_series_params)
        self.source = source
