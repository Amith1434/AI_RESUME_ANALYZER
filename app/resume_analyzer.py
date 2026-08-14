SKILLS = [
    "python",
    "c++",
    "java",
    "sql",
    "pytorch",
    "tensorflow",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "git",
    "docker",
    "fastapi",
    "javascript",
    "react"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


if __name__ == "__main__":
    resume_text = """
    I am an AIML student with experience in Python,
    C++, PyTorch, SQL and Machine Learning.
    """

    skills = extract_skills(resume_text)

    print("Skills found:")
    print(skills)