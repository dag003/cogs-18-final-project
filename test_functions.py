"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import (examing_results, beginning, quiz_options, ask_question)


def test_examing_results(): 
    
    assert callable(examing_results)
    assert isinstance(examing_results('8'), IPython.core.display.Image)

def test_beginning():

    assert callable(beginning)

def test_quiz_options():

    assert callable(quiz_options)
    

def test_ask_question():
    
    assert callable(ask_question)
    
def test_ask_question_purple():

    assert callable(ask_question_purple)

def test_examing_results_purple(): 
    
    assert callable(examing_results_purple)
    

    