from bs4 import BeautifulSoup as BS
from bs4 import Comment
html = "<!--include /text/header.html--> <!--getenv HTTP_USER_AGENT--> <!--ifsubstr $exec_result Mozilla-->   Hey, you are using Netscape!<p> <!--endif--> <!--sql database select * from table where user=\'$username\'--> <!--ifless $numentries 1-->   Sorry, that record does not exist<p> <!--endif exit-->   Welcome <!--$user-->!<p>   You have <!--$index:0--> credits left in your account.<p> <!--include /text/footer.html-->"
soup = BS(html, 'html.parser')

for comment in soup.find_all(text=lambda e: isinstance(e, Comment)):
    comment.replace_with(comment.strip())

print(soup)
