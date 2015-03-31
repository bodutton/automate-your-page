def generate_lesson_HTML(lesson_title, lesson_content):
    html_text_1 = '''
    <div class="lesson-title">
        ''' + lesson_title
    html_text_2 = '''
    </div>
    <div class="lesson-content">
        ''' + lesson_content
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text


def pull_title(lesson):
    start_location = lesson.find('TITLE:')
    end_location = lesson.find('DESCRIPTION:')
    title = lesson[start_location+7 : end_location-1]
    return title

def pull_description(lesson):
    start_location = lesson.find('DESCRIPTION:')
    description = lesson[start_location+13 :]
    return description

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('TITLE:')
        next_lesson_end   = text.find('TITLE:', next_lesson_start + 1)
        lesson = text[next_lesson_start:next_lesson_end]
        text = text[next_lesson_end:]
    return lesson
        
LESSON_TEST_TEXT = '''Basics of the Web and HTML TITLE: How the Web Works DESCRIPTION: The Web, or internet, is a global network of computers that connects billions of users worldwide. Invented in the 90s, the Web has grown to host over 30 billion pages. The vast majority of the Web is made up of inter-linked hypertext documents written in a language called Hypertext Markup Language, or HTML. When you visit a website (www.example.com) you're actually sending an HTTP request from your computer to a server who in turn finds the appropriate HTML document and sends it back to your computer where your web browser interprets and displays it. This video does a good job of explaining more.

HTML

HTML Hypertext Markup Language makes up most of the content on the web. HTML dictates Text Content, what you see, Markup,what it looks like behind the scenes References to other documents, images and videos Links to other pages in the form of hyperlinks. 
Plain text equals plain text, markups do everything else.
'''


def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = pull_title(lesson)
        description = pull_description(lesson)
        lesson_html = generate_lesson_HTML(title, description)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html


print generate_all_html(LESSON_TEST_TEXT)