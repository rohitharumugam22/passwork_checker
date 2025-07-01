# Password Strength Checker 
A GUI-based tool to evaluate password security and provide actionable improvement suggestions

# Key Features
1. Real-time password strength assessment

2. Visual strength indicator (Weak/Medium/Strong)

3. Specific improvement suggestions

4. Criteria-based evaluation (length, character diversity)

5. No external dependencies (pure Python)

# Requirements
Python 3.6+


# Installation

Clone repository (if applicable)

      bash

      git clone https://github.com/rohitharumugam22/password_checker.git
      
      cd password-checker

No additional installation required

# Usage
      bash
      python password_checker.py
      

# Evaluation Criteria

The tool checks passwords against these security standards:

Length: Minimum 8 characters (+1 point)

Uppercase letters: At least one (A-Z) (+1 point)

Lowercase letters: At least one (a-z) (+1 point)

Numbers: At least one digit (0-9) (+1 point)

Special characters: At least one (!@#$%^&*_+-=) (+1 point)

# Scoring System
      Points	Rating
      
      0-1      Very Weak
      
      2-3      Medium	

      4-5      Strong	

