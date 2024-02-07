class status_do_aluno():

    def media_alunos(self, nota):

        self.media = self.media + nota
        return self.media

total = status_do_aluno(10)
print(total.media_alunos(10))