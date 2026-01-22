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
        
        # TREATMENT RECOMMENDATIONS (Evidence-Based)
        self.recommendations = {
            'major_depression': [
                "URGENT: Contact mental health professional within 24-48 hours",
                "Treatment: Cognitive Behavioral Therapy (CBT) proven most effective",
                "Medication: SSRI antidepressants (Prozac, Zoloft) if needed",
                "Daily activity scheduling - combat withdrawal",
                "Crisis Support: National Suicide Prevention Lifeline 988"
            ],
            
            'gad': [
                "Schedule therapy appointment within 1-2 weeks",
                "Treatment: CBT for anxiety - highly effective",
                "Practice: Progressive muscle relaxation (20 min daily)",
                "Reduce caffeine intake significantly",
                "Establish consistent sleep schedule"
            ],
            
            'panic_disorder': [
                "Medical evaluation needed - rule out heart issues first",
                "Treatment: Panic-focused CBT + breathing techniques",
                "Learn interoceptive exposure (face physical sensations)",
                "Avoid alcohol and caffeine - both worsen panic",
                "Emergency: 911 if severe chest pain"
            ],
            
            'social_anxiety': [
                "Treatment: CBT with gradual exposure therapy",
                "Start exposure hierarchy (easiest situations first)",
                "Challenge negative thoughts about social judgment",
                "Join safe group activities to practice",
                "Beta-blockers may help performance anxiety (doctor prescribed)"
            ],
            
            'ptsd': [
                "URGENT: Trauma-specialized therapist required",
                "Treatment: EMDR or Prolonged Exposure Therapy",
                "Establish safety first before processing trauma",
                "Avoid alcohol/drug self-medication",
                "Veterans: Call 988 then press 1"
            ],
            
            'ocd': [
                "Treatment: Exposure and Response Prevention (ERP) therapy",
                "Higher-dose SSRIs often needed (vs depression doses)",
                "Resist compulsions gradually - start small",
                "Find OCD specialist: iocdf.org therapist directory",
                "Family education important for support"
            ],
            
            'bipolar': [
                "Psychiatric evaluation URGENT - medication required",
                "Treatment: Mood stabilizers (Lithium/Valproate) essential",
                "Sleep regulation absolutely critical for stability",
                "Avoid alcohol/drugs - destabilizes mood severely",
                "Regular monitoring needed - don't skip appointments"
            ],
            
            'burnout': [
                "Take immediate time off work if possible",
                "Set firm work-life boundaries",
                "Therapy: Address perfectionism patterns",
                "Reconnect with purpose or consider career change",
                "Delegate tasks - you cannot do everything"
            ],
            
            'sad': [
                "Light therapy: 10,000 lux light box - 30 min morning",
                "Vitamin D supplementation (check levels)",
                "Maximize outdoor time during daylight",
                "Maintain exercise through winter months",
                "Preventive SSRI before winter if severe"
            ],
            
            'eating_disorder': [
                "Medical evaluation URGENT - can be life-threatening",
                "Treatment: Specialized eating disorder program",
                "CBT-E (Enhanced CBT) for eating disorders",
                "Nutritionist + therapist team approach",
                "NEDA Helpline: 1-800-931-2237"
            ],
            
            'substance_use': [
                "Medical detox may be needed - DON'T quit cold turkey",
                "Treatment: Motivational Enhancement + CBT",
                "Support groups: AA/NA or SMART Recovery",
                "Address underlying mental health issues",
                "SAMHSA Helpline: 1-800-662-4357"
            ]
        }

    def ask_symptom(self, symptom: str) -> bool:
        """
        Real-time interactive questioning
        Asks user about specific symptom and stores answer
        """
        symptom_display = symptom.replace('_', ' ').title()
        
        while True:
            response = input(f"\n  ➤ {symptom_display}? (yes/no): ").strip().lower()
            
            if response in ['yes', 'y']:
                self.answers[symptom] = True
                
                # Check for high-risk symptoms
                if symptom in self.high_risk_symptoms:
                    self.risk_factors.append(symptom)
                
                return True
            elif response in ['no', 'n']:
                self.answers[symptom] = False
                return False
            else:
                print("  ⚠️  Please answer 'yes' or 'no'")
    
    def count_yes(self, symptoms: List[str]) -> int:
        """Count how many symptoms user confirmed as 'yes'"""
        return sum(1 for s in symptoms if self.answers.get(s, False))
    
    def calculate_severity(self, symptoms: List[str]) -> int:
        """
        Calculate severity score using weighted heuristics
        Sum of weights for all 'yes' symptoms
        """
        score = 0
        for symptom in symptoms:
            if self.answers.get(symptom, False):
                weight = self.weights.get(symptom, self.default_weight)
                score += weight
        return score
    
    def calculate_confidence(self, yes_count: int, total: int) -> float:
        """Calculate confidence percentage"""
        return (yes_count / total * 100) if total > 0 else 0
    
    def get_severity_level(self, score: int) -> str:
        """Classify severity level based on score"""
        if score >= 20:
            return 'SEVERE'
        elif score >= 12:
            return 'MODERATE'
        elif score >= 8:
            return 'MILD'
        else:
            return 'MINIMAL'
    
    def meets_csp_constraints(self, yes_count: int, severity: int, confidence: float) -> bool:
        """
        CSP CONSTRAINTS for diagnosis
        All three conditions must be met:
        1. At least 3 symptoms matched
        2. Severity score >= 8
        3. Confidence >= 40%
        """
        return yes_count >= 3 and severity >= 8 and confidence >= 40
        
    
    def diagnose_condition(self, condition: str) -> Dict:
        """
        Diagnose a specific condition
        Returns diagnosis result with metrics
        """
        symptoms = self.symptoms[condition]
        
        for symptom in symptoms:
            if symptom not in self.answers:
                self.ask_symptom(symptom)
        
        yes_count = self.count_yes(symptoms)
        severity = self.calculate_severity(symptoms)
        confidence = self.calculate_confidence(yes_count, len(symptoms))
        
        if self.meets_csp_constraints(yes_count, severity, confidence):
            return {
                'condition': condition,
                'yes_count': yes_count,
                'severity': severity,
                'confidence': confidence,
                'level': self.get_severity_level(severity),
                'diagnosed': True
            }
        
        return None
    
    def check_crisis(self):     
        if self.risk_factors:
            print("\n" + "="*50)
            print("║  ⚠️  CRISIS ALERT - HIGH RISK DETECTED ⚠️  ║")
            print("="*50)
            print(f"\nHigh-risk symptoms detected: {', '.join(self.risk_factors)}")
            print("\n🚨 IMMEDIATE ACTIONS:")
            print("1. Call 988 (Suicide & Crisis Lifeline) NOW")
            print("2. Go to emergency room if in immediate danger")
            print("3. Do NOT stay alone - contact someone immediately")
            print("4. Remove means of self-harm")
            print()
    
    def display_result(self, result: Dict):
        print("\n┌" + "─"*48 + "┐")
        print(f"│ CONDITION: {result['condition'].upper()}")
        print("├" + "─"*48 + "┤")
        print(f"│ Symptoms Matched: {result['yes_count']}")
        print(f"│ Severity Score: {result['severity']} ({result['level']})")
        print(f"│ Confidence: {result['confidence']:.1f}%")
        print("└" + "─"*48 + "┘")
    
    def show_recommendations(self, condition: str):
        if condition in self.recommendations:
            print(f"\n━━ {condition.upper()} TREATMENT RECOMMENDATIONS ━━")
            for rec in self.recommendations[condition]:
                print(f"  • {rec}")
    
    def clear_session(self):
        self.answers.clear()
        self.risk_factors.clear()
    
    def run_assessment(self):
        self.clear_session()
        
        print("\n" + "="*55)
        print("║   MENTAL HEALTH EXPERT SYSTEM v3.0              ║")
        print("║   Real-Time Interactive Assessment               ║")
        print("="*55 + "\n")
        
        print("This system screens for 11 mental health conditions.")
        print("Answer honestly - all responses are confidential.")
        print("Available conditions: GAD, Panic Disorder, Social Anxiety,")
        print("Major Depression, SAD, PTSD, Burnout, OCD, Bipolar,")
        print("Eating Disorders, Substance Use\n")
        
        input("Press Enter to begin assessment...")
        
        results = []
        for condition in self.symptoms.keys():
            result = self.diagnose_condition(condition)
            if result:
                results.append(result)
        
        self.check_crisis()
        
        print("\n" + "="*55)
        print("║            ASSESSMENT RESULTS                    ║")
        print("="*55 + "\n")
        
        if not results:
            print("✓ No significant conditions detected based on screening\n")
            print("General Recommendations:")
            print("  • Continue healthy lifestyle practices")
            print("  • Monitor mental health regularly")
            print("  • Seek help if symptoms develop or worsen")
        else:
            print(f"Found {len(results)} condition(s) meeting diagnostic criteria:\n")
            
            for result in results:
                self.display_result(result)
            
            print("\n" + "="*55)
            print("║         TREATMENT RECOMMENDATIONS                ║")
            print("="*55)
            
            for result in results:
                self.show_recommendations(result['condition'])
        
        print("\n" + "─"*55)
        print("DISCLAIMER: This is a screening tool, NOT a diagnosis.")
        print("Consult a qualified mental health professional for")
        print("comprehensive evaluation and treatment.")
        print("─"*55 + "\n")
        
        self.save_report(results)
