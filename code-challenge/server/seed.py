from models import db, Power, Hero, Hero_power
from app import app
import random


with app.app_context():
    
    Power.query.delete()
    Hero.query.delete()
    Hero_power.query.delete()

    print("🦸‍♀️ Seeding powers...")
    pow1 = Power(name= "super strength", description= "gives the wielder super-human strengths",)
    pow2 = Power(name= "flight", description= "gives the wielder the ability to fly through the skies at supersonic speed",)
    pow3 = Power(name= "super human senses", description= "allows the wielder to use her senses at a super-human level",)
    pow4 = Power(name= "elasticity", description= "can stretch the human body to extreme lengths",) 
  
    db.session.add_all([pow1, pow2, pow3, pow4])

    print("🦸‍♀️ Seeding heroes...")
    hero1 = Hero(name= "Kamala Khan", super_name= "Ms. Marvel",)
    hero2 = Hero(name= "Doreen Green", super_name= "Squirrel Girl",)
    hero3 = Hero(name= "Gwen Stacy", super_name= "Spider-Gwen",)
    hero4 = Hero(name= "Janet Van Dyne", super_name= "The Wasp",)
    hero5 = Hero(name= "Wanda Maximoff", super_name= "Scarlet Witch",)
    hero6 = Hero(name= "Carol Danvers", super_name= "Captain Marvel",)
    hero7 = Hero(name= "Jean Grey", super_name= "Dark Phoenix",)
    hero8 = Hero(name= "Ororo Munroe", super_name= "Storm",)
    hero9 = Hero(name= "Kitty Pryde", super_name= "Shadowcat",)
    hero10 = Hero(name= "Elektra Natchios", super_name= "Elektra",)

    db.session.add_all([hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10])

    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    
    hp1 = Hero_power(strength= random.choice(strengths), hero_id=1,power_id=1,)
    hp2 = Hero_power(strength= random.choice(strengths), hero_id=1,power_id=2,)
    hp3 = Hero_power(strength= random.choice(strengths), hero_id=2,power_id=3,)
    hp4 = Hero_power(strength= random.choice(strengths), hero_id=3,power_id=4,)
    hp5 = Hero_power(strength= random.choice(strengths), hero_id=3,power_id=1,)
    hp6 = Hero_power(strength= random.choice(strengths), hero_id=4,power_id=2,)
    hp7 = Hero_power(strength= random.choice(strengths), hero_id=5,power_id=3,)
    hp8 = Hero_power(strength= random.choice(strengths), hero_id=5,power_id=4,)
    hp9 = Hero_power(strength= random.choice(strengths), hero_id=6,power_id=1,)
    hp10 = Hero_power(strength= random.choice(strengths), hero_id=6,power_id=2,)
    hp11 = Hero_power(strength= random.choice(strengths), hero_id=7,power_id=3,)
    hp12 = Hero_power(strength= random.choice(strengths), hero_id=8,power_id=4,)
    hp13 = Hero_power(strength= random.choice(strengths), hero_id=8,power_id=1,)
    hp14 = Hero_power(strength= random.choice(strengths), hero_id=9,power_id=2,)
    hp15 = Hero_power(strength= random.choice(strengths), hero_id=10,power_id=3,)
    hp16 = Hero_power(strength= random.choice(strengths), hero_id=10,power_id=4,)

    db.session.add_all([hp1, hp2, hp3, hp4, hp5, hp6, hp7, hp8, hp9, hp10, hp11, hp12, hp13, hp14, hp15, hp16])
    db.session.commit()

    print("🦸‍♀️ Done seeding!")