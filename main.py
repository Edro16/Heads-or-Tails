import random

print(r"""        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  /`       .-'~"-.       `\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'` ASCII art by jgs
""")

random_int = random.randint(0, 1)

prediction = input("Heads or Tails? - Game made by Edro\n> ").lower()

random_heads_or_tails = "Heads" if random_int == 0 else "Tails"

print(f"{random_heads_or_tails}: You've won.") if random_heads_or_tails.lower() == prediction else print(f"{random_heads_or_tails}: You've lost.")
