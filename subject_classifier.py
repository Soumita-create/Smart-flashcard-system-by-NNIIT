def classify_subject(text: str) -> str:
    keywords = {
        "Physics": ["newton", "force", "acceleration", "velocity", "mass", "energy"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "animal", "dna"],
        "Math": ["algebra", "geometry", "calculus", "equation", "matrix", "integral"],
        "Chemistry": ["atom", "molecule", "reaction", "compound", "acid", "base"],
        "History": ["war", "revolution", "empire", "president", "ancient"],
        "Geography": ["continent", "country", "river", "mountain", "climate"],
        "Computer Science": ["algorithm", "data", "program", "python", "binary", "computer"]
    }

    text = text.lower()
    for subject, keys in keywords.items():
        if any(keyword in text for keyword in keys):
            return subject
    return "General"
