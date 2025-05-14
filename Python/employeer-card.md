import random as profile

eye_color = profile.choice(['Azul', 'Azul Claro', 'Cinza', 'Verde', 'Marrom'])
hair_color = profile.choice(['Preto', 'Vermelho', 'Loiro', 'Castanho', 'Castanho'])
fav_color = profile.choice(['Amarelo', 'Verde', 'Vermelho', 'Laranja', 'Azul',
 'Rosa', 'Branco', 'Preto', 'Marrom', 'Roxo', 'Cinza'])

if profile.randint(0, 1):
    gender = 'Male'
    name = profile.choice(['Alex', 'Michael', 'Samuel', 'Daniel', 'Orlando', 'Wesley', 'Carlos', 'Oscar', 'André',
                          'Fernando', 'Eric', 'Davi', 'Edgar', 'Danilo', 'Charles', 'Bruno', 'Arthur', 'Frederico', 'Adriano', 'Marcos'])
else:
    gender = 'Female'
    name = profile.choice(['Daiana', 'Marta', 'Amanda', 'Alice', 'Barbara', 'Ana', 'Valéria', 'Viviane',
                          'Gabriela', 'Katia', 'Elizabete', 'Julieta', 'Vitória', 'Sarah', 'Maria', 'Eva', 'Andressa', 'Sofia'])

print('Gênero:', gender)
print('Nome:', name)
print('Cor dos olhos:', eye_color)
print('Cor do cabelo:', hair_color)
print('Cor favorita:', fav_color)
