import pandas as pd
import copy
from sklearn.base import BaseEstimator, TransformerMixin

class Cleaner(BaseEstimator, TransformerMixin):

    def __init__(self, feature_name: str, style: str = "raw_text"):
        """
        This class only acts as a transformer. Its purpose is to clean a text feature

        :param feature_name: name of the feature to be cleaned
        :param style: string with one of the following values:
                       "raw text" -> "lower case, without numbers and special characters";
                       "regex" -> "matching a regex";
        """

        #cheking variable types
        if not (isinstance(feature_name, str)):
            raise TypeError("feature should be of type string and not {}".format(str(type(feature_name))))
        else:
            self.feature_name = feature_name

        # cheking variable types
        if not (isinstance(style, str)):
            raise TypeError("style should be of type str and not {}".format(str(type(style))))
        #checking if style has a valid value
        elif style not in ["raw_text", "regex"]:
            raise ValueError("{} is not a valid style.".format(style))
        else:
            self.style = style

    def raw_text(self, value: str):
        if not (isinstance(value, str)):
            raise TypeError("value sgould be of type str and not {}".format(str(type(value))))
        value_ = copy.copy(value)
        value_ = value_.lower() #to lower case
        #todo remove special characters
        #todo tabs
        #todo new lines
        #todo extra spaces
        return value_

    def transform(self, X, *_):
        return X.select_dtypes(exclude='object').copy()

    def fit(self, *_):
        return self


