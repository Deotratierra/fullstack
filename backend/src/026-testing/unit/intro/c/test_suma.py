#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import load, clean
import pytest  # pip3 install pytest

C_LIB = "biblioteca"

def test_suma():
    biblioteca = load(C_LIB)
    assert biblioteca.suma(5, 5) == 10

@pytest.fixture(scope="module", autouse=True)
def mod_set_tear():
    """El código antes del yield se ejecuta antes
    de los tests de este módulo y el de después
    se ejecuta después"""
    # SETUP
    yield
    # TEARDOWN
    clean(C_LIB)