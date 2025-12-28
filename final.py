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
        
        # SYMPTOM SEVERITY WEIGHTS (Heuristics)
        self.weights = {
        # CRITICAL - Immediate intervention (10 points)
        'suicidal_thoughts': 10,
        'fear_of_dying': 8,
            
        # SEVERE - Urgent care needed (5-7 points)
        'intrusive_memories': 6,
        'flashbacks': 7,
        'chest_pain': 6,
        'persistent_sadness': 5,
        'loss_of_interest': 5,
        'nightmares': 5,
        'periods_of_high_energy': 6,
        'distorted_body_image': 6,
            
        # MODERATE - Professional help recommended (3-4 points)
        'excessive_worry': 4,
        'restlessness': 3,
        'difficulty_concentrating': 3,
        'muscle_tension': 3,
        'sleep_problems': 4,
        'fear_of_judgment': 3,
        'avoid_social_situations': 4,
        'fatigue': 3,
        'emotional_exhaustion': 4,
        'repetitive_behaviors': 4,
        'mood_swings': 4,
        'binge_eating': 4,
        'unable_to_control_use': 5,
            
        # MILD - Monitoring needed (1-2 points)
        'cynicism': 2,
        'reduced_performance': 2,
        'sleep_changes': 2,
        'low_energy_seasonal': 2,
        'physical_symptoms_in_public': 2,
        'weight_gain': 2
        }
        
        # Default weight for unlisted symptoms
        self.default_weight = 2
        
        # HIGH RISK SYMPTOMS (Crisis Detection)
        self.high_risk_symptoms = [
            'suicidal_thoughts',
            'self_harm',
            'fear_of_dying'
        ]
        
