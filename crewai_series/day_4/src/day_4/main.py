#!/usr/bin/env python
from crew import Day4Crew
import sys
from datetime import datetime

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'ai agents',
        'date': datetime.now().strftime("%Y-%m-%d")
    }
    Day4Crew().crew().kickoff(inputs=inputs)
run()