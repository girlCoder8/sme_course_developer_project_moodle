# course.py

import json

# Course Information
course_info = {
    "title": "Effective Leadership and Management",
    "duration": "10 weeks",
    "target_audience": "Mid-level professionals looking to develop leadership and management skills",
    "platform": "Moodle"
}

# Accessibility and Inclusivity Considerations
accessibility = {
    "alt_text": "All images and infographics will include descriptive alt text.",
    "captioned_videos": "All video content will have closed captions.",
    "transcripts": "Transcripts for video and audio content will be provided.",
    "accessible_documents": "All documents will be provided in accessible formats (e.g., tagged PDFs).",
    "keyboard_navigation": "Ensure all interactive elements are accessible via keyboard.",
    "color_contrast": "High contrast color schemes will be used for readability.",
    "screen_reader_compatibility": "Ensure all content is compatible with screen readers."
}

# Weekly Content and Activities
weeks = [
    {
        "week": 1,
        "topic": "Introduction to Leadership",
        "objective": "Understand the fundamentals of leadership and its importance in organizational success.",
        "content": [
            {"type": "video", "title": "What is Leadership?", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Theories of Leadership", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Share an Example of Great Leadership"}
        ],
        "practical_activity": [
            {"type": "scenario", "title": "Read a case study about a leadership challenge and discuss possible "
                                          "solutions in groups", "accessibility": "ensure scenario description is "
                                                                                  "accessible"}
        ]
    },
    {
        "week": 2,
        "topic": "Communication Skills",
        "objective": "Develop effective communication skills for leadership.",
        "content": [
            {"type": "video", "title": "Effective Communication Techniques", "accessibility": "captioned, with "
                                                                                              "transcript"},
            {"type": "reading", "title": "The Role of Communication in Leadership", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Communication Barriers and How to Overcome Them"}
        ],
        "practical_activity": [
            {"type": "role_play", "title": "Conduct a simulated team meeting where participants practice active "
                                           "listening and clear communication", "accessibility": "instructions "
                                                                                                 "accessible, "
                                                                                                 "role descriptions "
                                                                                                 "provided in text "
                                                                                                 "format"}
        ]
    },
    {
        "week": 3,
        "topic": "Conflict Resolution",
        "objective": "Learn strategies to manage and resolve conflicts in the workplace.",
        "content": [
            {"type": "video", "title": "Conflict Resolution Strategies", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Managing Workplace Conflicts", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Share a Conflict You Experienced and How It Was Resolved"}
        ],
        "practical_activity": [
            {"type": "simulation", "title": "Participate in a conflict resolution simulation where learners take on "
                                            "different roles to practice negotiation and mediation", "accessibility":
                "accessible simulation software, clear text-based instructions"}
        ]
    },
    {
        "week": 4,
        "topic": "Decision Making and Problem Solving",
        "objective": "Enhance decision-making and problem-solving skills.",
        "content": [
            {"type": "video", "title": "Effective Decision-Making Processes", "accessibility": "captioned, with "
                                                                                               "transcript"},
            {"type": "reading", "title": "Problem-Solving Techniques", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Decision-Making Challenges and Solutions"}
        ],
        "practical_activity": [
            {"type": "scenario", "title": "Analyze a complex problem scenario and develop a step-by-step "
                                          "decision-making plan", "accessibility": "accessible scenario description "
                                                                                   "and instructions"}
        ]
    },
    {
        "week": 5,
        "topic": "Team Building and Motivation",
        "objective": "Understand the principles of team building and how to motivate team members.",
        "content": [
            {"type": "video", "title": "Building and Motivating Teams", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "The Psychology of Motivation", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Motivation Techniques in Your Experience"}
        ],
        "practical_activity": [
            {"type": "role_play", "title": "Conduct a team-building exercise where learners role-play as team leaders "
                                           "and members", "accessibility": "accessible role descriptions, "
                                                                           "instructions provided in text format"}
        ]
    },
    {
        "week": 6,
        "topic": "Leadership Styles",
        "objective": "Explore different leadership styles and their impact on team performance.",
        "content": [
            {"type": "video", "title": "Exploring Leadership Styles", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Leadership Styles and Their Effectiveness", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Which Leadership Style Resonates with You and Why?"}
        ],
        "practical_activity": [
            {"type": "scenario", "title": "Evaluate a scenario where different leadership styles are applied and "
                                          "discuss the outcomes", "accessibility": "accessible scenario description "
                                                                                   "and instructions"}
        ]
    },
    {
        "week": 7,
        "topic": "Strategic Planning",
        "objective": "Develop strategic planning skills for effective leadership.",
        "content": [
            {"type": "video", "title": "Introduction to Strategic Planning", "accessibility": "captioned, with "
                                                                                              "transcript"},
            {"type": "reading", "title": "Steps in Strategic Planning", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Strategic Planning Challenges in Your Industry"}
        ],
        "practical_activity": [
            {"type": "simulation", "title": "Create a strategic plan for a fictional company and present it to peers", "accessibility": "accessible simulation software, instructions provided in text format"}
        ]
    },
    {
        "week": 8,
        "topic": "Ethical Leadership",
        "objective": "Understand the importance of ethics in leadership.",
        "content": [
            {"type": "video", "title": "Ethical Leadership Principles", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Ethics in Leadership", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Discuss an Ethical Dilemma You Faced"}
        ],
        "practical_activity": [
            {"type": "scenario", "title": "Discuss and solve an ethical dilemma scenario", "accessibility": "accessible scenario description and instructions"}
        ]
    },
    {
        "week": 9,
        "topic": "Change Management",
        "objective": "Learn how to manage organizational change effectively.",
        "content": [
            {"type": "video", "title": "Change Management Strategies", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Leading Change in Organizations", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Experiences with Organizational Change"}
        ],
        "practical_activity": [
            {"type": "simulation", "title": "Participate in a change management simulation where learners practice "
                                            "leading a change initiative", "accessibility": "accessible simulation "
                                                                                            "software, instructions "
                                                                                            "provided in text format"}
        ]
    },
    {
        "week": 10,
        "topic": "Final Project and Review",
        "objective": "Apply the knowledge gained throughout the course to a comprehensive leadership and management "
                     "project.",
        "content": [
            {"type": "video", "title": "Synthesizing Leadership Skills", "accessibility": "captioned, with transcript"},
            {"type": "reading", "title": "Case Studies in Leadership", "accessibility": "accessible PDF"},
            {"type": "discussion_board", "title": "Course Reflections and Key Takeaways"}
        ],
        "assignments": [
            {"type": "final_project", "title": "Develop a leadership and management plan for a fictional company", "accessibility": "accessible project guidelines and instructions"},
            {"type": "peer_review", "title": "Provide feedback on classmates' final projects", "accessibility": "accessible review criteria and guidelines"}
        ]
    }
]

# Moodle Features Utilized
features = [
    "Announcements",
    "Course Content",
    "Forums",
    "Assignments",
    "Quizzes",
    "Grade book",
    "Collaborate"
]

# Additional Resources
resources = [
    "Office Hours: Weekly virtual office hours for Q&A sessions",
    "Supplementary Materials: Links to additional readings, videos, and tools",
    "Technical Support: Resources and contacts for technical assistance with Moodle"
]

