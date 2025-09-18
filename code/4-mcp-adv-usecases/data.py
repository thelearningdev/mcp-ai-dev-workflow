lms_data = {
    "users": {
        "trainers": [
            {
                "id": "trainer_1",
                "name": "Alice",
                "role": "trainer",
                "category": "Python",
                "courses": [
                    {"id": "py_c1", "title": "Intro to Python", "level": "Starter"},
                    {"id": "py_c2", "title": "Python Data Types", "level": "Novice"},
                    {
                        "id": "py_c3",
                        "title": "Object-Oriented Python",
                        "level": "Intermediate",
                    },
                    {
                        "id": "py_c4",
                        "title": "Advanced Python Patterns",
                        "level": "Advanced",
                    },
                    {
                        "id": "py_c5",
                        "title": "Python for Data Science",
                        "level": "Expert",
                    },
                ],
                "assestrainernt": [
                    {
                        "q_id": "py_q1",
                        "question": "What is a Python list comprehension?",
                    },
                    {
                        "q_id": "py_q2",
                        "question": "Explain the difference between list and tuple.",
                    },
                    {
                        "q_id": "py_q3",
                        "question": "How does Python handle memory management?",
                    },
                    {"q_id": "py_q4", "question": "What is a metaclass in Python?"},
                    {
                        "q_id": "py_q5",
                        "question": "Explain the GIL (Global Interpreter Lock).",
                    },
                ],
            },
            {
                "id": "trainer_2",
                "name": "Bob",
                "role": "trainer",
                "category": "JavaScript",
                "courses": [
                    {"id": "js_c1", "title": "JS Basics", "level": "Starter"},
                    {"id": "js_c2", "title": "DOM Manipulation", "level": "Novice"},
                    {
                        "id": "js_c3",
                        "title": "Asynchronous JS",
                        "level": "Intermediate",
                    },
                    {"id": "js_c4", "title": "JS Design Patterns", "level": "Advanced"},
                    {
                        "id": "js_c5",
                        "title": "Building SPAs with JS",
                        "level": "Expert",
                    },
                ],
                "assestrainernt": [
                    {"q_id": "js_q1", "question": "What are closures in JavaScript?"},
                    {
                        "q_id": "js_q2",
                        "question": "Explain event bubbling and capturing.",
                    },
                    {
                        "q_id": "js_q3",
                        "question": "What is the difference between var, let, and const?",
                    },
                    {"q_id": "js_q4", "question": "Explain the concept of promises."},
                    {
                        "q_id": "js_q5",
                        "question": "What are ES6 modules and why use them?",
                    },
                ],
            },
            {
                "id": "trainer_3",
                "name": "Charlie",
                "role": "trainer",
                "category": "Design",
                "courses": [
                    {
                        "id": "ds_c1",
                        "title": "Intro to Design Principles",
                        "level": "Starter",
                    },
                    {"id": "ds_c2", "title": "Color Theory", "level": "Novice"},
                    {
                        "id": "ds_c3",
                        "title": "Typography in UI",
                        "level": "Intermediate",
                    },
                    {"id": "ds_c4", "title": "UX Patterns", "level": "Advanced"},
                    {"id": "ds_c5", "title": "Design Systems", "level": "Expert"},
                ],
                "assestrainernt": [
                    {
                        "q_id": "ds_q1",
                        "question": "What are the basic principles of design?",
                    },
                    {
                        "q_id": "ds_q2",
                        "question": "Explain the importance of contrast in UI.",
                    },
                    {
                        "q_id": "ds_q3",
                        "question": "How does typography affect readability?",
                    },
                    {
                        "q_id": "ds_q4",
                        "question": "What is a wireframe and why is it used?",
                    },
                    {
                        "q_id": "ds_q5",
                        "question": "How do you ensure accessibility in design?",
                    },
                ],
            },
        ],
        "students": [
            {
                "id": "stu_1",
                "name": "David",
                "role": "student",
                "exam_scores": {"python": 5, "javascript": 3, "design": 2},
            },
            {
                "id": "stu_2",
                "name": "Eve",
                "role": "student",
                "exam_scores": {"python": 2, "javascript": 4, "design": 1},
            },
            {
                "id": "stu_3",
                "name": "Frank",
                "role": "student",
                "exam_scores": {"python": 0, "javascript": 2, "design": 5},
            },
            {
                "id": "stu_4",
                "name": "Grace",
                "role": "student",
                "exam_scores": {"python": 3, "javascript": 3, "design": 3},
            },
            {
                "id": "stu_5",
                "name": "Heidi",
                "role": "student",
                "exam_scores": {"python": 1, "javascript": 1, "design": 1},
            },
            {
                "id": "stu_6",
                "name": "Ivan",
                "role": "student",
                "exam_scores": {"python": 4, "javascript": 2, "design": 0},
            },
            {
                "id": "stu_7",
                "name": "Judy",
                "role": "student",
                "exam_scores": {"python": 5, "javascript": 5, "design": 5},
            },
            {
                "id": "stu_8",
                "name": "Mallory",
                "role": "student",
                "exam_scores": {"python": 2, "javascript": 2, "design": 2},
            },
            {
                "id": "stu_9",
                "name": "Niaj",
                "role": "student",
                "exam_scores": {"python": 3, "javascript": 1, "design": 4},
            },
            {
                "id": "stu_10",
                "name": "Olivia",
                "role": "student",
                "exam_scores": {"python": 1, "javascript": 5, "design": 3},
            },
        ],
    },
    "recommendation_rules": {
        "5": "Advanced",
        "3": "Intermediate",
        "2": "Novice",
        "other": "Starter",
    },
}
