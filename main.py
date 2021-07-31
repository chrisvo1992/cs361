from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuration

app = Flask(__name__)

# Routes
all_posts = [
    {
        'title' : 'Post 1',
        'content': 'This is the content of post 1.',
        'author': 'chris'
    },
    {
        'title' : 'Post 2',
        'content': 'This is the content of post 2.'
    }
]
ct = {
    "americano" : {"ingredients" : ["11/2 oz Campari", "11/2 oz Sweet Vermouth", "2 oz Club Soda", "Garnish: orange twist"],
                   "instructions" : ["1. Fill a highball glass with ice, then add the campari and sweet vermouth.",
                                     "2. Top with the club soda and stire gently to combine.",
                                     "3. Garnish with an orange twist."],
                   "img" : "https://www.liquor.com/thmb/BeSLdsxQ2pCBDtYVK0Z2hOmDdAs=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__liquor__2017__05__18075612__americano-720x720-article-50171f19cc644b05b8df563e06a647fd.jpg",
                   "src": "https://www.youtube.com/embed/TmeUJ2g3ogM",
                   "name" : "Americano"
                    },
    "aperol_spritz" : {"ingredients" : ["3 oz Prosecco", "2 oz Aperol", "1 oz Soda Water", "Garnish: orange slice"],
                       "instructions" : ["1. Add the prosecco, Aperol and club soda to a wine glass filled iwth ice and stir.",
                                         "2. Garnish with an orange slice."],
                       "img" : "https://www.liquor.com/thmb/07gvk8s3cIs2mIj9z2F6ZCu6X3U=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__04__24075106__Aperol-Spritz-720x720-recipe-d36b577de7974fd3a9051707c07bd30b.jpg",
                       "src" : "https://www.youtube.com/embed/cvxH8lHFKG0",
                       "name" : "Aperol Spritz"
                    },
    "bloody_mary" : {"ingredients" : ["celery salt", "1 lemon wedge", "1 lime wedge", "2 oz vodka", "4 oz tomato juice",
                                     "2 teaspoons prepared horseradish", "2 dashes Tabasco sauce", "2 dashes Worcestershire sauce",
                                     "1 pinch ground black pepper", "1 pinch smoked paprika", "Garnish: parsley sprig, green olives,"
                                                                                              "lime wedge, celery stalk"],
                     "instructions" : ["1. Pour some celery salt onto small plate.", "2. Rub the juicy side of the lemon or "
                                        "lime wedge along the lip of a pint glass.", "3. Roll the outer edge of the glass in celery"
                                        " salt until fully coated, then fill the glass with ice and set aside.", "4. Squeeze the "
                                        "lemon and lime wedges into a shaker and drop them in.", "5. Add the vodka, tomato juice, horseradish, "
                                        " Tabasco Worcestershire, black pepper, paprika, plus a pinch of celery salt along with ice and shake gently.",
                                       "6. Strain into the prepared glass.", "7. Garnish with parsley sprig, 2 speared green olivers, a lim wedge and a celery stalk."],
                    "img" : "https://www.liquor.com/thmb/EQoj4B-kUXtXGb4jyx_C5ytHDBE=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/bloody-mary-720x720-primary-28cf1aaa79d0424d951901fcc0a42e91.jpg",
                    "src" : "https://www.youtube.com/embed/rpEzoWNbgSk",
                     "name": "Blood Mary"
                    },
    "clover_club" :{ "ingredients" : ["2 oz gin", " 1/2 oz lemon juicie, freshly squeezed", "1/2 oz raspberry syrup",
                                     "1 egg white", "Garnish: 3 raspberries"],
                     "instructions" : ["1. Add the gin, lemon juice, raspberry syrup and egg white into a shaker with ice "
                                       "and shake vigorously until well-chilled.", "2. Strain into a chilled cocktail glass.",
                                       "3. Garnish with 2 speared raspberries."],
                     "img" : "",
                     "src" : "https://www.youtube.com/embed/j1v-1QchxcY",
                     "name" :"Clover Club"},
    "corpse_reviver" : { "ingredients" : ["1 oz cognac","1 oz Calvados", "1/2 oz sweet vermouth"],
                         "instructions" : ["1. Add the cognac, Calvadoes and sweet vermouth to a mixing glass and add ice.",
                                           "2. Stir until chilled and strain into a cocktail glass."],
                         "img": "",
                         "src" : "https://www.youtube.com/embed/YblPFVgPEKE",
                         "name" : "Corpse Reviver"
                        },
    "daiquiri" :        { "ingredients" : ["2 oz light run", "1 oz lime juice, freshly squeezed", "3/4 oz demerara sugar syrup",
                                           "Garnish: lime twist"],
                          "instructions" : ["1. Add the rum, lime juice and demarara sugar syrup to a shaker with ice.",
                                            "2. Shake until well chilled.", "3. Strain into a chilled coupe.", "4. Garnish with a lime twist."],
                          "img" : "",
                          "src" : "https://www.youtube.com/embed/TbRmNrAeymo",
                          "name" : "Daiquiri"
                        },
    "dark_n_stormy" :   { "ingredients" : ["2 oz Gosling's Black Seal Rum", "1/2 oz lime juicie, freshly squeezed",
                                            "Ginger beer, to top (about 5 oz)", "Garnish: lime wedge"],
                          "instructions" : ["1. Add rum and lime juicie to a tall glass filled with ice.",
                                            "2. Top with the ginger beer.",
                                            "3. Garnish with a lime wedge."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/FT43iTg0RYQ",
                          "name": "Dark N Stormy"
                        },
    "dry_martini" :     { "ingredients" : ["2 1/2 oz gin", "1/2 oz dry vermouth", "1 dash orange bitters", "Garnish: lemon twist"],
                          "instructions" : ["1. Add the gin, dry vermouth and orange bitters into a mixing glass with ice.",
                                            "2. Stir until very cold.", "3. Strain into a chilled cocktail glass.",
                                            "4. Garnish with a lemon twist."],
                          "img": "",
                          "src" : "https://www.youtube.com/embed/ApMR3IWYZHI",
                          "name": "Dry Martini"
                        },
    "espresso_martini" : { "ingredients" : ["1 oz vodka", " 1 oz Kahlua", "1 oz coffee"],
                           "instructions" :["1. Fill a Boston glass with ice.", "2. Add vodka, kahlua, and coffee into glass.",
                                            "3. Shake and double strain into a chilled coupe."],
                           "img": "",
                           "src" : "https://www.youtube.com/embed/nyRjNfDKQw4",
                           "name": "Espresso Martini"
                        },
    "french_75" :       { "ingredients" : ["1 oz Gin", ".5 oz Lemon Juice", ".5 oz Simple Syrup", "top champagne", "Garnish: lemon twist"],
                          "instructions" : ["1. Add the gin, lemon juice and simple syrup to a shaker with ice.",
                                            "2. Shake until well-chilled.",
                                            "3. Strain into a champagne flute.",
                                            "4. Top with champagne.",
                                            "5. Garnish with a lemon twist."],
                          "img": "",
                          "src" : "https://www.youtube.com/embed/g6jjDhuSj5o",
                          "name" : "French 75"
                        },
    "gimlet" :          { "ingredients" : [".75 oz Fresh Lime Juice", " .75 oz simple syrup", "2 oz Gin", "Garnish: lime wheel"],
                          "instructions" : ["1. Add the gin, lime juice and simple syrup to a shaker with ice.",
                                            "2. Shake until well-chilled.",
                                            "3. Strain into a chilled cocktail glass or a rocks glass filled with fresh ice.",
                                            "4. Garnish with a lime wheel."],
                          "img": "",
                          "src" : "https://www.youtube.com/embed/TuiCT7tDO88",
                          "name" : "Gimlet"
                        },
    "mai_tai" :         { "ingredients" : ["2 oz aged Jamaican/White Rum", ".75 oz orange curacao", "1 oz lime juice", ".5 oz Orgeat",
                                           "Garnish: Lime Wheel, Mint Sprig"],
                          "instructions" : ["1. Add the white rum,  curacao, lime juice and orgeat into a shaker with crushed ice.",
                                            "2. Shake lightly for about 3 seconds.",
                                            "3. Pour into a double rocks glass.",
                                            "4. Float the dark rum over the top.",
                                            "5. Garnish with a lime wheel and mint sprig."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/vTqNLJG2ExE",
                          "name" : "Mai Tai"
                        },
    "manhattan" :       { "ingredients" : ["2 oz Rye Whiskey", "1 oz Sweet Vermouth", "4-6 Dashes Angostura Bitters",
                                           "1 dash orange bitters", "Garnish: Luxardo Cherry"],
                          "instructions": ["1. Add the whiskey, sweet vermouth and both bitters to a mixing glass with ice.",
                                           "2. Stire until well-chilled.",
                                           "3. Strain into a chilled coupe.",
                                           "4. Garnish with a cherry."],
                          "img": "",
                          "src" : "https://www.youtube.com/embed/wiOxt4J5zaM",
                          "name" : "Manhattan"
                         },
    "margarita" :       { "ingredients" : ["1.5 oz Tequila", ".75 oz Cointreau", ".75 oz Fresh Lime Juice", "1/2 oz agave syrup",
                                           "1/2 orange liqueur", "Garnish : lime wheel"],
                          "instructions" : ["1. Add tequila, orange liquer, lime juice and agave syrup to a cocktail shaker filled with ice.",
                                            "2. Shake until well-chilled.",
                                            "3. Strain into a rocks glass over fresh ice.",
                                            "4. Garnish with a lime wheel."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/XhXgmkP1r3c",
                          "name": "Margarita"
                        },
    "mojito":           { "ingredients" : ["2 oz White Rum", "1 oz Fresh Lime Juice", ".75 oz sugar syrup 1:1", "6-8 Mint Leaves",
                                           "2 oz Soda"],
                          "instructions" : ["1. Tear and clap the mint leaves to release the oils.",
                                            "2. Add the mint to a hi-ball glass.",
                                            "3. Add the white rum, fresh lime and sugar syrup.",
                                            "4. Fill the ho-ball with ice.",
                                            "5. Add a dash of soda and stir thoroughly."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/NANdz-YKMUw",
                          "name" : "Mojito"
                        },
    "moscow_mule" :     { "ingredients" : ["2 oz Vodka", ".75 oz Lime Juice", "4 oz top ginger beer", "Garnish: Lime Wheel"],
                          "instructions" : ["1. Fill moscow mule mug (or highball glass) with ice, then add vodka and lime juice.",
                                            "2. Top with the ginger beer.",
                                            "3. Garnish with a lime wheel."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/69wSCFe4GAI",
                          "name": "Moscow Mule"
                         },
    "negroni" :         { "ingredients" : ["1.5 oz Gin", "1 oz Sweet Vermouth", "1 oz Campari", "Garnish : orange peel"],
                          "instructions" : ["1. Add the gin, campari and sweet vermouth to a mixing glass filled with ice.",
                                            "2. Stir until well-chilled",
                                            "3. Strain into a rocks glass filled with large ice cubes",
                                            "4. Garnish with an orange peel."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/2IXWmW1R898",
                          "name" : "Negroni"
                        },
    "old_fashioned" :   { "ingredients" : ["2 oz Bourbon Whiskey", ".3 oz Sugar Syrup (2:1)", "2 dashes of Angostura Bitters",
                                           "Garnish : orange peel"],
                          "instructions" : ["1. Fill a mixing glass with ice.",
                                            "2. Add whiskey, sugar syrup, and angostura bitters to mixing glass.",
                                            "3. Stire for 25 seconds or until adequately diluted.",
                                            "4. Strain over fresh ice into a double old fashioned glass.",
                                            "5. Garnish with a twist of orange peel."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/JzN8-dNHj-o",
                          "name" : "Old Fashioned"
                        },
    "paloma" :          { "ingredients" : ["2 oz Tequila", ".5 oz Fresh Lime Juice", "Pinch of salt", "Grapefruit soda",
                                           "Garnish: Wedge of lime"],
                          "instructions" : ["1. Add tequila, lime juice, salt, and soda to high ball glass.",
                                            "2. Fill with ice and top with grapefruit soda.",
                                            "3. Stir for 40 seconds.",
                                            "4. Garnish with wedge of lime."],
                          "img" : "",
                          "src": "https://www.youtube.com/embed/peYS5TJl8Tk",
                          "name": "Paloma"
                        },
    "penicillin" :       { "ingredients" : ["2 oz Blended Scotch Whiskey", " .75 oz Fresh Lemon Juice", " .75 oz Honey Ginger Syrup",
                                            ".25 oz Islay Whiskey", "Garnish: Skewered Ginger"],
                           "instructions" : ["1. Combine the whiskey, lemon juice, and syrup in a cocktail shaker.",
                                             "2. Shake with ice.",
                                             "3. Strain over fresh ice into an old fashioned glass.",
                                             "4. Float the Islay Whiskey.",
                                             "5. Garnish with ginger."],
                           "img": "",
                           "src" : "https://www.youtube.com/embed/KYixmx56Agk",
                           "name": "Penicillin"
                        },
    "pisco_sour" :      { "ingredients" : ["2 oz Pisco", ".75 oz Lime Juice", ".75 oz Simple Syrup", "1 egg white",
                                           "Garnish: Angostura Bitters"],
                          "instructions" : ["1. Add pisco, lime juice, simple syrup, and egg white into a shaker.",
                                            "2. Dry-shake (without ice) vigorously.",
                                            "3. Add ice and shake again until well-chilled.",
                                            "4. Strain into a chilled rocks glass.",
                                            "5. Garnish with 3 to 5 drops of Angostura bitters."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/JRkUtNlNN0U",
                          "name": "Pisco Sour"
                        },
    "sazerac" :         { "ingredients" : ["4 dashes Peychauds Bitters and Angostura Bitters", "1 Sugar Cube", "2 oz Rye Whiskey",
                                            "Garnish: Lemon Peel"],
                          "instructions" : ["1. In a mixing glass, muddle the sugar cube, water, and the Peychaud and Angostura bitters.",
                                            "2. Add the whiskey fill the mixing glass with ice and stir until well-chilled.",
                                            "3. Strain into the prepared glass.",
                                            "4. Twist the lemon peel over the drink's surface to express the peel's oils, then garnish with the peel."],
                          "img": "",
                          "src": "https://www.youtube.com/embed/RuZzOcjJUYw",
                          "name": "Sazerac"
                        },
    "vieux_carre" :     { "ingredients" : ["1 oz Rye Whiskey", " 1 oz Cognac", "1 oz Sweet Vermouth", "Dash of Benedictine liqueur",
                                           "2 Dashes of Angostura Bitters", " Garnish: Orange Twist and Luxardo Cherry"],
                          "instructions" : ["1. Add the whiskey, cognac, sweet vermouth, Benedictine and bitters into a mixing"
                                            " glass with ice.",
                                            "2. Stire until well-chilled.",
                                            "3. Strain into a rocks glass over fresh ice or cocktail glass.",
                                            "4. Garnish with a cheery, a lemon twist, or both."],
                          "img": '',
                          "src" : "https://www.youtube.com/embed/UR5rahGRxhs",
                          "name" : "Vieux Carre"
                        },
    "whiskey_sour" :    { "ingredients" : ["2 oz Whiskey", ".75 oz Lemon Juice", ".75 oz Simple Syrup", "1 egg white",
                                           "Garnish: Angostura Bitters"],
                          "instructions" : ["1. Add whiskey, lemon juice, simple syrup and egg white to a shaker.",
                                            "2. Dry shake(without ice) for 30 seconds.",
                                            "3. Add ice and shake again until well-chilled.",
                                            "4. Strain into a coupe glass.",
                                            "5. Garnish with 3 or 4 drops of Angostura bitters."],
                          "img":"",
                          "src" : "https://www.youtube.com/embed/hFKZPzfngcU",
                          "name" : "Whiskey Sour"
                        }
}



@app.route("/aboutus")
def hello():
    return render_template("about.html")

@app.route('/')
def root():
    return render_template("base.html")

@app.route("/home")
def result1():
    return render_template("result1.html")

@app.route("/results_2")
def result2():
    return render_template("result2.html")

@app.route("/results_3")
def result3():
    return render_template("result3.html")

@app.route("/<string:cocktail>", methods =['GET', 'POST'])
def information(cocktail):
    return render_template("information.html", posts=ct[cocktail])


#@app.route('/posts', methods=['GET', 'POST'])
#def posts():
#    if request.method == 'POST':
#        post_title = request.form['title']
#        post_content = request.form['content']
#        new_post = BlogPost(title=post_title, content=post_content, author='Aron')
#        db.session.add(new_post)
#        db.session.commit()
#        return redirect('/posts')
#    else:
#        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
#        return render_template('posts.html', posts = all_posts)


# Listener

if __name__ == "__main__":
    app.run(debug=True)

