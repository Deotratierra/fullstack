#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Database inputs verifier"""

class Verifier:
    """Class to verify database inputs

    All public methods has the next optional params:

        :param on_success: Callback if verification success
        :type on_success: function

        :param on_error: Callback if verification fails.
        :type on_error: function

    :param log_error: Callback for logs errors.
        Internal function self._log_error as default.
    :type log_error: function
    """
    def __init__(self, log_error=None):
        if not log_error:
            self.log_error = self._log_error

    def _log_error(self, error):
        """Default logger error method"""
        self.logger.database.error("VERIFY ERROR: %s", error)
   
    def verify_dict(self, data, fields_cls=None, 
                    lenght=None, **kwargs):
        """Verify a dictionary 

        :param data: Data to verify
        :type data: dict

        :param fields_cls: Fields classes to assert is instance.
            You can pass a dict or a class. In the first case,
            dicts keys must be the same that the data processed.
            In the last case, all fields will be asserted 
            against that class. If None, will not be asserted.
        :type fields_cls: list/any

        :param length: Number of keys
        :type lenght: int
        """
        def call_on_error(error):
            if "on_error" in kwargs:
                kwargs["on_error"](str(error))

        try:
            assert isinstance(data, dict) # verify_DICT
        except AssertionError as error:
            self.log_error("Data struct error: %s" % error)
            call_on_error(error)
        else:
            try:
                if lenght: assert len(data) == lenght # Lenght assert
            except AssertionError as error:
                self.log_error("Lenght error: %s" % error)
                call_on_error(error)
            else:
                try:
                    if fields_cls:  # Fields assertions
                        if isinstance(fields_cls, dict): # Classes in dict
                            for key, value in data.items():
                                assert isinstance(value, fields_cls[key])
                        else:                    # All the same class
                            for key, value in data.items():
                                assert isinstance(value, fields_cls)
                except Exception as error:
                    self.log_error(error)
                    call_on_error(error)
                else:
                    if "on_success" in kwargs:
                        kwargs["on_success"]()

    
