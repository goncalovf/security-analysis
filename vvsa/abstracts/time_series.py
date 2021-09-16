from abc import ABC


class Time_Series(ABC):
    def __init__(self, name, series, **alter_series_params):
        self.name = name
        self.series = series.dropna()
        if alter_series_params:
            self.alter_time_series(**alter_series_params)

    def alter_time_series(self, **params):
        """
        Args
        ----
        s: EOD_Series
            The time series to alter.

        params: dictionary
            Params that describe how the series should be altered.
        """
        s = self.series

        if "start_date" in params and params["start_date"] is not None:
            s = s.loc[params["start_date"] :]

        if "end_date" in params and params["end_date"] is not None:
            s = s.loc[: params["end_date"]]

        if "base" in params and params["base"] > 0:
            s = s / s[0] * params["base"]

        if "resample_rule" in params and params["resample_rule"] is not None:
            label = params["label"] if "label" in params else "left"

            if "resampling_method" in params and params["resampling_method"] == "last":
                s = s.resample(params["resample_rule"], label=label).last()
            else:
                s = s.resample(params["resample_rule"], label=label).first()

        self.series = s

        return self
