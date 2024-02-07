from medias import media
from status_aluno import status_do_aluno

resultado = status_do_aluno.media_alunos()
cont = 0
result = 0
res = 20
while cont < 6:

    res = media()
    result = result + res.nota()
    cont += 1

print(cont)
print(result)
print(res.res_media(result, cont))