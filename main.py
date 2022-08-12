from bs4 import BeautifulSoup

with open('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #tags = soup.find('h5') #it's select only first tag
    #print(tags)
    #courses_html_tags = soup.find_all('h5') #it's select all tag
    
    #for course in courses_html_tags:
        #print(course.text)
    
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print('Name: ' + course_name + ' price:' + course_price)