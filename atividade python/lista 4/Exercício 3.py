animais = {
         "vertebrado": {
             "ave": {
                 "carnivoro": "aguia",
                 "onivoro": "pomba"
             },
             "mamifero": {
                 "onivoro": "homem",
                 "herbivoro": "vaca"
             }
         },
         "invertebrado": {
             "inseto": {
                 "hematofago": "pulga",
                 "herbivoro": "lagarta"
             },
             "anelideo": {
                 "hematofago": "sanguessuga",
                 "onivoro": "minhoca"
             }
         }
     }
tipo1 = input().strip()
tipo2 = input().strip()
tipo3 = input().strip()
print(animais[tipo1][tipo2][tipo3])
