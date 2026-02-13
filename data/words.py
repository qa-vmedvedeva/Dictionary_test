VALID_WORDS = [
    {
        "create": {"word": "apple", "translation": "яблоко"},
        "update": {"word": "Green Apple", "translation": "зелёное яблоко"},
    },
    {
        "create": {"word": "cat", "translation": "кот"},
        "update": {"word": "Home Cat", "translation": "домашний кот"},
    },
    {
        "create": {"word": "deteriorate", "translation": "ухудшаться"},
        "update": {"word": "Deteriorate", "translation": "Ухудшаться"},
    },
    {
        "create": {"word": "/d<e>teriorate", "translation": "\\\ухудшаться"},
        "update": {"word": "#$%^&*()-_+=``~Deteriorate", "translation": "</>$У$худшаться"},
    },
{
        "create": {'word': "Some people fail in school, but end up being successful in life. Why do you think that is the case? \
Education is considered the key to a successful life. However, there are many individuals being unsuccessful in school who gain significant accomplishments in future life. \
Firstly, the school system may not fit everyone because it does not take into account individual characteristics of students. Because of that, people with bright personalities, unique visions and dreams may be different from other students, which can lead to conflicts between the person and strict school rules. For instance, Steve Jobs and Bill Gates left college to follow their own plans, which led them to success. \n), school systems with focus on academic skills often can not attract students with talents in non-academic areas, such as music, arts or sports because such people who are interested in the development of their talents do not pay much attention to the school subjects. However, it does not stop them from achieving significant results in the future.\
And lastly, people struggling in school gain rich experience in conflict resolutions and relationship management which can be very useful in future life. \
To conclude, a lot of schools are not able to work with individuals who differ from the other students. Because of that, a person with a strong personality and non-academic talents can be unsuccessful in school and it is very important to find an individual approach to those students to help them find their own life path.\
", "translation": "ухудшаться"},
        "update": {"word": "Deteriorate", "translation": "Some people fail in school, but end up being successful in life. Why do you think that is the case? \
Education is considered the key to a successful life. However, there are many individuals being unsuccessful in school who gain significant accomplishments in future life. \
Firstly, the school system may not fit everyone because it does not take into account individual characteristics of students. Because of that, people with bright personalities, unique visions and dreams may be different from other students, which can lead to conflicts between the person and strict school rules. For instance, Steve Jobs and Bill Gates left college to follow their own plans, which led them to success. \n), school systems with focus on academic skills often can not attract students with talents in non-academic areas, such as music, arts or sports because such people who are interested in the development of their talents do not pay much attention to the school subjects. However, it does not stop them from achieving significant results in the future.\
And lastly, people struggling in school gain rich experience in conflict resolutions and relationship management which can be very useful in future life. \
To conclude, a lot of schools are not able to work with individuals who differ from the other students. Because of that, a person with a strong personality and non-academic talents can be unsuccessful in school and it is very important to find an individual approach to those students to help them find their own life path.\
"},
    },
]
INVALID_WORDS = [
    {"word": "", "translation": "яблоко"},
    {"word": "apple", "translation": ""},
]