"""
==================================================================
    MENTAL HEALTH EXPERT SYSTEM - REAL-TIME VERSION
    Interactive Assessment + CSP Constraints + Expert Rules
    Python Implementation with Knowledge Base
==================================================================
"""

import json
from datetime import datetime
from typing import List, Dict, Tuple

class MentalHealthExpertSystem:
    
    def __init__(self):
        """Initialize the expert system with knowledge base"""
        self.answers = {}
        self.risk_factors = []
        self.init_knowledge_base()
    
    def init_knowledge_base(self):
        """
        KNOWLEDGE BASE - Real-World Mental Health Conditions
        Structure: {condition: [symptoms]}
        """
        self.symptoms = {
            # ANXIETY DISORDERS
            'gad': [
                'excessive_worry',
                'restlessness',
                'difficulty_concentrating',
                'muscle_tension',
                'sleep_problems'
            ],
            
            'panic_disorder': [
                'sudden_intense_fear',
                'chest_pain',
                'rapid_heartbeat',
                'fear_of_dying',
                'sweating',
                'trembling'
            ],
            
            'social_anxiety': [
                'fear_of_judgment',
                'avoid_social_situations',
                'fear_of_embarrassment',
                'physical_symptoms_in_public'
            ],
            
            # DEPRESSION
            'major_depression': [
                'persistent_sadness',
                'loss_of_interest',
                'sleep_changes',
                'fatigue',
                'feelings_of_worthlessness',
                'difficulty_concentrating',
                'suicidal_thoughts'
            ],
            
            'sad': [
                'winter_depression',
                'oversleeping',
                'weight_gain',
                'low_energy_seasonal'
            ],
            
            # TRAUMA & STRESS
            'ptsd': [
                'intrusive_memories',
                'nightmares',
                'flashbacks',
                'avoidance_of_reminders',
                'hypervigilance',
                'emotional_numbness'
            ],
            
            'burnout': [
                'emotional_exhaustion',
                'cynicism',
                'reduced_performance',
                'chronic_work_stress'
            ],
            
            # OTHER CONDITIONS
            'ocd': [
                'intrusive_thoughts',
                'repetitive_behaviors',
                'compulsive_checking',
                'excessive_cleaning'
            ],
            
            'bipolar': [
                'mood_swings',
                'periods_of_high_energy',
                'periods_of_depression',
                'impulsive_behavior',
                'racing_thoughts'
            ],
            
            'eating_disorder': [
                'preoccupation_with_weight',
                'restrictive_eating',
                'binge_eating',
                'distorted_body_image'
            ],
            
            'substance_use': [
                'unable_to_control_use',
                'cravings',
                'neglecting_responsibilities',
                'continued_use_despite_harm'
            ]
        }
        