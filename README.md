## Bugs and Solutions
1. base.css not found - file was not in css folder - just under it!
2. background image not loading - error in making tuple l157 settings.py - removed COMMA
3. migrations ok I think: 

![](screenshots/migrations.png)

4. python3 manage.py loaddata : categories ok but products key error has_sizes

Hi @Cairi S I had this issue too. It depends on whether you take the json file from Tim or Chris. Tim's is the one with the sizes and is formatted already and Chris' is the one without sizes and unformatted. I'm not sure why they are different or why Tim's hasn't been either removed or updated, but that is the issue :+1:

download from here(https://github.com/ckz8780/boutique_ado_v1)



![](screenshots/has_sizes.png)

4. Mixed up urls home and products when copy pasting so had them reversed

5. Categories badges not displaying below header. For loop not being read at all. No errors in terminal. Used print() statements to see that loop being missed and print {% current_categories %} raised an error page. Solved: Was missing  _ in current_categories in views.py

6. Error - bag.html - bag template does not exist in bag/bag.html. Solved forgot to create another bag folder inside bag/templates

7. Template does not exist - twice have created template directly in templates folder with subfolder within templates e.g products

8. Error removing products - POST error Jquery - but was missing import HTTPresponse in bag/views.py

